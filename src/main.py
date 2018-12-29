import streamlit as st
import numpy as np
import time

st.title("My first Streamlit report")
st.write("Hello, world!")

st.header("Time for some data")
st.write("Here's a random dataset:")

df = np.random.randn(500, 3)
st.write(df)

st.write("And here's what it looks like:")
st.line_chart(df)

st.header("Showing progress")

import time

st.write("Starting a long computation...")

# Place some widgets on the page
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the widgets in each iteration.
    latest_iteration.text("Iteration %d" % i)
    bar.progress(i + 1)
    time.sleep(0.1)

st.write("...and now we're done!")
st.balloons()
