import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
print("start")
xs = [1, 5, 10, 20, 30, 50, 100]
y1 = [150000, 100000, 50000, 30000, 20000, 10000, 6000]
y2 = [40000, 30000, 20000, 10000, 6000, 4000, 2000]

plt.plot(xs, y1, 'go', label="C")
plt.plot(xs, y2, 'mo', label="D")
plt.title("行业收入情况")
plt.xlabel("行业内排名百分比（越小代表越靠前）")
plt.ylabel("收入")
plt.xticks(np.arange(0, 110, 10))
plt.yticks(np.arange(0, 160000, 10000))
plt.legend()
plt.show()
