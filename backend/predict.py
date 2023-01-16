import tensorflow as tf
import streamlit as st
from backend import member

# モデルを読み込む関数
# @st.casheで再読み込みにかかる時間を減らす。
@st.cache(allow_output_mutation=True)
def model_load():
    with tf.keras.utils.CustomObjectScope({'GlorotUniform':tf.keras.initializers.glorot_uniform()}):
        model50 = tf.keras.models.load_model('./50_fine4.h5')
        model10 = tf.keras.models.load_model('./10_fine1.h5')
    return model10,model50

# 顔画像が誰なのか予測値を上位3人まで返す関数
def predict_name(image):

    # モデルを読み込んで予測値を出す(予測値はラベルでなく確率で出力される）
    model10,model50 = model_load()
    pred_value10 = model10.predict(image)
    pred_value50 = model50.predict(image)

    sum_pred_value10 = 0
    sum_pred_value50 = 0
    for index in range(100):
        sum_pred_value10 += pred_value10[index][:]
        sum_pred_value50 += pred_value50[index][:]


    result10_ja = []
    result10_en = []
    result50_ja = []
    result50_en = []
    top = 3
    max_index10 = sum_pred_value10.argsort()[::-1][:top]
    max_index50 = sum_pred_value50.argsort()[::-1][:top]
    for i in range(top):
        result10_ja.append([member.member_ja(max_index10[i],max_index10[i]+1)[0],round(sum_pred_value10[max_index10[i]],1)])
        result10_en.append([member.member_en(max_index10[i],max_index10[i]+1)[0],round(sum_pred_value10[max_index10[i]],1)])
        result50_ja.append([member.member_ja(max_index50[i],max_index50[i]+1)[0],round(sum_pred_value50[max_index50[i]],1)])
        result50_en.append([member.member_en(max_index50[i],max_index50[i]+1)[0],round(sum_pred_value50[max_index50[i]],1)])
    return result10_ja,result50_ja,result10_en,result50_en