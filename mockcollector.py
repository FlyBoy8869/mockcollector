import os
import time
from pprint import pprint
from typing import List, Tuple

from flask import Flask, render_template, request, url_for, redirect, Response

from data import data_repository
from modemstatusdata import ModemStatusDataGenerator
from rawconfig import RawConfigDataGenerator
from sensordata import SensorDataGenerator

app = Flask(__name__)
data = data_repository

print(f"secret_key: {os.environ.get('FLASK_SECRET_KEY')}")


def _append_link(links: List[Tuple[str, str]], label: str, url: str):
    links.append((label, url))
    return links


def _make_link_list(pages: List[str]):
    links: List[Tuple[str, str]] = []

    for page in pages:
        _append_link(links, page, url_for(page))
    return links


def login_needed():
    return data.advanced_config_login != "" and not data.logged_in


@app.route('/', methods=['GET', 'POST'])
def index():
    pages = [
        "settings", "configuration", "modem_status", "raw_config", "temperature_scale", "sensor_data",
        "software_upgrade", "voltage_ride_through", "fault_current"
    ]

    return render_template("index.html", links=_make_link_list(pages))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data.logged_in = True

    return render_template("login.html")


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if request.method == 'POST':
        print("data sent from settings page in 'POST' request.")
        pprint(request.form)
        data.transfer_from_settings(request)
    
    return render_template('settings.html',
                           data=data,
                           serial_numbers=data.serial_numbers,
                           rssi_values=data.rssi_values)


@app.route('/configuration', methods=['GET', 'POST'])
def configuration():
    if request.method == 'POST':
        print("data sent from configuration page")
        pprint(request.form)
        data.transfer_from_configuration(
            request,
            ("serial_num_A", "serial_num_B", "serial_num_C",
             "serial_num_D", "serial_num_E", "serial_num_F")
        )

    if data.collector_power == "ON":
        if not data.modem_status_pause:
            data.modem_status_pause = True
            data.modem_status_ready = time.time() + int(data.serial_update_delay)

        return render_template('configuration.html', serial_numbers=data.serial_numbers)
    else:
        return Response(status=data.off_status_code)


modem_data = ModemStatusDataGenerator()


@app.route('/modemstatus')
def modem_status():
    if data.collector_power == "ON" and not data.modem_status_pause:
        return render_template('modem_status.html',
                               config=modem_data.generate_data(data.serial_numbers, data.rssi_values)
                               )
    elif time.time() >= data.modem_status_ready:
        data.modem_status_pause = False
        data.modem_status_ready = 0

    return render_template('modem_status.html', config=modem_data.generate_blank_page())


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
        return redirect(url_for("login"))

    return render_template("temperature_scale.html")


raw_config_data_generator = RawConfigDataGenerator()


@app.route('/rawconfig', methods=['POST', 'GET'])
def raw_config():
    if data.collector_power == "ON":

        if login_needed():
            return redirect(url_for("login"))

        scale_current = raw_config_data_generator.generate_scale_current(data.raw_tolerance)
        scale_voltage = raw_config_data_generator.generate_scale_voltage(data.raw_tolerance)
        correction_angle = raw_config_data_generator.generate_correction_angle(data.raw_tolerance)

        return render_template("raw_config.html", scale_current=scale_current, scale_voltage=scale_voltage,
                               correction_angle=correction_angle)
    else:
        return Response(status=0)


@app.route('/voltageridethrough', methods=['POST', 'GET'])
def voltage_ride_through():
    vrt: float = 0.0000000
    if request.method == "POST":
        vrt = request.form["CollectorCalibration"]
    return render_template("voltage_ride_through.html", vrt=vrt)


@app.route('/faultcurrent')
def fault_current():
    return render_template("fault_current.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=bool(os.environ.get("FLASK_DEBUG", False)))
