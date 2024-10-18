import streamlit as st
st.write('Paris, le 18 octobre 2024')

st.markdown("### Happy birthday ")

if st.button(label="SuperButton") :

    st. balloons ()
    

st.markdown("#### Joyeux Noel ")
if  st.button("Click me"):
    st. snow()
    st.write("Button clicked!")

check = st.checkbox("Checkbox title", ["Add a constant", "Add beta 1", "Add beta 2"])
radio = st.radio("Vous voulez voter?", ["Yes", "No"])
txt = st.text_input("Votre vote")
txt_area = st.text_area("Votre ville")

if  st.button("Votre nom"):
    st.text_input("Votre nom")