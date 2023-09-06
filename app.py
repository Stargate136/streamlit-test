import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def show_graphs(df):
    st.header("DataFrame")
    st.dataframe(df)
    st.subheader("Heatmap de corrélation")
    ax_heatmap = sns.heatmap(df.select_dtypes(include="number").corr(), annot=True)
    st.pyplot(ax_heatmap.get_figure())
    st.subheader("Histogrammes de distribution")
    
    n = len(df.columns)
    fig_dist, axes = plt.subplots(n, 1, figsize=(5, 4*n))

    for idx, col in enumerate(df.columns):
        df[col].hist(ax=axes[idx])
        axes[idx].set_title(col)

    st.pyplot(fig_dist)
        

def main():
    st.title('Bonjour, bienvenu sur ma première application Streamlit')
    st.write("Je suis ravi de découvrir les posibilités de streamlit!")

    link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

    df = pd.read_csv(link)
    

    
    show_filtered = False
	
    filter = "Pas de filtre"

    st.header("Filtres")
    btn_cols = st.columns(4)
    if btn_cols[0].button("Pas de filtre"):
        show_filtered = False
        filter = "Pas de filtre"
    if btn_cols[1].button("US") :
        df_filtered = df[df["continent"] == " US."]
        show_filtered = True
        filter = "US"
    if btn_cols[2].button("Europe") :
        df_filtered = df[df["continent"] == " Europe."]
        show_filtered = True
        filter = "Europe"
    if btn_cols[3].button("Japan") :
        df_filtered = df[df["continent"] == " Japan."]
        show_filtered = True
        filter = "Japan"
        
    st.header(f"Analyse avec le filtre '{filter}'")
    
    if show_filtered:
        show_graphs(df_filtered)
    else:
         show_graphs(df)
         

if __name__ == "__main__":
	main()