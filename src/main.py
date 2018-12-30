import altair as alt
import streamlit as st
from vega_datasets import data

st.title("Streamlit with Altair")

cars = data.cars()
iris = data.iris()

cars_scatter = alt.Chart(cars).mark_point().encode(
    x="Horsepower",
    y="Miles_per_Gallon",
    color="Origin",
)

iris_scatter = alt.Chart(iris).mark_circle().encode(
    alt.X('sepalLength', scale=alt.Scale(zero=False)),
    alt.Y('sepalWidth', scale=alt.Scale(zero=False)),
    color='species'
)

chart = cars_scatter | iris_scatter

def id_transform(data):
    """ Altair data transformer that returns a fake named dataset with the object id. """
    return {
        "name": str(id(data))
    }

# register the id transformer
alt.data_transformers.register("id", id_transform)

with alt.data_transformers.enable("id"):
    chart_dict = chart.to_dict()

    st.json(chart_dict)

    data = {
        id(cars): cars,
        id(iris): iris
    }

    st.vega_lite_chart(data, chart_dict)
