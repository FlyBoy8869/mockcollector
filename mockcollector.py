import os
import time
from pprint import pprint
from typing import List, Tuple

from flask import Flask, render_template, request, url_for, redirect

from data import DataRepository
from modemstatusdata import ModemStatusDataGenerator
from rawconfig import RawConfigDataGenerator
from sensordata import SensorDataGenerator

app = Flask(__name__)
data = DataRepository()

print(f"secret_key: {os.environ.get('FLASK_SECRET_KEY')}")


def _append_link(links: List[Tuple[str, str]], label: str, url: str):
    links.append((label, url))
    return links


def _make_link_list(pages: List[str]):
    links: List[Tuple[str, str], ...] = []

    for page in pages:
        _append_link(links, page, url_for(page))
    return links


def login_needed():
    return data.advanced_config_login != ""


@app.route('/', methods=['GET', 'POST'])
def index():
    pages = [
        "settings", "configuration", "modem_status", "raw_config", "temperature_scale", "sensor_data",
        "software_upgrade"
    ]

    return render_template("index.html", links=_make_link_list(pages))


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if request.method == 'POST':
        pprint(request.form)
        data.transfer_from_settings(request)
    
    return render_template('settings.html',
                           data=data,
                           serial_numbers=data.serial_numbers,
                           rssi_values=data.rssi_values)


@app.route('/configuration', methods=['GET', 'POST'])
def configuration():
    if request.method == 'POST':
        pprint(request.form)
        data.transfer_from_configuration(request, ("serial_num_A", "serial_num_B", "serial_num_C",
                                                   "serial_num_D", "serial_num_E", "serial_num_F"))
        time.sleep(5)

    return render_template('configuration.html', serial_numbers=data.serial_numbers)


modem_data = ModemStatusDataGenerator()


@app.route('/modemstatus')
def modem_status():
    return render_template('modem_status.html', config=modem_data.generate_data(data.serial_numbers, data.rssi_values))


@app.route('/softwareupgrade')
def software_upgrade():
    versions = ["0x75" if rssi != "0" else "0x00" for rssi in data.rssi_values.values()]
    print(versions)
    return render_template('software_upgrade.html', versions=versions)


sensor_data_generator = SensorDataGenerator()


@app.route('/sensordata')
def sensor_data():
    readings = sensor_data_generator.generate_sensor_data(
        sensor_data_generator.make_key_combinations(data.serial_numbers, data.rssi_values),
        data.voltage,
        data.tolerance
    )
    return render_template("sensor_data.html", readings=readings)


@app.route('/temperaturescale', methods=['POST', 'GET'])
def temperature_scale():
    if login_needed():
        return redirect(url_for("settings"))

    return render_template("temperature_scale.html")


raw_config_data_generator = RawConfigDataGenerator()


@app.route('/rawconfig', methods=['POST', 'GET'])
def raw_config():
    if login_needed():
        return redirect(url_for("settings"))

    scale_current = raw_config_data_generator.generate_scale_current(data.raw_tolerance)
    scale_voltage = raw_config_data_generator.generate_scale_voltage(data.raw_tolerance)
    correction_angle = raw_config_data_generator.generate_correction_angle(data.raw_tolerance)

    return render_template("raw_config.html", scale_current=scale_current, scale_voltage=scale_voltage,
                           correction_angle=correction_angle)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
