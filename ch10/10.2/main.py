import os
from keras.models import load_model
import pandas as pd
import numpy as np
from datasetmake import make_dataset
from modeltrain import train_model

if __name__ == '__main__':
    command = 0
    flags = []
    while True:
        print(
            '''
            --------PM2.5预测系统---------

                输入1     初始化
                输入2   预测PM2.5
            '''
        )
        if flags:
            print('下一时刻PM2.5的值为：', flags)
        command = int(input('请输入数字>>>'))
        if command == 1:
            make_dataset()
            train_model()
        flags = []

        if command == 2:
            if os.path.exists(r'new_data.csv'):
                new_data = pd.read_csv(r'new_data.csv')
                print('读取数据成功')
            else:
                flags.append('no_new_data')

            if os.path.exists(r'lstm_model.h5'):
                lstm_model = load_model('lstm_model.h5')
                print('加载模型成功')
            else:
                flags.append('no_lstm_model')

            if flags:
                for flag in flags:
                    print(flag)
                print('需要初始化！')
            else:
                predict_value = lstm_model.predict(new_data.values.reshape(1,24,8))
                flags = predict_value[0][0]
        os.system('cls')
