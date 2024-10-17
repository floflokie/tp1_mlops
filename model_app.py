import streamlit as st
from model_utils import load_model, make_prediction

model = load_model()
size = st.number_input("Size")
nb_rooms = st.number_input("Number of rooms")
garden = st.number_input("Garden")

if st.button("Predict"):
    result = make_prediction(size, nb_rooms, garden, model)
    st.write(result)
