from Destination import Destination
from DestinationRepository import DestinationRepository


def test_set_destination_option():
    # Arrange
    repository = DestinationRepository()
    destination1 = Destination(1, "Test 1")
    destination2 = Destination(2, "Test 2")

    # Act
    repository.set_destination_option(destination1)

    # Assert
    assert len(repository.destination_list) == 1
    assert repository.destination_list[0].DDD == destination1.DDD
    assert repository.destination_list[0].destination == destination1.destination
    assert destination2 not in repository.destination_list


def test_check_if_option_exists():
    # Arrange
    repository = DestinationRepository()
    destination1 = Destination(1, "Test 1")
    option1 = 1
    option2 = 2

    # Act
    repository.set_destination_option(destination1)
    test_option1 = repository.check_if_option_exists(option1)
    test_option2 = repository.check_if_option_exists(option2)

    # Assert
    assert test_option1 == True
    assert test_option2 == False


def test_get_destination_by_DDD():
    # Arrange
    repository = DestinationRepository()
    destination1 = Destination(1, "Test 1")
    option1 = 1
    option2 = 2

    # Act
    repository.set_destination_option(destination1)
    test_option1 = repository.get_destination_by_DDD(option1)
    test_option2 = repository.get_destination_by_DDD(option2)

    # Assert
    assert test_option1 == destination1.destination
    assert test_option2 == None
