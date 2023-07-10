import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

# create a repeatable code block called function
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# new section to display fruity vice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  # Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information")
  else:
    back_from_fuction =  get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_fuction)
except URLError as e:
  streamlit.error()

# dont run anything past here while we troubleshoot
#streamlit.stop()

streamlit.header("The Fruit Load list contains")
#snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
        return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

# Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding', add_my_fruit)

# This will not work correctly but just go with in for now
streamlit.write("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')");
