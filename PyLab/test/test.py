# from pylab import math
import pylab.math
from pylab import math as plmath
import numpy

from pylab.utils.Checker import Checker
print(pylab.math.add(1, 2))
print(plmath.sub(1, 2))
print(plmath.div(1, 2))

print(Checker.match_email("xxx@xxx.com"))
