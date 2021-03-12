from dictionary import definition

def test_returns_definition():
    solution = definition("mathematics")

    assert solution == ["The science that deals with concepts such as quantity, structure, space and change."]