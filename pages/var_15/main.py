import streamlit as st
import matplotlib.pyplot as plt


def man_survived(file):
    survived_passengers = {
        'class_1': {},
        'class_2': {},
        'class_3': {},
    }
    lib = {
        '1': 'class_1',
        '2': 'class_2',
        '3': 'class_3',
    }
    for line in file:
        data = line.split(',')
        if data[1] == 'Survived' or data[1] == '0' or data[5] == 'female':
            continue
        else:
            if data[6] == '':
                age = '0'
            else:
                age = data[6]
            class_num = data[2]
            if age not in survived_passengers[lib[class_num]]:
                survived_passengers[lib[class_num]][age] = 1
            else:
                survived_passengers[lib[class_num]][age] += 1
    return survived_passengers


def select_ages(passengers, selected_ages):
    selected_passengers = {
        'class_1': 0,
        'class_2': 0,
        'class_3': 0,
    }
    for n_class in passengers:
        for age in passengers[n_class]:
            if selected_ages[0] <= float(age) <= selected_ages[1]:
                selected_passengers[n_class] += passengers[n_class][age]
    return [selected_passengers['class_1'], selected_passengers['class_2'], selected_passengers['class_3']]


def var15():
    st.info('Количество выживших мужчин по каждому классу обслуживания в заданном возростном диапазоне.')
    with open('src/data/data.csv') as file:
        mans_survived = man_survived(file)
    clas = ['Класс 1', 'Класс 2', 'Класс 3']
    selected = st.slider("Возраст пассажиров", 0, 100, (0, 100))
    passenger = select_ages(mans_survived, selected)
    data = {'Класс обслуживание': ['I Класс', 'II Класс', 'III Класс'], 'Число выживших': [i for i in passenger]}
    st.dataframe(data, use_container_width=True)
    fig = plt.figure(figsize=(7, 5))
    plt.bar(clas, passenger)
    for i in range(len(clas)):
        plt.text(i, passenger[i], str(passenger[i]), ha='center')
    plt.xlabel('Класс обслуживания')
    plt.ylabel('Число выживших')
    plt.title('Диаграмма - количество выживших мужчин')
    st.pyplot(fig)
