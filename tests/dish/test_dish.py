from src.models.dish import Dish
from models.ingredient import Ingredient
import pytest


def test_dish():
    sample_dish = Dish("Prato Exemplo", 10.99)
    other_dish = Dish("Outro Prato", 15.99)

    assert hash(sample_dish) != hash(other_dish)
    assert isinstance(sample_dish.price, float)
    assert sample_dish.price == 10.99
    assert not sample_dish.recipe  #

    sample_dish = Dish("Prato Exemplo", 10.99)
    duplicate_dish = Dish("Prato Exemplo", 10.99)

    assert hash(sample_dish) == hash(duplicate_dish)
    expected_repr = f"Dish('{sample_dish.name}', R${sample_dish.price:.2f})"
    assert repr(sample_dish) == expected_repr

    duplicate_dish = Dish("Prato Exemplo", 10.99)
    assert sample_dish == duplicate_dish

    # Verifica se o preço é um número real
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Prato Inválido", "invalid_price")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Prato Inválido", 0)

    cheese = Ingredient("Queijo")
    tomato = Ingredient("Tomate")

    sample_dish.add_ingredient_dependency(cheese, 100)
    sample_dish.add_ingredient_dependency(tomato, 150)

    dish = Dish("Pizza", 15.99)
    dish.add_ingredient_dependency(cheese, 100)
    dish.add_ingredient_dependency(tomato, 150)

    expected_restrictions = set()
    assert dish.get_restrictions() == expected_restrictions

    assert sample_dish.get_ingredients() == {cheese, tomato}

    assert sample_dish.recipe.get(cheese) == 100
