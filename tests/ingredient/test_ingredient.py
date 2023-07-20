from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingrediente_boi = Ingredient("boi")
    ingrediente_camarão = Ingredient("camarão")
    ingrediente_boi_2 = Ingredient("boi")

    assert ingrediente_boi.name == "boi"
    assert ingrediente_camarão.name == "camarão"
    assert ingrediente_boi_2.name == "boi"

    assert ingrediente_boi.__hash__() == ingrediente_boi_2.__hash__()

    assert ingrediente_boi.__hash__() != ingrediente_camarão.__hash__()

    assert ingrediente_boi.__eq__(ingrediente_boi) is True
    assert ingrediente_boi.__eq__(ingrediente_camarão) is False

    assert ingrediente_boi.__repr__() == "Ingredient('boi')"

    assert ingrediente_camarão.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
