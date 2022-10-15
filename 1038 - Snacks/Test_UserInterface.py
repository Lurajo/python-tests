from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order


def test_get_total_price():
    # Arrange
    menu_repository = MenuRepository()
    menu1 = Menu(1, "Test 1", 10)
    order1 = Order(1, 10)
    order2 = Order(2, 10)

    # Act
    menu_repository.set_menu_item(menu1)
    total_price1 = menu_repository.get_total_price(order1)
    total_price2 = menu_repository.get_total_price(order2)

    # Assert
    assert total_price1 == 100
    assert total_price2 == None
