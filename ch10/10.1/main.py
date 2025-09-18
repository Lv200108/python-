import facecollecter
import facerecognizer
import facerecognition
import os

if __name__ == '__main__':
    command = 0
    while True:
        print(
            '''
            --------人脸检测系统---------
            
                输入1  增加新的人脸
                输入2   人脸检测       
            '''
        )
        if command != 0:
            if command == 1:
                print('新增人脸成功!\n')
        command = int(input('请输入数字>>>'))

        if command == 1:
            facecollecter.collect_face_data()
            facerecognizer.train_recognizer()

        if command == 2:
            facerecognition.recognise_face()
        os.system('cls')
