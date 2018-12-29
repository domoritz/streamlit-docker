import altair as alt
import streamlit as st
from vega_datasets import data

st.title("Streamlit with Altair")

cars = data.cars()

chart = alt.Chart(cars).mark_point().encode(
    x="Horsepower",
    y="Miles_per_Gallon",
    color="Origin",
).interactive()

with alt.data_transformers.enable(consolidate_datasets=False):
    chart_dict = chart.to_dict()
    chart_dict.pop("data", None)

    st.write(chart_dict)

    st.vega_lite_chart(cars, chart_dict)
