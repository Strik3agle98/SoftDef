import matplotlib.pyplot as plt
import numpy as np

local = [0.0, 0.0010004, 0.0030279, 0.0050002, 0.0080528, 0.0100262, 0.0120381, 0.0130394, 0.0150279, 0.0160264, 0.0180371]
virtual_local =


if __name__ == "__main__":
    x = np.linspace(0, 50000, 11)
    plt.plot(x, [0,1,2,3,4,5,6,7,8,10,10], label='quadratic')
    plt.legend()
    plt.show()