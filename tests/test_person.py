from lib.person import Person


def test_person_get_name():
    person = Person("Lea")

    assert person.get_name() == "Lea"