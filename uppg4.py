
import numpy
import matplotlib.pyplot
import scipy

currents = numpy.array([0.20, 0.29, 0.39, 0.49, 0.60]) # current
voltages = numpy.array([5.98, 5.99, 5.99, 5.99, 6.02]) # mv

def voltage_to_temperature(mv):
    # linjär interpolering mellan 5.97 (88K) och 6.05 (86K)
    return 88 - (mv - 5.97)*2/0.08

temperatures = voltage_to_temperature(voltages)
x = currents
y = temperatures

def f(t, a, b):
    return a + b*t
params, pcov = scipy.optimize.curve_fit(f, x, y)
print(params)
matplotlib.pyplot.figure()
matplotlib.pyplot.plot(x, y, "k.")
matplotlib.pyplot.plot(x, params[0] + params[1] * x)
stderr = numpy.sqrt(numpy.diag(pcov))
print(stderr)
matplotlib.pyplot.ylabel("Critical temperature [K]")
matplotlib.pyplot.xlabel("Current [A]")
matplotlib.pyplot.show()