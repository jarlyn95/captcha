import os
import requests
import time


def download_captcha_image(data_root_path='captcha/train_data/rec',
                           stage='train',
                           amount=1000):
    """
    下载软考成绩查询验证码
    :param data_root_path: 图片呆保存目录
    :param stage: train、dev、test
    :param amount: 图片下载数量
    :return: 0——成功，-1——失败
    """
    if amount <= 0:
        return -1
    max_bits = len(str(amount - 1))  # 文件序号最大位数
    session = requests.session()

    dir_path = f'{data_root_path}/{stage}'
    os.makedirs(dir_path, exist_ok=True)
    sn_list = already_download_image_sn(dir_path) # 已存在的验证码序号

    for i in range(amount):
        bits = len(str(i))
        image_file_name = '{}/word_{}.jpg'
        image_file_name = image_file_name.format(dir_path, '0' * (max_bits - bits) + str(i))
        if i in sn_list:  # 防止重复下载
            print(image_file_name + ' already download!')
            continue
        else:
            print(image_file_name + ' need download')
            with open(image_file_name, 'wb') as f:
                f.write(session.get(f'https://query.ruankao.org.cn//score/captcha?{time.time() * 1000}').content)

    return 0


def already_download_image_sn(dirctory='captcha/train_data/rec/dev'):
    """

    :param dirctory: 文件夹目录
    :return: 已存在验证码序号
    """
    image_sn = []
    for filename in os.listdir(dirctory):
        try:
            text = filename[0:-4]
            text = text.split('_')
            image_sn.append(int(text[1]))
        except:
            print(filename)
    return image_sn


if __name__ == '__main__':
    download_captcha_image(stage='dev', amount=10)
    download_captcha_image(stage='test', amount=100)
    download_captcha_image(stage='train', amount=1000)
    download_captcha_image(stage='eval', amount=10)
