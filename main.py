import streamlit as st
from pages import var1, var8, var15, var16

st.title('Данные пассажиров Титаника')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["О проекте", "Вариант 1", "Вариант 8", "Вариант 15", "Вариант 16"])

with tab1:
    st.header("О титанике")
    st.image('src/img/titanic.jpg')
    with open('src/docs/Titanic_info.MD') as file:
        test = file.read()
        file.close()
    st.markdown(test)
with tab2:
    var1()

with tab3:
    var8()

with tab4:
    var15()

with tab5:
    var16()
