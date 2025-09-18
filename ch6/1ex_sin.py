import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y, label = 'y = sin(x)')  #绘制的图形
plt.title('Functional Image')  #图标题
plt.xlabel('x-axis')   #x轴标题 
plt.ylabel('y-axis')   #y轴标题
plt.legend()   #图例
plt.annotate('Minimum point', (-np.pi / 2, -1), (0, -0.75), 
             arrowprops = dict(arrowstyle = '->'))  #文字标注

plt.show() 

