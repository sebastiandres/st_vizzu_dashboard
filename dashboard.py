import pandas as pd
import streamlit as st
from streamlit_vizzu import Config, Data, VizzuChart

###############################################################################
# Header of page
###############################################################################
st.set_page_config(layout="wide", page_title="Dashboard with streamlit and vizzu", page_icon="🧮")
c1, c2 = st.columns([3, 1])
c1.header("Editable dataframes and Vizzu charts")
c2.button("Useless button")
warning_placeholder = st.empty()

###############################################################################
# The editable dataframe
###############################################################################
c1, c2 = st.columns(2)

df = pd.read_csv("data/Hydra-Movie-Scrape.csv", sep=",", encoding="utf-8")
df.Year = df.Year.astype(str)
#st.write(df.head())

# First 2 graphs
c1, c2 = st.columns(2)
c1_data = Data()
c1_data.add_data_frame(df)
# Create the chart
chart = VizzuChart(key="c11")
# Add the first chart
chart.animate(c1_data)
chart.animate(
    Config({"x": "Year", "y": "Rating", "title": "Stars"}),
)
with c1:
    chart.show()

# Second chart
c1, c2 = st.columns(2)
c2_data = Data()
c2_data.add_data_frame(df)
# Create the chart
chart = VizzuChart(key="c22")
# Add the first chart
chart.animate(c2_data)
chart.animate(
    Config({"x": "Year", "y": "Runtime", "title": "Stars"}),
)
with c2:
    chart.show()
# Some other links
_, c1, c2, c3 = st.columns([1,2,2,2])
c1.caption("[streamlit-vizzu documentation](https://github.com/vizzu-streamlit/streamlit-vizzu/)")
c2.caption("[streamlit documentation](https://docs.streamlit.io/)")
c3.caption("[(ipy)vizzu documentation](https://ipyvizzu.vizzuhq.com/latest/)")
