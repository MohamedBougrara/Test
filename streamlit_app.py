import streamlit as st

# st.header('st.button')

# if st.button('say hello'):
#      st.write('why hello?')
# if st.button('say goodbye'):
#      st.write('goodbye !!')
    
# if st.button('tu pars pas ?'):
#     st.write('Re-bienvenue')


import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('bonjour, bienvenue sur mon application Streamlit !')

# Example 1

st.write('Hello, *World!* ')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     "col1": [1, 2, 3, 4],
     "col2": [10, 20, 30, 40]
     })

# Example 4

st.write('Ci-dessous se trouve un DataFrame :', df, 'Ci-dessus se trouve un DataFrame.')

# Graphique à partir d'un dataframe

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
