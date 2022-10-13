from Coordinate import Coordinate
from Menu import Menu


def test_cordinate_is_valid():
    # Setup
    menu = Menu()
    coord_X = 1
    coord_Y = 1
    menu.coordinates = Coordinate(coord_X, coord_Y)

    # Action
    result = menu.cordinate_is_valid(menu.coordinates)

    # Assert
    assert result == True
