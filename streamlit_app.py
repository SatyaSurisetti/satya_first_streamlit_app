import streamlit
#import pandas
#import requests
import snowflake.connector
from URrllib.error import URLError

# dont run anything past here while we troubleshoot
streamlit.stop()

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

# Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
# Below function calls a pandas function to show the json file in a normalized form. 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# This funciton below puts the data into a datframe.
streamlit.dataframe(fruityvice_normalized)

# Querying our trial account metadata
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load list contains")
streamlit.dataframe(my_data_rows)

# Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding', add_my_fruit)

# This will not work correctly but just go with in for now
streamlit.write("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')");
