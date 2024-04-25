import streamlit as st
import pandas as pd
from settings import Path

st.write('Hello World!')

df = pd.read_csv(Path)
st.write(df.head(5))
