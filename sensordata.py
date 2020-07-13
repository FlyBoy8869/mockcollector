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

    def generate_sensor_data(self, link_status, high_low: str, tolerance: str):
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
        print(f"link status: {link_status}")
        return self._flatten(
            [_link_combinations_to_data[(link_status, high_low, tolerance)]
                for link_status in link_status]
        )

    @staticmethod
    def make_key_combinations(serial_numbers, rssi_values):
        return [True if serial_num != "0" and rssi != "0" else False for serial_num, rssi in
                zip(serial_numbers, rssi_values)]

    @staticmethod
    def _flatten(sensor_readings):
        return [reading[index] for index in range(15) for reading in sensor_readings]


if __name__ == '__main__':
    from pprint import pprint

    sdg = SensorDataGenerator()
    pprint(sdg.generate_sensor_data([True, False, True, True, False, True], "7200", "NOMINAL"))
