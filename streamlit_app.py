import streamlit
import pandas
import requests
streamlit.title (" This is my first python program on GitHub")
streamlit.header('Breakfast favourites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])


# new section to display fruity vice api response
#fruityvice_response = requests.get("Hai Satya what are you doing?")

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +Kiwi+")
#streamlit.text(fruityvice_response.json())
# Below function calls a pandas function to show the json file in a normalized form. 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# This funciton below puts the data into a datframe.
streamlit.dataframe(fruityvice_normalized)
