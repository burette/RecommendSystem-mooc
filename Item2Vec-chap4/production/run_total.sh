# 串联所有过程的脚本:
# 1.从训练文件中得到训练数据文件
# 2.通过word2vec从训练数据文件中得到训练数据的向量表示
# 3.从向量表示文件中计算得到制定itemid的相似item列表，保存到item_sim_file

python="/usr/local/bin/python3.7"
user_rating_file="../data/ratings_1000000.csv"
train_file="../data/train_data_bk.txt"
item_vec_file="../data/item_vec_bk.txt"
item_sim_file="../data/sim_result_bk.txt"
if [ -f $user_rating_file ]; then
    $python produce_train_data.py $user_rating_file $train_file
else :
  echo "no rating file"
  exit

fi
if [ -f $train_file ]; then
    sh train.sh $train_file $item_vec_file
else
  echo "no train data file"
  exit
fi
if [ -f $item_vec_file ]; then
    $python produce_item_sim.py $item_vec_file $item_sim_file
else
  echo "no item vec file"
  exit
fi