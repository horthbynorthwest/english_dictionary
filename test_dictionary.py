import pytest

from dictionary import definition

def test_returns_definition():
    solution = definition("mathematics")

    assert solution == ["The science that deals with concepts such as quantity, structure, space and change."]

def test_fails_with_incorrect_word():
    # How to test for errors!!
    # with pytest.raises(Exception):
    #     definition("aaasdf")
    solution = definition("aaasdf")

    assert solution == "That word doesn't exist. Please double check your spelling."

def test_can_handle_different_cases():
    solution = definition("RAIN")

    assert solution == ["Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.",
    "To fall from the clouds in drops of water."]