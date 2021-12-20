import io
import os
import time
import PIL.Image as Image
import numpy as np
import requests
from paddleocr import PaddleOCR
import argparse
import logging


def query_score(query_params: dict):
    """

    :param query_params: 查询参数字典， 例如：
    query_params = {'stage': '2021年下半年',
        'xm': 'xx', # 姓名
        'zjhm': 'xx', #身份证号
             }
    :return: 成绩查询结果
    """

    session = requests.session()
    url = 'https://query.ruankao.org.cn//score/result'
    tstmps = int(time.time() * 1000)
    content = session.get(f'https://query.ruankao.org.cn//score/captcha?{tstmps}').content
    image = Image.open(io.BytesIO(content))
    jym = parse_captcha(image)
    jym = jym[0][0]
    os.makedirs('tmp', exist_ok=True)
    image.save('tmp/word_' + str(tstmps) + '_' + jym + '.png')
    query_params['jym'] = int(jym)
    query_params['captcha'] = int(jym)
    query_params['select_type'] = 1
    time.sleep(3)
    # commit_ret = session.post('https://query.ruankao.org.cn//score/VerifyCaptcha', data=query_params)  # 提交验证码
    result = session.post(url, data=query_params).json()
    return result



def parse_captcha(img: Image):
    data = np.array(img)
    ocr = PaddleOCR(rec_model_dir='./captcha/inference/rec_num_best',
                    rec_char_dict_path='./captcha/arbic_number_dic.txt',
                    use_gpu=False,
                    rec_image_shape='3, 40, 220')  # need to run only once to load model into memory
    result = ocr.ocr(data, det=False, rec=True, cls=False)
    return result


def get_params():
    parser = argparse.ArgumentParser(description='不用验证码查询软考成绩')
    parser.add_argument('-y', "--year", type=str, help='考试时间', required=True)
    parser.add_argument('-n', "--name", type=str, help='姓名', required=True)
    parser.add_argument('-id', type=str, help='身份证号', required=True)
    args = parser.parse_args()
    parmas = args.__dict__
    return parmas


if __name__ == '__main__':

    parmas = get_params()
    data = {'stage': parmas.get('year'),
            'xm': parmas.get('name'),
            'zjhm': parmas.get('id'),
             }
    score = query_score(data)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info(score)
