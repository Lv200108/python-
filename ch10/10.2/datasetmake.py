import pandas as pd
import numpy as np
from dataprocess import load_data, encode_label

# 显示所有的列
pd.set_option('display.max_columns', None)


def make_dataset():
    # 导入数据
    data = load_data('PRSA_data_2010.1.1-2014.12.31.csv')

    # 对风向列进行编码，风向为第5列所以这里为4
    data = encode_label(data, 4)
    data.columns = ['pm2.5', 'DEWP', 'TEMP', 'PRES', 'cbwd', 'Iws', 'Is', 'Ir']

    # 将2014年12月31日的数据单独保存作为测试
    new_data = data[data.shape[0] - 24:]
    new_data.to_csv('new_data.csv', index=False)

    # 将其余数数据制作为神经网络训练样本
    X_data = data
    print(X_data.shape)
    Y_data = data[['pm2.5']]  # 提取pm2.5数据
    X = np.ones((X_data.shape[0] - 24, 24, X_data.shape[-1]))
    Y = np.ones((Y_data.shape[0] - 24, 1))
    rows = range(0, X_data.shape[0] - 24, 1)
    for i in rows:
        X[i, :, :] = X_data.iloc[i: i + 24]
        Y[i, :] = [Y_data.iloc[i + 24]]

    # 将80%样本作为训练集，20%样本作为测试集
    X_train = X[:int(X.shape[0] * 0.95)]
    print(X_train.shape)
    Y_train = Y[:int(X.shape[0] * 0.95)]
    np.save('train_data/X_train.npy', X_train)
    np.save('train_data/Y_train.npy', Y_train)
    X_val = X[int(X.shape[0] * 0.95):]
    Y_val = Y[int(X.shape[0] * 0.95):]
    np.save('train_data/X_val.npy', X_val)
    np.save('train_data/Y_val.npy', Y_val)


if __name__ == '__main__':
    make_dataset()
