import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'première colonne': [1, 2, 3, 4],
     'deuxième colonne': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write(
    'Ci-dessous se trouve un DataFrame :', df,
    'Ci-dessus se trouve un DataFrame.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


# Example 6

markdown_text = """
# Heading
This is a paragraph of **bold** and *italic* text.
- Item 1
- Item 2
"""

st.markdown(markdown_text)