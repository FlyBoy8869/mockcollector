from data import data_repository


class ModemStatusDataGenerator:
    def __init__(self):
        self._suffix = "dB R	 0 LQI R	 -56 dB F	 3 LQI F"

    def generate_data(self, serial_numbers, rssi_values):
        sn_keys = ["serial_1", "serial_2", "serial_3", "serial_4", "serial_5", "serial_6"]
        rssi_keys = ["rssi_1", "rssi_2", "rssi_3", "rssi_4", "rssi_5", "rssi_6"]
        data_lines = []

        for sn_key, rssi_key in zip(sn_keys, rssi_keys):
            if serial_numbers[sn_key] == "0":
                continue
            if rssi_values[rssi_key] == "0":
                data_lines.append(self.generate_non_linked_line(serial_numbers[sn_key]))
            else:
                data_lines.append(self.generate_data_line(serial_numbers[sn_key], rssi_values[rssi_key]))

        return tuple(data_lines)

    @staticmethod
    def generate_blank_page():
        return tuple([""] * 6)

    @staticmethod
    def generate_serial_number_segment(serial_number):
        return "".join(serial_number+'\t') * 3

    @staticmethod
    def append_rssi(text, rssi_value):
        return text + rssi_value + " "

    @staticmethod
    def append_suffix(text, suffix):
        return text + suffix

    def generate_data_line(self, serial, rssi):
        return self.append_suffix(self.append_rssi(self.generate_serial_number_segment(serial), rssi), self._suffix)

    def generate_non_linked_line(self, serial):
        return serial + '\t' + "     -1" + '\t' + "     -1"
