import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
plt.rcParams['axes.unicode_minus'] = False  # 负号显示


# 读取数据，并将前4列合并为1列，指定第一列为索引
def load_data(filename):
    data = pd.read_csv(filename, parse_dates=[['year', 'month', 'day', 'hour']], index_col=0)
    # 删除序号no列，并修改内存中存储的数据
    data.drop('No', axis=1, inplace=True)
    # 对数据集中pm2.5浓度列中缺失值使用中位数填充
    data['pm2.5'].fillna(data['pm2.5'].median(), inplace=True)
    return data


# 将风向编码为适合训练的标签
def encode_label(data, index):
    encoder = LabelEncoder()
    values = pd.DataFrame(data).values
    # 对第index列数据制作标签
    values[:, index] = encoder.fit_transform(values[:, index])
    data = pd.DataFrame(values)
    return data


if __name__ == '__main__':
    # 导入数据
    data = load_data('PRSA_data_2010.1.1-2014.12.31.csv')
    # 对风向列进行编码，风向为第5列所以这里送入4
    data = encode_label(data, 4)
    # 可视化历史PM2.5值和气象因素
    col_names = ['pm2.5', 'DEWP', 'TEMP', 'PRES', 'cbwd', 'Iws', 'Is', 'Ir']
    display_list = [0, 1, 2, 3, 5, 6, 7]
    i = 1
    for index in display_list:
        plt.subplot(7, 1, i)
        plt.plot(data.values[:, index], label=col_names[index])
        plt.legend(loc='lower right')
        i = i + 1
    plt.show()
