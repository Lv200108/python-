from lstmpredicter import lstm_model
from keras.optimizers import Adam
from keras.models import load_model
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
plt.rcParams['axes.unicode_minus'] = False  # 负号显示


# 可视化训练过程
def show_train_history(train_history, value1, value2, ylable):
    plt.plot(train_history.history[value1], )
    plt.plot(train_history.history[value2], linewidth=1.0, linestyle='--')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title('Train History', fontsize=16)
    plt.ylabel(ylabel=ylable, fontsize=16)
    plt.xlabel('Epoch', fontsize=16)
    plt.legend([value1, value2], loc='best', fontsize=13.5)
    plt.tight_layout()
    plt.show()


def train_model():
    # 加载数据和模型
    X_train = np.load('train_data/X_train.npy')
    Y_train = np.load('train_data/Y_train.npy')
    X_val = np.load('train_data/X_val.npy')
    Y_val = np.load('train_data/Y_val.npy')
    model = lstm_model((24, 8))

    # 编译模型并训练
    model.compile(optimizer=Adam(lr=0.003), loss='mae')
    history = model.fit(X_train, Y_train, epochs=10, batch_size=128,
                        validation_data=(X_val, Y_val), verbose=2)
    model.save('lstm_model.h5')

    return history


if __name__ == '__main__':
    history = train_model()
    show_train_history(history, value1='loss', value2='val_loss', ylable='loss')
    # 预测PM2.5值并与真实PM2.5值对比
    X_val = np.load('train_data/X_val.npy')
    Y_val = np.load('train_data/Y_val.npy')
    model = load_model('lstm_model.h5')
    val_pred = model.predict(X_val)
    plt.plot(range(Y_val.shape[0]), Y_val[:, 0], label='PM2.5实际值')
    plt.plot(range(Y_val.shape[0]), val_pred[:, 0], linewidth=1.0, linestyle='--', label='PM2.5预测值')
    plt.legend(loc='best')
    plt.show()
