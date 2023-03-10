import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=5 * 1000)


df = pd.read_csv("data.csv").drop(columns=["Dead"])

classes = sorted(df.Class.unique())
chosen_class = st.selectbox(label = 'Choose class', options=["All classes", *classes ])
top_five = st.checkbox(label="Top 5")

def prepare_top_five(top_five_label):
    if top_five_label==True:
        return 5
    else:
        return None

def read_data(df, chosen_class):
    if chosen_class == "All classes":
        count = df.shape[0]
        
        return st.dataframe(df.sort_values(by=["Rank"], ascending=True).\
            head(prepare_top_five(top_five)).reset_index(drop=True), width = 700), st.subheader(f"Total people: {count}")
    else:
        return st.dataframe(df[df.Class==chosen_class].\
            sort_values(by="Level", ascending=False).\
            reset_index(drop=True).\
            head(prepare_top_five(top_five)), width = 700), None
            

read_data(df, chosen_class)
