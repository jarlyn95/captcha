import os


def format_data(input_dictory, label_file):
    with open(label_file, 'wb') as f:
        for filename in os.listdir(input_dictory):
            try:
                text = filename[0:-4]
                str_list = text.split('_')
                line = filename + '\t' + str_list[2] + '\n'
                f.write(line.encode('utf-8'))
            except:
                print(filename)


if __name__ == '__main__':
    format_data('captcha/train_data/rec/dev',
                'captcha/train_data/rec/rec_gt_dev.txt')
    format_data('captcha/train_data/rec/test',
                'captcha/train_data/rec/rec_gt_test.txt')
    format_data('captcha/train_data/rec/train',
                'captcha/train_data/rec/rec_gt_train.txt')
