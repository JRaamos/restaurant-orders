from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    def create_ingredient(name):
        return Ingredient(name)

    ingredient = create_ingredient("queijo mussarela")
    assert isinstance(ingredient, Ingredient)
    assert ingredient.name == "queijo mussarela"

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == expected_restrictions

    expected_repr = f"Ingredient('{ingredient.name}')"
    assert repr(ingredient) == expected_repr

    ingredient1 = create_ingredient("queijo mussarela")
    ingredient2 = create_ingredient("queijo mussarela")
    ingredient3 = create_ingredient("bacon")
    assert ingredient1 == ingredient2
    assert not (ingredient1 == ingredient3)

    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)

    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions == expected_restrictions

    unexpected_restrictions = {Restriction.GLUTEN, Restriction.SEAFOOD}
    assert ingredient.restrictions != unexpected_restrictions
