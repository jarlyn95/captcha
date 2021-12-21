# 基于PaddleOCR训练模型识别数字验证码
可参考教程：https://blog.csdn.net/eton_liu/article/details/122021046


以[软考成绩查询](https://query.ruankao.org.cn/score/main)数字验证码为例，学习如何使用PaddleOCR库调优（fine-tune）模型。
学完本实战后，可以训练以下特定场景任务的OCR模型：
1. 字母+数字类型的图形验证码
2. 简单算术表达式（+、-、*、/）验证码
3. 手写数字识别
4. 邮编识别
5. 电话号码识别
6. 车牌号识别
7. 银行卡卡号识别
8. 身份证号识别
9. 任何类型OCR任务，只要训练数据集足够大

**1-8场景，数据标注任务相对较小，因为字符数量较少** 

**数据标注可以使用PaddleOCR自带的PPOCRLabel标注工具**