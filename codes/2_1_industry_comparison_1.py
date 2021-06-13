import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
print("start")
xs = [1, 5, 10, 20, 30, 50, 100]
y1 = [100000, 50000, 30000, 20000, 10000, 5000, 2000]
y2 = [60000, 50000, 40000, 30000, 20000, 10000, 5000]

plt.plot(xs, y1, 'ro', label="A")
# plt.plot(xs, y2, 'bo', label="B")
plt.title("行业收入情况")
plt.xlabel("行业内排名百分比（越小代表越靠前）")
plt.ylabel("收入")
plt.xticks(np.arange(0, 110, 10))
plt.yticks(np.arange(0, 110000, 10000))
plt.legend()
plt.show()
