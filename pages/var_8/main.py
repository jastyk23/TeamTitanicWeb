from pages.var_8.scripts.titanic import Titanic
import streamlit as st


def var8():
    data_path = 'src/data/data.csv'
    titanic = Titanic(path_name=data_path)

    class_dict = titanic.get_class()

    option = st.selectbox(
        "Выберите класс",
        ("1", "2", "3"))

    select = option if not option is None else '1'

    passengers = class_dict[option]

    data = {'Пол': ['male', 'female'],
            'Количество': [passengers['male'], passengers['female']]}

    st.bar_chart(data=data, x='Пол', y='Количество')
