import statistics
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


x = [0.0, 1.0, 2.0, 3.0, 4.0]
y = np.square(x)
y3 = np.power(x, 3)

def print_list():
    # Use a breakpoint in the code line below to debug your script.
    print(x)  # Press Ctrl+F8 to toggle the breakpoint.
    print('max: ', max(x))
    print('min: ', min(x))
    print('mean is: ', statistics.mean(x))
    print('sd is: ', statistics.stdev(x))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_list()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
