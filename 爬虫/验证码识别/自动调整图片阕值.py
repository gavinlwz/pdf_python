import numpy as np
import pytesseract
from PIL import Image
from pytesseract import Output
import numpy


def clear(imgUrl, threshold):
    '''
    调整图片灰度，亮度，对比度，剪切，旋转
    '''
    image = Image.open(imgUrl)
    image = image.point(lambda x: 0 if x < threshold else 255)  # 调整阕值为143正常为128 上线为255 image.point提高渐变色
    return image


def getConfidence(image):
    '''
    获取置信率
    '''
    data = pytesseract.image_to_data(image, output_type=Output.DICT)
    text = data['text']
    conf = data['conf']
    confidence = []
    numChar = []
    # print(text)
    for i in range(len(text)):
        if float(conf[i]) > -1:
            confidence.append(float(conf[i]))
            numChar.append(len(text[i]))

    print(confidence, numChar)
    return np.average(confidence, weights=numChar), sum(numChar)


if __name__ == '__main__':
    start = 1
    end = 255
    stop = 1
    for threshold in range(start, end, stop):
        img = clear("text.png", threshold)
        score = getConfidence(img)
        print("阕值是" + str(threshold) + ",置信度是" + str(score[0]) + ",字符总数是" + str(score[1]))
        print(score[0] * score[1])
