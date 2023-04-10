import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Favourites')
streamlit.text(' 🥣 omega 3 & Blueberry oatmeal')
streamlit.text(' 🐔 boiled eggs')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
