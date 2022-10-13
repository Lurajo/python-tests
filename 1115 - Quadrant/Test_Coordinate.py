from Coordinate import Coordinate


def test_coordinate():
    # Setup
    coord_X = 1
    coord_Y = 2

    # Action
    result = Coordinate(coord_X, coord_Y)

    # Assert
    assert (result.coordinateX == coord_X) and (result.coordinateY == coord_Y)
