
from matplotlib import widgets
import streamlit as st
import pandas as pd


import plotly.express as px

def get_metrics(df):
    average_lvl = df.Level.mean()
    min_lvl = df.Level.min()
    max_lvl = df.Level.max()
    return [average_lvl, min_lvl, max_lvl]


def draw_class_dist_all_classes_graph(df):
    new_df = df.Class.value_counts()
    
    fig = px.bar(new_df, x = new_df.index.values, y = new_df.values, text_auto = True)
    fig.update_layout(title = 'Сlass distribution', 
        xaxis_title = "Classes", 
        yaxis_title = 'Count', 
        width = 800, 
        height = 700, 
        titlefont=dict(size=40),
        )
    fig.update_xaxes(tickangle=280, tickfont=dict(size=15), titlefont=dict(size=25))
    fig.update_yaxes(titlefont=dict(size=25))
    
    st.plotly_chart(fig, theme="streamlit")

def draw_class_dist_all_classes_table(df):
    new_df = df.Class.value_counts().reset_index().rename(columns={"Class":"Total_count", "index":"Class_name"}).reset_index(drop=True)
    st.dataframe(new_df, width=400)


def draw_lvl_dist_all_classes_graph(df):

    new_df = df.Level.value_counts()
    fig = px.bar(new_df, x = new_df.index.values, y = new_df.values, text_auto = True)
    fig.update_layout(title = 'Lvl distribution', 
        xaxis_title = "Lvl", 
        yaxis_title = 'Count', 
        width = 800, 
        height = 700, 
        titlefont=dict(size=40),
        )
    fig.update_xaxes(tickangle=280, tickfont=dict(size=15), titlefont=dict(size=25))
    fig.update_yaxes(titlefont=dict(size=25))
    st.plotly_chart(fig, theme="streamlit")

def draw_lvl_dist_all_classes_table(df):
    new_df = df.Level.value_counts().reset_index().rename(columns={"index":"Lvl", "Level": "Total_count"}).sort_values(by="Lvl", ascending=False).reset_index(drop=True)
    st.dataframe(new_df, width=400)


def draw_metrics_data(df):
    metrics_data = get_metrics(df)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total character", df.shape[0])
    col2.metric("Average level is", round(metrics_data[0]))
    col3.metric("Min level is", metrics_data[1])
    col4.metric("Max level is", metrics_data[2])




data = st.file_uploader("Upload a data file", type=["csv"])



if data != None:
    df = pd.read_csv(data, sep=",").drop(columns="Dead")
    classes = sorted(df.Class.unique())
    
    selected_class = st.sidebar.selectbox("Choose class", options = ["All classes", *classes], index = 0)
    how_much = st.sidebar.number_input("How much to show in Overall window?", min_value = 1, max_value = df.shape[0], value = 5)


    if selected_class == "All classes":
        st.header("Overall")
        st.dataframe(df.head(how_much))        
        draw_metrics_data(df)
        
        st.header('Сlass distribution')
        tab1, tab2 = st.tabs(["Graph", "Table"])
        with tab1:
            draw_class_dist_all_classes_graph(df)
        with tab2:
            draw_class_dist_all_classes_table(df)
        
        st.header('Lvl distribution')
        tab1, tab2 = st.tabs(["Graph", "Table"])
        with tab1:
            draw_lvl_dist_all_classes_graph(df)
        with tab2:
            draw_lvl_dist_all_classes_table(df)


    else:
        new_df = df[df.Class==selected_class].sort_values(by="Rank")
        

        st.dataframe(new_df.head(how_much))

        draw_metrics_data(new_df)






