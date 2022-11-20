
import numpy
import matplotlib.pyplot
import scipy
import skimage

x = [85.5, 88.2, 90.2, 90.5, 91.5, 93.4, 94.4, 96.5, 98.5, 101.5, 102.0, 105.4, 105.6]
y = [0,    0.05, 0.14, 0.4,  1.0,  1.1,  1.72, 2.65, 3.01, 3.2,   3.3,   3.4,   3.42]

def f(t, a, b):
    return a + b*t
params, pcov = scipy.optimize.curve_fit(f, x, y)
print(params)
matplotlib.pyplot.figure()
matplotlib.pyplot.plot(x, y, "k.")
matplotlib.pyplot.plot(x, params[0] + params[1] * numpy.array(x))
matplotlib.pyplot.xlabel("Temperature [K]")
matplotlib.pyplot.ylabel("Resistance [mΩ]")
matplotlib.pyplot.show()

