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