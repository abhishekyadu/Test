import streamlit as st

st.write("Testing import of matplotlib")

try:
    import matplotlib.pyplot as plt
    st.write("Matplotlib imported successfully")
except ImportError as e:
    st.error(f"Error importing matplotlib: {e}")
