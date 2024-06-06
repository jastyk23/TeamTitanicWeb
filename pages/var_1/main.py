import streamlit as st
import matplotlib.pyplot as plt


def get_ages(inner_file, stat, sex):
    inner_file = iter(inner_file)
    lst = []
    next(inner_file)
    for line in inner_file:
        line = line.split(',')
        if bool(int(line[1])) != stat or line[6] == '':
            continue
        if line[5] == sex:
            lst.append(float(line[6]))
    return lst


def var1() -> None:
    """
    Ключевая функция, именно она отрисовывает вашу часть. Вы можете дополнительно создавать функции под ваши
    нужды и меня данный файл как вам удобно, НО все элементы streamlit для страницы должны быть внесены в эту
    функцию.
    :return: None
    """
    data_path = 'src/data/data.csv'
    # Ваш код будет ниже
    # Создание сайта с изображением Титаника и диаграммой
    st.header('Диапазон возрастов спасенных пассажиров каждого пола')

    status = st.radio('Выберите статус пассажира:', ('Спасен', 'Погиб'))
    gender = st.radio('Выберите пол пассажира:', ('Мужчины', 'Женщины'))

    fig, ax = plt.subplots()
    my_dict = {
        'Мужчины': 'male',
        'Женщины': 'female',
    }

    with open(data_path, 'r') as file:
        if status == 'Спасен':
            passengers = get_ages(file, True, my_dict[gender])
            st.write(f'Минимальный возраст спасенных {gender.lower()[:-1]}: {min(passengers)}')
            st.write(f'Максимальный возраст спасенных {gender.lower()[:-1]}: {max(passengers)}')

        else:
            passengers = get_ages(file, False, my_dict[gender])
            st.write(f'Минимальный возраст погибших {gender.lower()[:-1]}: {min(passengers)}')
            st.write(f'Максимальный возраст погибших {gender.lower()[:-1]}: {max(passengers)}')

    # Создание диаграммы

    ax.hist(passengers, bins=10, alpha=0.5, label=gender)
    plt.xlabel('Возраст')
    plt.ylabel('Количество')
    plt.legend()
    st.pyplot(fig)
