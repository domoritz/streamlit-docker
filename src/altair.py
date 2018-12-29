import altair as alt
from vega_datasets import data
import streamlit as st

st.title("Streamlit with Altair")

cars = data.cars()

st.write(dir(alt))

# chart = alt.Chart(cars).mark_point().encode(
#     x='Horsepower',
#     y='Miles_per_Gallon',
#     color='Origin',
# )

# st.vega_lite_chart(cars, chart.to_json())
