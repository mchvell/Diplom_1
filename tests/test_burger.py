from unittest.mock import Mock

from practikum.burger import Burger
from practikum.bun import Bun
from practikum.ingredient import Ingredient


class TestBurger:
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Sesame", 1.5)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient("Cheese", "Беконайзер", 2.0)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("Cheese", "Сыр", 2.0)
        ingredient2 = Ingredient("Lettuce", "Салат", 0.5)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("Cheese", "Сыр", 2.0)
        ingredient2 = Ingredient("Lettuce", "Салат",0.5)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient2 and burger.ingredients[1] == ingredient1

    def test_get_price(self):
        burger = Burger()
        bun = Bun("Sesame", 1.5)
        ingredient1 = Ingredient("Cheese", "Сыр", 2.0)
        ingredient2 = Ingredient("Lettuce", "Салат", 0.5)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        expected_price = bun.get_price() * 2 + ingredient1.get_price() + ingredient2.get_price()

        assert burger.get_price() == expected_price, f"Ожидаемая цена {expected_price}, а была {burger.get_price()}"

    def test_get_receipt(self):
        bun_mock = Mock()
        bun_mock.get_name.return_value = 'Булочка Бриошь'

        ingredient1_mock = Mock()
        ingredient1_mock.get_type.return_value = 'Мясо'
        ingredient1_mock.get_name.return_value = 'Говяжья котлета'

        ingredient2_mock = Mock()
        ingredient2_mock.get_type.return_value = 'Соус'
        ingredient2_mock.get_name.return_value = 'Шрирача'

        obj = Mock()
        obj.bun = bun_mock
        obj.ingredients = [ingredient1_mock, ingredient2_mock]
        obj.get_price.return_value = 12.50

        obj.get_receipt.return_value = (
            "(==== Булочка Бриошь ====)\n"
            "= мясо Говяжья котлета =\n"
            "= соус Шрирача =\n"
            "(==== Булочка Бриошь ====)\n"
            "Price: 12.5"
        )

        result = obj.get_receipt()

        expected_receipt = (
            "(==== Булочка Бриошь ====)\n"
            "= мясо Говяжья котлета =\n"
            "= соус Шрирача =\n"
            "(==== Булочка Бриошь ====)\n"
            "Price: 12.5"
        )

        assert result == expected_receipt
