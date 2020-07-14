"""
>>> import sensordata
>>> sdg = sensordata.SensorDataGenerator()
>>> sdg.generate_sensor_data([True], "13800", "LOW")
['13876.2', '119.88', '0.9000', 'Lagging', '1482.948', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', '6.1']

>>> sdg.generate_sensor_data([True], "13800", "NOMINAL")
['13800.0', '120.0', '0.9000', 'Lagging', '1490.40', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', '21.7']

>>> sdg.generate_sensor_data([True], "13800", "HIGH")
['13813.8', '120.12', '0.9000', 'Lagging', '1497.852', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', '69.0']

>>> sdg.generate_sensor_data([False], "13800", "LOW")
['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']

>>> sdg.generate_sensor_data([False], "13800", "NOMINAL")
['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']

>>> sdg.generate_sensor_data([False], "13800", "HIGH")
['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']

>>> sdg.generate_sensor_data([True], "7200", "LOW")
['7192.8', '59.94', '0.9000', 'Lagging', '386.856', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', '6.1']

>>> sdg.generate_sensor_data([True], "7200", "NOMINAL")
['7200.0', '60.0', '0.9000', 'Lagging', '388.80', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', '21.7']

>>> sdg.generate_sensor_data([True], "7200", "HIGH")
['7207.2', '60.06', '0.9000', 'Lagging', '390.744', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', '69.0']

>>> sdg.generate_sensor_data([False], "7200", "LOW")
['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']

>>> sdg.generate_sensor_data([False], "7200", "NOMINAL")
['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']

>>> sdg.generate_sensor_data([False], "7200", "HIGH")
['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']

>>> sdg.generate_sensor_data([False, False, False, False, False, False], "7200", "NOMINAL")
['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', \
'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', \
'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', \
'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', \
'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', \
'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']

>>> sdg.generate_sensor_data([True, True, True, True, True, True], "13800", "LOW")
['13876.2', '13876.2', '13876.2', '13876.2', '13876.2', '13876.2', \
'119.88', '119.88', '119.88', '119.88', '119.88', '119.88', \
'0.9000', '0.9000', '0.9000', '0.9000', '0.9000', '0.9000', \
'Lagging', 'Lagging', 'Lagging', 'Lagging', 'Lagging', 'Lagging', \
'1482.948', '1482.948', '1482.948', '1482.948', '1482.948', '1482.948', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', 'FILLER', \
'6.1', '6.1', '6.1', '6.1', '6.1', '6.1']


--- Test link combinations ---V:

Six sensors on the line and linked
>>> sensordata.SensorDataGenerator.sensor_link_status(
...     ["9800001", "9800002", "9800003", "9800004", "9800005", "9800006"],
...     ["-50", "-55", "-60", "-65", "-70", "-75"]
... )
[True, True, True, True, True, True]

Six sensors on the line, but some not linked as indicated by an rssi of "0"
>>> sensordata.SensorDataGenerator.sensor_link_status(
...     ["9800001", "9800002", "9800003", "9800004", "9800005", "9800006"],
...     rssi_values=["-50", "0", "-60", "0", "-70", "0"]
... )
[True, False, True, False, True, False]

Three sensors on the line and linked
>>> sensordata.SensorDataGenerator.sensor_link_status(
...     ["9800001", "9800002", "9800003"],
...     ["-50", "-55", "-60"]
... )
[True, True, True]

Three sensors on the line, but none linked
>>> sensordata.SensorDataGenerator.sensor_link_status(
...     ["9800001", "9800002", "9800003"],
...     ["0", "0", "0"]
... )
[False, False, False]

"""
