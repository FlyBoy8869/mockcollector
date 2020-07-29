from typing import List, Dict

scale_current = {
    "LOW": ["0.02375"],
    "NOMINAL": ["0.02500"],
    "HIGH": ["0.02625"]
}

scale_voltage = {
    "LOW": ["1.20000"],
    "NOMINAL": ["1.50000"],
    "HIGH": ["1.80000"]
}

correction_angle = {
    "LOW": ["-45.0"],
    "NOMINAL": ["0.0"],
    "HIGH": ["45.0"]
}


def get_scale_currents(scale_currents: Dict[str, List[str]], tolerance: str, count: int) -> List[str]:
    return scale_currents[tolerance] * count


def get_scale_voltages(scale_voltages: Dict[str, List[str]], tolerance: str, count: int) -> List[str]:
    return scale_voltages[tolerance] * count


def get_correction_angles(correction_angles: Dict[str, List[str]], tolerance: str, count: int) -> List[str]:
    return correction_angles[tolerance] * count
