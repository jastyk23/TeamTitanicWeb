import streamlit as st
from pages import var1, var8, var15, var16

st.title('Данные пассажиров Титаника')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["О проекте", "Вариант 1", "Вариант 8", "Вариант 15", "Вариант 16"])

with tab1:
    st.header("О титанике")
    st.image('src/img/titanic.jpg')
    st.markdown('''**«Тита́ник»** (англ. Titanic) — британский трансатлантический пассажирский пароход, второй лайнер класса «Олимпик» компании «White Star Line». Крупнейшее судно в мировой истории начала XX века. При строительстве получил номер 401.

Во время первого рейса, в ночь с 14 на 15 апреля 1912 года, столкнулся с айсбергом и затонул в Северной Атлантике.

Строился в Белфасте на верфи «Harland & Wolff» с 1909 по 1912 год. «Титаник» был оборудован двумя четырёхцилиндровыми паровыми машинами и паровой турбиной. Вся силовая установка обладала мощностью 55 000 л. с. Лайнер мог развивать скорость до 23 узлов (42 км/ч). Его водоизмещение, превышавшее пароход-близнец «Олимпик» на 243 т, составляло 52 310 т. Корпус судна был изготовлен из стали. Трюм и нижние палубы разделялись на 16 отсеков переборками с герметичными дверями. При повреждении днища попаданию воды в отсеки препятствовало двойное дно. Журнал «Shipbuilder» назвал «Титаник» практически непотопляемым, это высказывание получило широкое распространение в прессе и среди общественности. В соответствии с устаревшими правилами «Титаник» был оснащён 20 спасательными шлюпками, суммарной вместимостью 1178 человек, что составляло лишь треть от максимальной загрузки парохода.

Каюты и общественные помещения «Титаника» разделялись на три класса. К услугам пассажиров первого класса были представлены плавательный бассейн, корт для игры в сквош, ресторан «À La Carte», два кафе, гимнастический зал. Во всех классах имелись обеденные и курительные салоны, открытые и закрытые променады. Наиболее роскошными и изысканными были интерьеры первого класса, выполненные в различных художественных стилях с использованием дорогих материалов, таких как красное дерево, позолота, витражное стекло, шёлк и прочие. Каюты и салоны третьего класса оформлялись максимально просто: стальные стены окрашивались в белый цвет либо обшивались деревянными панелями.

10 апреля 1912 года «Титаник» отправился из Саутгемптона в Нью-Йорк, в свой первый и единственный рейс. Совершив остановки во французском Шербуре и ирландском Квинстауне, лайнер вышел в Атлантический океан с 1317 пассажирами и 908 членами экипажа на борту. Планировалось прибыть в Нью-Йорк 17 апреля. Командовал судном капитан Эдвард Смит. 14 апреля радиостанция «Титаника» приняла семь ледовых предупреждений, однако лайнер продолжал двигаться почти на предельной скорости. Чтобы избежать встречи с плавучими льдами, капитан приказал идти чуть южнее привычного маршрута.

14 апреля в 23:39 вперёдсмотрящий Фредерик Флит доложил на капитанский мостик об айсберге прямо по курсу. Меньше чем через минуту произошло столкновение. Получив несколько пробоин, пароход начал тонуть. В шлюпки сажали в первую очередь женщин и детей. В 2:20 15 апреля, разломившись на две части, «Титаник» затонул, унеся жизни 1496 человек. 712 спасшихся человек подобрал пароход «Карпатия».
Обломки «Титаника» покоятся на глубине 3750 м. Впервые их обнаружила экспедиция Роберта Балларда в 1985 году. Последующие экспедиции подняли со дна тысячи артефактов. Носовая и кормовая части глубоко ушли в донный ил и находятся в ветхом состоянии, подъём их на поверхность в целости не представляется возможным.''')
    st.header('Зачем это всё')
    st.markdown('''Проект реализован в рамках обучения по сетевой магистратуре [МИИГАиК](https://www.miigaik.ru/) совместно с [ТюМГУ](https://www.utmn.ru/) и подготовлен группой студентов имена которых знает только преподаватель.
    ''')
with tab2:
    var1()

with tab3:
    var8()

with tab4:
    var15()

with tab5:
    var16()
