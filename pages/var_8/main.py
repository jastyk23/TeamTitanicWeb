from pages.var_8.scripts.titanic import Titanic
import streamlit as st


def var8():
    data_path = 'src/data/data.csv'
    titanic = Titanic(path_name=data_path)

    class_dict = titanic.get_class()

    st.header('Количество пассажиров каждого пола по указанному классу обслуживания')

    option = st.selectbox(
        "Выберите класс",
        ("1", "2", "3"))

    passengers = class_dict[option]

    data = {'Пол': ['Мужчины', 'Женщины'],
            'Количество': [passengers['male'], passengers['female']]}

    st.bar_chart(data=data, x='Пол', y='Количество')
