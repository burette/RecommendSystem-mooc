train_file=$1
item_vec_file=$2
../bin/word2vec/word2vec -train $train_file -output $item_vec_file -size 128 -window 5 -sample 1e-3 -negative 5 -hs 0 -binary 0 -cbow 0 -iter 100


# 参数详解：
# -train 训练数据
# -output 结果输入文件，即每个词的向量
# -cbow 是否使用cbow模型，0表示使用skip-gram模型，1表示使用cbow模型，默认情况下是skip-gram模型，cbow模型快一些，skip-gram模型效果好一些
# -size 表示输出的词向量维数
# -window 为训练的窗口大小，8表示每个词考虑前8个词与后8个词（实际代码中还有一个随机选窗口的过程，窗口大小<=5)
# -negative 表示是否使用NEG方，0表示不使用，其它的值目前还不是很清楚
# -hs 是否使用HS方法，0表示不使用，1表示使用
# -sample 表示 采样的阈值，如果一个词在训练样本中出现的频率越大，那么就越会被采样
# -binary 表示输出的结果文件是否采用二进制存储，0表示不使用（即普通的文本存储，可以打开查看），1表示使用，即vectors.bin的存储类型
# -alpha 表示 学习速率
# -min-count 表示设置最低频率，默认为5，如果一个词语在文档中出现的次数小于该阈值，那么该词就会被舍弃
# -classes 表示词聚类簇的个数，从相关源码中可以得出该聚类是采用k-means