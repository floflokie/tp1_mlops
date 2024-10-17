import streamlit as st
import joblib


def load_model():
    model_loaded = joblib.load("regression.joblib")
    return model_loaded


model = load_model()
size = st.number_input("Size")
nb_rooms = st.number_input("Number of rooms")
garden = st.number_input("Garden")

if st.button("Predict"):
    result = model.predict([[size, nb_rooms, garden]])
    st.write(result)
