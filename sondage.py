import streamlit as st
st.write ('Sondage de la semaine')

st.write('Paris, le 19 octobre 2024')

check = st.checkbox("Checkbox title", ["Add a constant", "Add beta 1", "Add beta 2"])
radio = st.radio("Voulez vous voter?", ["Yes", "No"])
txt = st.text_input("Votre cours prefere de la semaine")
slider = st.slider("Votre satisfactions des cours", 0, 100, 50)
txt_area = st.text_area("Vos suggestions")

if  st.button("Votre nom"):
    st.text_input("Votre nom")

st.markdown("### Bon weekend!!! ")

if st.button(label="SuperButton") :

    st. balloons ()
    

st.markdown("#### Ce n'est pas encore l'hiver ;)")
if  st.button("Click me"):
    st. snow()
    st.write("Button clicked!")

