from typing import List


class SensorDataGenerator:
    _FILLER_DATA = ["FILLER"] * 9

    OUT_13800_LOW = ["13876.2", "119.88", "0.9000", "Lagging", "1482.948"] + _FILLER_DATA + ["6.1"]
    NOMINAL_13800 = ["13800.0", "120.0", "0.9000", "Lagging", "1490.40"] + _FILLER_DATA + ["21.7"]
    OUT_13800_HIGH = ["13813.8", "120.12", "0.9000", "Lagging", "1497.852"] + _FILLER_DATA + ["69.0"]

    OUT_7200_LOW = ["7192.8", "59.94", "0.9000", "Lagging", "386.856"] + _FILLER_DATA + ["6.1"]
    NOMINAL_7200 = ["7200.0", "60.0", "0.9000", "Lagging", "388.80"] + _FILLER_DATA + ["21.7"]
    OUT_7200_HIGH = ["7207.2", "60.06", "0.9000", "Lagging", "390.744"] + _FILLER_DATA + ["69.0"]

    # TODO: Replace 'NA' with a constant from LWTest.constants, that doesn't involve PyQt being a dependency.
    NO_LINK = ['NA'] * 15

    def generate_sensor_data(self, link_status, high_low: str, tolerance: str):
        """"""
        _link_combinations_to_data = {
            (True, "13800", "LOW"): self.OUT_13800_LOW,
            (True, "13800", "NOMINAL"): self.NOMINAL_13800,
            (True, "13800", "HIGH"): self.OUT_13800_HIGH,

            (False, "13800", "LOW"): self.NO_LINK,
            (False, "13800", "NOMINAL"): self.NO_LINK,
            (False, "13800", "HIGH"): self.NO_LINK,

            (True, "7200", "LOW"): self.OUT_7200_LOW,
            (True, "7200", "NOMINAL"): self.NOMINAL_7200,
            (True, "7200", "HIGH"): self.OUT_7200_HIGH,

            (False, "7200", "LOW"): self.NO_LINK,
            (False, "7200", "NOMINAL"): self.NO_LINK,
            (False, "7200", "HIGH"): self.NO_LINK,
        }
        return self._group_by_index(
            [_link_combinations_to_data[(link_status, high_low, tolerance)]
                for link_status in link_status],
            15
        )

    @staticmethod
    def sensor_link_status(serial_numbers: List[str], rssi_values: List[str]) -> List[bool]:
        """ Makes a list of True/False values based on sensor linking results.

        Args:
            serial_numbers: A list of sensor serial numbers e.g, ["9800001", "9800002", "0"].
            rssi_values: A list of rssi values e.g., ["-50", "-60", "0"].

        Returns:
            A list of boolean values e.g., [True, True, False]. An element is True if both corresponding elements of
                serial_numbers and rssi_values != "0", False otherwise.

        """
        return [True if serial_num != "0" and rssi != "0" else False for serial_num, rssi in
                zip(serial_numbers, rssi_values)]

    @staticmethod
    def _group_by_index(nested_list: List[List[str]], elements_per_list: int) -> List[str]:
        """Groups elements of a nested lists by index.

        Args:
            nested_list: a list of lists; all sub-lists must be of the same length
            elements_per_list: number of elements per sub-list

        Returns:
            A one dimensional list grouped by ascending index.

        """
        return [list_[index] for index in range(elements_per_list) for list_ in nested_list]
