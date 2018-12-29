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

def empty(data):
    """ Altair data transformer that returns an empty array. """
    return {
        "values": []
    }

# register the empty transformer
alt.data_transformers.register("empty", empty)

with alt.data_transformers.enable("empty"):
    chart_dict = chart.to_dict()
    chart_dict.pop("datasets", None)

    st.json(chart_dict)

    st.vega_lite_chart(cars, chart_dict)
