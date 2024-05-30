from pages.var_8.scripts.titanic import Titanic


def test_failed_file_name():
    titanic = Titanic(path_name='fasfasfas.csv')
    assert titanic.get_class() == {}


def test_class_sex_data():
    lines = [
        'PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked',
        '1,1,1,0,male,0,0,0,0,1.125,0,0',
        '2,1,1,0,female,0,0,0,0,25.1222,0,0',
        '3,0,2,0,male,0,0,0,0,25.12,0,0',
        '4,1,2,0,female,0,0,0,0,12.125,0,0',
        '5,1,3,0,male,0,0,0,0,21.5125,0,0',
        '6,1,3,0,female,0,0,0,0,1.51,0,0',
        '7,1,2,0,male,0,0,0,0,21.1241242,0,0',
        '8,1,1,0,male,0,0,0,0,123.4,0,0',
        '9,1,3,0,female,0,0,0,0,42.2,0,0',
        '10,1,3,0,female,0,0,0,0,12.21,0,0'
    ]
    titanic = Titanic()
    titanic.get_data_from_list(lines)
    assert titanic.get_class() == {
        '1': {
            'male': 2,
            'female': 1,
        },
        '2': {
            'male': 2,
            'female': 1,
        },
        '3': {
            'male': 1,
            'female': 3,
        }
    }


def test_sex_class_data():
    lines = [
        'PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked',
        '1,1,1,0,male,0,0,0,0,1.125,0,0',
        '2,1,1,0,female,0,0,0,0,25.1222,0,0',
        '3,0,2,0,male,0,0,0,0,25.12,0,0',
        '4,1,1,0,female,0,0,0,0,12.125,0,0',
        '5,1,3,0,male,0,0,0,0,21.5125,0,0',
        '6,1,3,0,female,0,0,0,0,1.51,0,0',
        '7,1,2,0,male,0,0,0,0,21.1241242,0,0',
        '8,1,1,0,male,0,0,0,0,123.4,0,0',
        '9,1,3,0,female,0,0,0,0,42.2,0,0',
        '10,1,3,0,female,0,0,0,0,12.21,0,0'
    ]
    titanic = Titanic()
    titanic.get_data_from_list(lines)
    assert titanic.get_sex() == {
        'male': {'1': 2,
                 '2': 2,
                 '3': 1
                 },
        'female': {'1': 2,
                   '2': 0,
                   '3': 3}

    }
