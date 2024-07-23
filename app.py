import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

uri = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
data = pd.read_csv(uri)

st.write("Dados do dataframe de Flor Iris")
st.write(data)
setosa = data[data["species"] == "setosa"]
virginica = data[data["species"] == "virginica"]
versicolor = data[data["species"] == "versicolor"]

st.write("Grafico de dispersão das Iris")
fig, ax = plt.subplots()
ax.scatter(setosa["sepal_length"], setosa["sepal_width"], label="setosa")
ax.scatter(virginica["sepal_length"], virginica["sepal_width"], label="virginica")
ax.scatter(versicolor["sepal_length"], versicolor["sepal_width"], label="versicolor")
ax.set_xlabel("Comprimento da Sepala")
ax.set_ylabel("Largura da Sepala")
ax.legend()
st.pyplot(fig)




