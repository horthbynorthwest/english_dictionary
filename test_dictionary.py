import pytest

from dictionary import definition, word_check

# definition tests

def test_returns_definition():
    solution = definition("mathematics")

    assert solution == ["The science that deals with concepts such as quantity, structure, space and change."]

def test_fails_with_incorrect_word():
    # How to test for errors!!
    # with pytest.raises(Exception):
    #     definition("aaasdf")
    solution = definition("aaasdf")

    assert solution == "That word doesn't exist. Please double check your spelling."

def test_can_handle_upper_case():
    solution = definition("RAIN")

    assert solution == ["Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.",
    "To fall from the clouds in drops of water."]

def test_can_handle_mixed_cases():
    solution = definition("RAiN")

    assert solution == ["Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.",
    "To fall from the clouds in drops of water."]

def test_can_suggest_words():
    solution = definition("rainn")

    assert solution == "Did you mean rain?"

def test_can_deal_with_proper_nouns():
    solution = definition("paris")

    assert solution == ["The capital and largest city of France."]

def test_can_deal_with_acronyms():
    solution = definition("nato")

    assert solution == ["An international organization created in 1949 by the North Atlantic Treaty for purposes of collective security."]

# word_check tests 

def test_returns_list_of_close_matches():
    solution = word_check("rainn")

    assert solution == ["rain", "train", "rainy"]