#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
print(sys.version)


# In[10]:


import pandas as pd
import stremlit as st
import plotly.expprees as px


# In[11]:


#merged11.csvの読み込み
merged_df = pd.read_csv("merged11csv")


# In[ ]:


st.title("サロンサーチ")
price_limit = st.slider("最低カット価格の上限", min_value=2000,  max_value=8500, step200, value=5000)
score_limit = st.slider("人気スコアの下落”, min_value=0.0,     max_value=35.0, step=2.0, value=5.0)


# In[5]:


filtered_df = merged_df[
    (merged_df['price'] <= price_limit)&
    (merged_df['pop_score'] >= score_limit)
    ]


# In[6]:


fig = px.scatter(
    filtered_df,
    x='pop_score',
    y='prico',
    hover_data=['name_salon', 'sccess,'star', 'review'],       titie'人気カットと最低カットの散布図'
)
st.plotly_chart(fig)


# In[7]:


selected_salon = st.selectbox('気になるサロンを選んで詳細を確認', filtered_['name_salon'])

if selected_salon:
    url = filtered_df(filtered__df['name_salon'] == selected_salon]['link_datail'].values[0]
    st.markdown(f"[{selected_salon}のページへ移動]({url})",unsafe_allow_html=True)


# In[8]:


solt_key = st.selectbox(
    "ランキング基準を選んでください",
    ("star, "pop_score", "review , "price , "seats")
)
ascending = True if sort_kye == "price" else False


# In[9]:


st.subheader(f"{sort_key} によるサロンランキング （上位10件）")
ranking_df = filtered_df.solt_values(by=solt_kye, ascending=ascending).head(10)
st.dataframe(ranking_df[["name_salon", "price", "pop_score", "star, "review" "seats" "access"]]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




