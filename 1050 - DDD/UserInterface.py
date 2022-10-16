from DestinationRepository import DestinationRepository


class UserInterface:
    def __init__(self, destination_repository: DestinationRepository) -> None:
        self.destination_repository = destination_repository

    def get_user_input(self) -> int:
        user_input = int(input("Inform a valid DDD code from menu: "))
        return user_input

    def show_destination(self, option: int) -> str:
        return self.destination_repository.get_destination_by_DDD(option)

    def interface_output(self) -> str:
        option = self.get_user_input()

        if (self.destination_repository.check_if_option_exists(option)):
            return self.show_destination(option)

        return "DDD not registered"
