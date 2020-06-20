from dataclasses import dataclass, field
from typing import Dict, Tuple


@dataclass
class DataRepository:
    serial_numbers: Dict[str, str] = \
        field(default_factory=lambda: {
            "serial_1": "9802386",
            "serial_2": "9802165",
            "serial_3": "9802316",
            "serial_4": "9802334",
            "serial_5": "9802310",
            "serial_6": "9802193"
        })

    rssi_values: Dict[str, str] = \
        field(default_factory=lambda: {
            "rssi_1": "-50",
            "rssi_2": "-55",
            "rssi_3": "-60",
            "rssi_4": "-65",
            "rssi_5": "-70",
            "rssi_6": "-75"
        })

    link_behaviour: str = "SAME_TIME"
    tolerance: str = "NOMINAL"
    tolerance_low_checked: str = ""
    tolerance_nominal_checked: str = "checked"
    tolerance_high_checked: str = ""

    voltage: str = "13800"
    high_data_checked: str = "checked"
    low_data_checked: str = ""

    raw_tolerance: str = "NOMINAL"
    raw_low: str = ""
    raw_nominal: str = "checked"
    raw_high: str = ""

    advanced_config_login: str = ""

    def transfer_from_settings(self, req):
        self.serial_numbers["serial_1"] = req.form["serial_1"]
        self.serial_numbers["serial_2"] = req.form["serial_2"]
        self.serial_numbers["serial_3"] = req.form["serial_3"]
        self.serial_numbers["serial_4"] = req.form["serial_4"]
        self.serial_numbers["serial_5"] = req.form["serial_5"]
        self.serial_numbers["serial_6"] = req.form["serial_6"]

        self.rssi_values["rssi_1"] = req.form["rssi_1"]
        self.rssi_values["rssi_2"] = req.form["rssi_2"]
        self.rssi_values["rssi_3"] = req.form["rssi_3"]
        self.rssi_values["rssi_4"] = req.form["rssi_4"]
        self.rssi_values["rssi_5"] = req.form["rssi_5"]
        self.rssi_values["rssi_6"] = req.form["rssi_6"]

        self.tolerance = req.form["tolerance"]
        self.persist_radio_button(self.tolerance,
                                  {
                                      "LOW": "tolerance_low_checked",
                                      "NOMINAL": "tolerance_nominal_checked",
                                      "HIGH": "tolerance_high_checked",
                                  })

        self.voltage = req.form["voltage"]
        self.persist_radio_button(self.voltage,
                                  {
                                      "7200": "low_data_checked",
                                      "13800": "high_data_checked"
                                  })

        self.raw_tolerance = req.form["raw_tolerance"]
        self.persist_radio_button(self.raw_tolerance,
                                  {
                                      "LOW": "raw_low",
                                      "NOMINAL": "raw_nominal",
                                      "HIGH": "raw_high"
                                  })

        self.advanced_config_login = req.form.get("advanced_config_login", "")

    def transfer_from_configuration(self, from_data: Dict[str, str], from_keys: Tuple[str, ...]):
        self.serial_numbers = self._transfer_from_configuration(from_data, tuple(self.serial_numbers.keys()), from_keys)

    @staticmethod
    def _transfer_from_configuration(serial_numbers, to_keys: Tuple[str, ...], from_keys: Tuple[str, ...]):
        serials = {to_key: serial_numbers[from_key] for to_key, from_key in zip(to_keys, from_keys)}
        return serials

    def persist_radio_button(self, state, state_to_member):
        for key, value in state_to_member.items():
            if state == key:
                self.__dict__[value] = "checked"
            else:
                self.__dict__[value] = ""


if __name__ == '__main__':
    from pprint import pprint

    data = DataRepository()

    serials_dict = {
        "serial_num_A": "9800001",
        "serial_num_B": "9800002",
        "serial_num_C": "9800003",
        "serial_num_D": "9800004",
        "serial_num_E": "9800005",
        "serial_num_F": "9800006"
    }

    new_serials = data._transfer_from_configuration(serials_dict,
                                                    tuple(data.serial_numbers.keys()),
                                                    ("serial_num_A", "serial_num_B", "serial_num_C",
                                                     "serial_num_D", "serial_num_E", "serial_num_F")
                                                    )

    pprint(new_serials)
