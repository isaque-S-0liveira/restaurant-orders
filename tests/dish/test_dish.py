from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    ingredient_camarão = Ingredient("camarão")
    dish_feijoada = Dish("Feijoada", 10.00)
    dish_acaraje = Dish("Acarajé", 5.00)

    assert dish_feijoada.name == "Feijoada"
    assert dish_acaraje.name == "Acarajé"

    assert dish_feijoada.__hash__() == dish_feijoada.__hash__()
    assert dish_feijoada.__hash__() != dish_acaraje.__hash__()

    assert dish_feijoada.__eq__(dish_feijoada) is True
    assert dish_feijoada.__eq__(dish_acaraje) is False

    assert dish_feijoada.__repr__() == "Dish('Feijoada', R$10.00)"
    dish_acaraje.add_ingredient_dependency(ingredient_camarão, 5)
    assert dish_acaraje.recipe.get(ingredient_camarão) == 5

    assert dish_acaraje.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
    assert dish_acaraje.get_ingredients() == {ingredient_camarão}

    with pytest.raises(TypeError):
        Dish("INVALIDE", "TYPE_ERROR")
    with pytest.raises(ValueError):
        Dish("INVALIDE", 00.0)
