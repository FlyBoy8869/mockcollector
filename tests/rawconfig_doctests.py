"""
>>> import rawconfig
>>> rcg = rawconfig.RawConfigDataGenerator()

>>> rcg.get_scale_currents("NOMINAL", 6)
['0.02500', '0.02500', '0.02500', '0.02500', '0.02500', '0.02500']

>>> rcg.get_scale_currents("LOW", 6)
['0.02375', '0.02375', '0.02375', '0.02375', '0.02375', '0.02375']

>>> rcg.get_scale_currents("HIGH", 6)
['0.02625', '0.02625', '0.02625', '0.02625', '0.02625', '0.02625']

>>> rcg.get_scale_voltages("NOMINAL", 6)
['1.50000', '1.50000', '1.50000', '1.50000', '1.50000', '1.50000']

>>> rcg.get_scale_voltages("LOW", 6)
['1.20000', '1.20000', '1.20000', '1.20000', '1.20000', '1.20000']

>>> rcg.get_scale_voltages("HIGH", 6)
['1.80000', '1.80000', '1.80000', '1.80000', '1.80000', '1.80000']

>>> rcg.get_correction_angles("NOMINAL", 6)
['0.0', '0.0', '0.0', '0.0', '0.0', '0.0']

>>> rcg.get_correction_angles("LOW", 6)
['-45.0', '-45.0', '-45.0', '-45.0', '-45.0', '-45.0']

>>> rcg.get_correction_angles("HIGH", 6)
['45.0', '45.0', '45.0', '45.0', '45.0', '45.0']

"""
