import streamlit as st
from PIL import Image
import pandas as pd
from backend import member

favicon = Image.open("名大.png")
st.set_page_config(
     page_title="日本産広葉樹判別アプリ",
     page_icon=favicon,
 )

st.title('木検索アプリ')
member50_ja = member.member_ja(0,50)
member50_en = member.member_en(0,50)
member10_ja = member.member10_ja(0,10)
member10_en = member.member10_en(0,10)

df_member50 = pd.DataFrame([member50_ja, member50_en], index=['樹種','scientific name'])
df_member10 = pd.DataFrame([member10_ja,member10_en], index=['樹種','scientific name'])
df_member50 = df_member50.T
df_member10 = df_member10.T



tab1, tab2 = st.tabs(["50種一覧 species list","10種一覧 species list"])

with tab1:
   st.header("50種一覧\n**50 species list**")
   st.write(df_member50)
   
with tab2:
   st.header("10種一覧\n**10 species list**")
   st.write(df_member10)


st.header('TWTwNo一覧')

df_10_differ = pd.read_csv("./TWTwNo/TWTwNo_50.csv")
df_10_same = pd.read_csv("./TWTwNo/TWTwNo_10_different.csv")
df_50 = pd.read_csv("./TWTwNo/TWTwNo_10_same.csv")

col3, col4, col5 = st.columns(3)

tab3, tab4, tab5 = st.tabs(["50種 50 species", "10種 4型 10 species 4types", "10種 1型 10 species 1type"])

with tab3:
   st.header("50種\n**50 species**")
   st.write(df_50)
   

with tab4:
   st.header("10種 4型\n**10 species 4types**")
   st.write(df_10_same)

with tab5:
   st.header("10種 1型\n**10 species 1type**")
   st.write(df_10_differ)