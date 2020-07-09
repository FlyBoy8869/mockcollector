class RawConfigDataGenerator:
    SCALE_CURRENT_IN = ["0.02500"] * 6
    SCALE_CURRENT_OUT_HIGH = ["0.02625"] * 6
    SCALE_CURRENT_OUT_LOW = ["0.02375"] * 6

    SCALE_VOLTAGE_IN = ["1.50000"] * 6
    SCALE_VOLTAGE_OUT_HIGH = ["1.80000"] * 6
    SCALE_VOLTAGE_OUT_LOW = ["1.20000"] * 6

    CORRECTION_ANGLE_IN = ["0.0"] * 6
    CORRECTION_ANGLE_OUT_HIGH = ["45.0"] * 6
    CORRECTION_ANGLE_OUT_LOW = ["-45.0"] * 6

    FILLER = ["FILLER"] * 30

    scale_current = {
        "LOW": SCALE_CURRENT_OUT_LOW,
        "NOMINAL": SCALE_CURRENT_IN,
        "HIGH": SCALE_CURRENT_OUT_HIGH
    }

    scale_voltage = {
        "LOW": SCALE_VOLTAGE_OUT_LOW,
        "NOMINAL": SCALE_VOLTAGE_IN,
        "HIGH": SCALE_VOLTAGE_OUT_HIGH
    }

    correction_angle = {
        "LOW": CORRECTION_ANGLE_OUT_LOW,
        "NOMINAL": CORRECTION_ANGLE_IN,
        "HIGH": CORRECTION_ANGLE_OUT_HIGH
    }

    def generate_scale_current(self, tolerance: str, count: int):
        return self.scale_current[tolerance][0:count]

    def generate_scale_voltage(self, tolerance: str, count: int):
        return self.scale_voltage[tolerance][0:count]

    def generate_correction_angle(self, tolerance: str, count: int):
        return self.correction_angle[tolerance][0:count]


if __name__ == '__main__':
    g = RawConfigDataGenerator()
    print("scale current:", g.generate_scale_current("NOMINAL"))
    print("scale voltage:", g.generate_scale_voltage("HIGH"))
