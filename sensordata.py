class SensorDataGenerator:
    _FILLER_DATA = ["FILLER"] * 9

    OUT_13800_LOW = ["13876.2", "119.88", "0.9000", "Lagging", "1482.948"] + _FILLER_DATA + ["6.1"]
    OUT_13800_HIGH = ["13813.8", "120.12", "0.9000", "Lagging", "1497.852"] + _FILLER_DATA + ["69.0"]
    NOMINAL_13800 = ["13800.0", "120.0", "0.9000", "Lagging", "1490.40"] + _FILLER_DATA + ["21.7"]

    OUT_7200_LOW = ["7192.8", "59.94", "0.9000", "Lagging", "386.856"] + _FILLER_DATA + ["6.1"]
    NOMINAL_7200 = ["7200.0", "60.0", "0.9000", "Lagging", "388.80"] + _FILLER_DATA + ["21.7"]
    OUT_7200_HIGH = ["7207.2", "60.06", "0.9000", "Lagging", "390.744"] + _FILLER_DATA + ["69.0"]

    # TODO: Replace 'NA' with a constant from LWTest.constants, that doesn't involve PyQt being a dependency.
    NO_LINK = ['NA'] * 15

    _data_combinations = {
        (True, "13800", "LOW"): OUT_13800_LOW,
        (True, "13800", "NOMINAL"): NOMINAL_13800,
        (True, "13800", "HIGH"): OUT_13800_HIGH,

        (False, "13888", "LOW"): NO_LINK,
        (False, "13800", "NOMINAL"): NO_LINK,
        (False, "13800", "HIGH"): NO_LINK,

        (True, "7200", "LOW"): OUT_7200_LOW,
        (True, "7200", "NOMINAL"): NOMINAL_7200,
        (True, "7200", "HIGH"): OUT_7200_HIGH,

        (False, "7200", "LOW"): NO_LINK,
        (False, "7200", "NOMINAL"): NO_LINK,
        (False, "7200", "HIGH"): NO_LINK
    }

    def generate_sensor_data(self, link_status, high_low: str, tolerance: str):
        _link_combinations = {
            (True, "13800", "LOW"): lambda: self._generate_high_readings("LOW", True),
            (True, "13800", "NOMINAL"): lambda: self._generate_high_readings("NOMINAL", True),
            (True, "13800", "HIGH"): lambda: self._generate_high_readings("HIGH", True),

            (False, "13800", "LOW"): lambda: self._generate_high_readings("LOW", False),
            (False, "13800", "NOMINAL"): lambda: self._generate_high_readings("NOMINAL", False),
            (False, "13800", "OUT"): lambda: self._generate_high_readings("HIGH", False),

            (True, "7200", "LOW"): lambda: self._generate_low_readings("LOW", True),
            (True, "7200", "NOMINAL"): lambda: self._generate_low_readings("NOMINAL", True),
            (True, "7200", "HIGH"): lambda: self._generate_low_readings("HIGH", True),

            (False, "7200", "LOW"): lambda: self._generate_low_readings("LOW", False),
            (False, "7200", "NOMINAL"): lambda: self._generate_low_readings("NOMINAL", False),
            (False, "7200", "HIGH"): lambda: self._generate_low_readings("HIGH", False),
        }
        print(f"link status: {link_status}")
        return self._flatten(
            [_link_combinations[(link_status, high_low, tolerance)]()
                for link_status in link_status]
        )

    @staticmethod
    def make_key_combinations(serial_numbers, rssi_values):
        return [True if serial_num != "0" and rssi != "0" else False for serial_num, rssi in
                zip(serial_numbers.values(), rssi_values.values())]

    @staticmethod
    def _flatten(sensor_readings):
        return [reading[index] for index in range(15) for reading in sensor_readings]

    def _get_readings(self, link_status, high_low, tolerance):
        """

        :param link_status: a boolean indicating a sensor linked or not liked status
        :param high_low: a string indicating high voltage or low voltage
        :param tolerance: a string indicating if readings should be in tolerance, out of tolerance or random
        :return:

        >>> sdg = SensorDataGenerator()
        >>> sdg._get_readings(True, "13800", "NOMINAL")
        ['13800.0', '120.0', '0.9000', 'Lagging', '1490.40', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', '21.7']

        """
        return self._data_combinations[(link_status, high_low, tolerance)]

    def _generate_high_readings(self, tolerance: str, linked: bool):
        return self._get_readings(linked, "13800", tolerance)

    def _generate_low_readings(self, tolerance: str, linked:bool):
        return self._get_readings(linked, "7200", tolerance)


if __name__ == '__main__':
    from pprint import pprint

    sdg = SensorDataGenerator()
    pprint(sdg.generate_sensor_data([True, False, True, True, False, True], "7200", "IN"))
