from dataclasses import dataclass, field
from typing import Dict, Tuple


@dataclass
class DataRepository:
    collector_power: str = "OFF"
    collector_on_checked: str = ""
    collector_off_checked: str = "checked"

    off_status_code: str = "404"
    status_code_404: str = "checked"
    status_code_408: str = ""

    serial_update_delay: int = 5

    serial_numbers: Dict[str, str] = \
        field(default_factory=lambda: {
            "serial_1": "0",
            "serial_2": "0",
            "serial_3": "0",
            "serial_4": "0",
            "serial_5": "0",
            "serial_6": "0"
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
    logged_in: bool = False

    modem_status_ready: int = 0
    modem_status_pause: bool = False

    def transfer_from_settings(self, req):
        self.collector_power = req.form["collector_power"]
        self.persist_radio_button(self.collector_power,
                                  {
                                      "ON": "collector_on_checked",
                                      "OFF": "collector_off_checked"
                                  })

        if "off_status_code" in req.form.keys():
            self.off_status_code = req.form["off_status_code"]
            self.persist_radio_button(self.off_status_code,
                                      {
                                          "404": "status_code_404",
                                          "408": "status_code_408"
                                      })

        self.serial_update_delay = req.form["serial_update_delay"]

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

    def transfer_from_configuration(self, req, from_keys: Tuple[str, ...]):
        self._transfer_from_configuration(req, tuple(self.serial_numbers.keys()), from_keys)

    def _transfer_from_configuration(self, req, to_keys, from_keys):
        self.serial_numbers = {to_key: req.form[from_key] for to_key, from_key in zip(to_keys, from_keys)}

    def persist_radio_button(self, state, state_to_member):
        for key, value in state_to_member.items():
            if state == key:
                self.__dict__[value] = "checked"
            else:
                self.__dict__[value] = ""


data_repository = DataRepository()
