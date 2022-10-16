from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order
from UserInterface import UserInterface


def test_get_total_price():
    # Arrange
    menu_repository = MenuRepository()
    menu1 = Menu(1, "Test 1", 10)
    user_interface = UserInterface(menu_repository)
    order1 = Order(1, 10)
    order2 = Order(2, 10)

    # Act
    menu_repository.set_menu_item(menu1)
    total_price1 = user_interface.get_total_price(order1)
    total_price2 = user_interface.get_total_price(order2)

    # Assert
    assert total_price1 == 100
    assert total_price2 == None


def test_get_user_input():
    # Arrange
    menu_repository = MenuRepository()
    user_interface = UserInterface(menu_repository)
    test_order = Order(1, 10)

    # Act
    order = user_interface.get_user_input()

    # Assert
    assert order.code == test_order.code
    assert order.quantity == test_order.quantity
