from lib.party import Party
from lib.person import Person
from unittest.mock import Mock

def test_party_instantiate(): 
    party = Party()

    assert party.guest_list == []

def test_party_invite_unit():
    party = Party()
    guest = Mock()
    guest.name = "Lea"

    party.invite(guest)
    assert party.guest_list[0].name == "Lea"
    assert len(party.guest_list) == 1

def test_party_invite_integration():
    party = Party()
    guest = Person("Lea")

    party.invite(guest)
    assert party.guest_list[0].name == "Lea"

def test_party_get_guests_returns_list(): 
     party = Party()

     assert party.get_guests() == []

def test_party_get_guests_unit(): 
    party = Party()
    guest_one = Mock()
    guest_two = Mock()
    guest_three = Mock()

    guest_one.get_name.return_value = "guest_one"
    guest_two.get_name.return_value = "guest_two"
    guest_three.get_name.return_value = "guest_three"

    party.invite(guest_one)
    party.invite(guest_two)
    party.invite(guest_three)

    assert party.get_guests() == ["guest_one","guest_two","guest_three"]

def test_party_get_guests_integration():
    party = Party()
    guest_one = Person("Lea")
    guest_two = Person("Hugo")
    guest_three = Person("Laurent")

    party.invite(guest_one)
    party.invite(guest_two)
    party.invite(guest_three)

    assert party.get_guests() == ["Lea","Hugo","Laurent"]