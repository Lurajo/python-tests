from Menu import Menu


def test_get_user_coordinate():
    # Setup
    menu = Menu()
    coord_X = 1
    coord_Y = 1

    # Action
    result = menu.get_user_coordinate()

    # Assert
    assert (result.coordinateX == coord_X) and (result.coordinateY == coord_Y)
