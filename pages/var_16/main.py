import streamlit as st
import matplotlib.pyplot as plt


def count_survivors(file, price):
    first_class_survived = 0
    second_class_survived = 0
    third_class_survived = 0

    if type(file) is list:
        file = file[1:]
    else:
        next(file)
    for line in file:
        parts = line.strip().split(',')
        if not price[0] <= float(parts[10]) <= price[1]:
            continue
        if parts[5] == 'female' and parts[1] == '1':
            if parts[2] == '1':
                first_class_survived += 1
            elif parts[2] == '2':
                second_class_survived += 1
            elif parts[2] == '3':
                third_class_survived += 1
    return [first_class_survived, second_class_survived, third_class_survived]


def var16() -> None:
    """
        Ключевая функция, именно она отрисовывает вашу часть. Вы можете дополнительно создавать функции под ваши
        нужды и меня данный файл как вам удобно, НО все элементы streamlit для страницы должны быть внесены в эту
        функцию
        :return: None
        """
    data_path = 'src/data/data.csv'

    st.header('Данные пассажиров Титаника')
    st.write('Просмотр данных количества выживших женщин по каждому классу обслуживания, с диапазоном платы за проезд')
    price = st.slider('Диапазон платы за проезд в $ 1000', 0, 1000, (0, 1000))

    classes = ['Первый класс', 'Второй класс', 'Третий класс']
    with open(data_path) as file:
        survivors = count_survivors(file, price)
    fig, ax = plt.subplots()
    ax.bar(classes, survivors)
    ax.set_xlabel('Класс')
    ax.set_ylabel('Количество выживших женщин')
    ax.set_title('Количество выживших женщин по классам')

    st.pyplot(fig)
