import pandas as pd
import jieba
import csv
import re
from gensim.models import word2vec
import gensim
import logging
path = "C:\\Users\\Administrator\\train.txt"
def cut_txt(cut_file):
    try:
        math = 0
        f2 = open("C:\\Users\\Administrator\\cut_file.txt", 'w', encoding='utf-8')
        for word in open(path, 'r', encoding='utf-8'):

            words = word.split("	")[0]
            # 精确模式
            seg_list = jieba.cut(words, cut_all=True)
            jieba_data = " ".join(seg_list)
            print(jieba_data)
            math = math+1
            # with open("C:\\Users\\Administrator\\cut_file.txt", 'w') as f2:

            f2.writelines(jieba_data)
            f2.write('\n')
        print(math)
        f2.close()
    except BaseException as e:  # 因BaseException是所有错误的基类，用它可以获得所有错误类型
        print(Exception, ":", e)    # 追踪错误详细信息

# cut_txt(path)

save_model_file = "C:\\Users\\Administrator\\ci_data.txt"
def model_train( save_model_file):  # model_file_name为训练语料的路径,save_model为保存模型名
    # sentences = "C:\\Users\\Administrator\\cut_file.txt"
    # 模型训练，生成词向量
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # model = gensim.models.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5

    sentences = word2vec.LineSentence("C:\\Users\\Administrator\\cut_file.txt")
    model = word2vec.Word2Vec(sentences, hs=1, min_count=1, window=3, size=100)
    # model.save_word2vec_format("C:\\Users\\Administrator\\ci_data.txt",binary=False)
    model.wv.save_word2vec_format("C:\\Users\\Administrator\\data_ci.bin",binary=True)

# model_train(save_model_file)
model =gensim.models.KeyedVectors.load_word2vec_format("C:\\Users\\Administrator\\data_ci.bin",binary = True)
# 计算两个词的相似度/相关程度

print(model.most_similar('珠宝',topn=5))
# y1 = model.similarity("腾讯",topn=10)

# for item in y1:
#     print(item[0], item[1])
# print("-------------------------------\n")
