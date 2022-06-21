import contextlib
import os
import time
from datetime import datetime
from pprint import pprint
from typing import List, Tuple

from flask import Flask, render_template, request, url_for, redirect, Response

import rawconfig
from data import data_repository
from modemstatusdata import ModemStatusDataGenerator
from sensordata import SensorDataGenerator

PORT = 6969

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
    # names of the functions below
    pages = [
        "settings", "configuration", "modem_status", "raw_config", "temperature_scale", "sensor_data",
        "software_upgrade", "voltage_ride_through", "fault_current", "date_and_time",
    ]

    return render_template("index.html", links=_make_link_list(pages), port=PORT)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data.logged_in = True

    return render_template("login.html", port=PORT)


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if request.method == 'POST':
        print("data sent from settings page in 'POST' request.")
        pprint(request.form)
        data.transfer_from_settings(request)
    
    return render_template(
        'settings.html',
        data=data,
        serial_numbers=data.serial_numbers,
        rssi_values=data.rssi_values,
        port=PORT
    )


date = "Mon May 22 09:00:30  2000"


@app.route('/date_and_time', methods=['GET', 'POST'])
def date_and_time():
    global date
    if data.collector_power == 'ON':
        if request.method == 'POST':
            if date_input := request.form['date']:
                with contextlib.suppress(ValueError):
                    date = datetime.fromisoformat(date_input).ctime()
        return render_template('date_and_time.html', collector_date_time=date, port=PORT)


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

    if data.collector_power != "ON":
        return Response(status=404)
    if not data.modem_status_pause:
        data.modem_status_pause = True
        data.modem_status_ready = time.time() + int(data.serial_update_delay)

    return render_template('configuration.html', serial_numbers=data.serial_numbers, port=PORT)


modem_data = ModemStatusDataGenerator()


@app.route('/modemstatus')
def modem_status():
    if data.collector_power == "ON" and not data.modem_status_pause:
        return render_template(
            'modem_status.html',
            config=modem_data.generate_data(data.serial_numbers, data.rssi_values, data.rssi_no_link),
            port=PORT
        )
    elif time.time() >= data.modem_status_ready:
        data.modem_status_pause = False
        data.modem_status_ready = 0

    return render_template('modem_status.html', config=modem_data.generate_blank_page(), port=PORT)


@app.route('/softwareupgrade', methods=['GET', 'POST'])
def software_upgrade():
    versions = ["0x75" if rssi != "0" else "0x00" for rssi in data.rssi_values.values()]
    # versions[2] = "0x00"

    if request.method == 'POST':
        return render_template('software_upgrade.html', versions=versions, port=PORT)

    print(versions)
    return render_template('software_upgrade.html', versions=versions, port=PORT)


sensor_data_generator = SensorDataGenerator()


@app.route('/sensordata')
def sensor_data():
    readings = sensor_data_generator.generate_sensor_data(
        sensor_data_generator.sensor_link_status(
            list(data.serial_numbers.values())[0: data.sensor_count],
            list(data.rssi_values.values())[0: data.sensor_count],
            list(data.rssi_no_link.values())[0: data.sensor_count]
        ),
        data.voltage,
        data.tolerance
    )
    if data.sensor_count > 3:
        return render_template("sensor_data.html", readings=readings, port=PORT)
    print(readings)
    return render_template("sensor_data_three_column.html", readings=readings, port=PORT)


@app.route('/temperaturescale', methods=['POST', 'GET'])
def temperature_scale():
    if login_needed():
        return redirect(url_for("login"))

    return render_template("temperature_scale.html", port=PORT)


@app.route('/rawconfig', methods=['POST', 'GET'])
def raw_config():
    if data.collector_power != "ON":
        return Response(status=0)
    if login_needed():
        return redirect(url_for("login"))

    count = 3 if len(data.serial_numbers) < 3 else 6
    scale_current = rawconfig.get_scale_currents(rawconfig.scale_current, data.raw_tolerance, count)
    scale_voltage = rawconfig.get_scale_voltages(rawconfig.scale_voltage, data.raw_tolerance, count)
    correction_angle = rawconfig.get_correction_angles(rawconfig.correction_angle, data.raw_tolerance, count)

    if data.sensor_count <= 3:
        return render_template(
            "raw_config_three_column.html",
            scale_current=scale_current,
            scale_voltage=scale_voltage,
            correction_angle=correction_angle,
            port=PORT
        )
    else:
        return render_template(
            "raw_config.html",
            scale_current=scale_current,
            scale_voltage=scale_voltage,
            correction_angle=correction_angle,
            port=PORT
        )


@app.route('/voltageridethrough', methods=['POST', 'GET'])
def voltage_ride_through():
    vrt: float = 0.0000000
    if request.method == "POST":
        vrt = request.form["CollectorCalibration"]
    return render_template("voltage_ride_through.html", vrt=vrt, port=PORT)


@app.route('/faultcurrent')
def fault_current():
    return render_template("fault_current.html", port=PORT)


@app.route('/calibrate', methods=['POST', 'GET'])
def calibrate():
    if login_needed():
        return redirect(url_for("login"))

    return render_template("calibrate.html", port=PORT)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", PORT))
    debug = bool(os.environ.get("FLASK_DEBUG", False))
    app.run(host='0.0.0.0', port=port, debug=debug)
