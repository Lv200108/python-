from keras import Sequential
from keras import Model
from keras.layers import Input, LSTM, Dense, BatchNormalization


def lstm_model(input_shape):
    model_input = Input(input_shape)
    bn = BatchNormalization()(model_input)
    lstm1 = LSTM(units=50, dropout=0.2, recurrent_dropout=0.2, return_sequences=True)(bn)
    lstm2 = LSTM(units=50, dropout=0.2, recurrent_dropout=0.2)(lstm1)
    dense = Dense(units=10, activation='relu')(lstm2)
    model_output = Dense(units=1)(dense)
    return Model(inputs=model_input, outputs=model_output)


if __name__ == '__main__':
    model = lstm_model((24, 8))
    model.summary()
