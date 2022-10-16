from Destination import Destination
from DestinationRepository import DestinationRepository
from UserInterface import UserInterface


def test_get_user_input():
    # Arrange
    repository = DestinationRepository()
    user_interface = UserInterface(repository)
    option = 1

    # Act
    test_option = user_interface.get_user_input()

    # Assert
    assert test_option == option


def test_show_destination():
    # Arrange
    repository = DestinationRepository()
    destination = Destination(1, "Test 1")
    user_interface = UserInterface(repository)
    option1 = 1
    option2 = 2

    # Act
    repository.set_destination_option(destination)
    test_option1 = user_interface.show_destination(option1)
    test_option2 = user_interface.show_destination(option2)

    # Assert
    assert test_option1 == destination.destination
    assert test_option2 == None


def test_interface_output():
    # Arrange
    repository = DestinationRepository()
    destination = Destination(1, "Test 1")
    user_interface = UserInterface(repository)

    # Act
    repository.set_destination_option(destination)
    test_option1 = user_interface.interface_output()
    test_option2 = user_interface.interface_output()

    # Assert
    assert test_option1 == destination.destination
    assert test_option2 == "DDD not registered"
