from typing import List

from Destination import Destination


class DestinationRepository:
    destination_list: List[Destination] = []

    def __init__(self) -> None:
        pass

    def set_destination_option(self, destination: Destination) -> None:
        self.destination_list.append(destination)

    def check_if_option_exists(self, option: int) -> bool:
        for destination in self.destination_list:
            if (option == destination.DDD):
                return True

        return False

    def get_destination_by_DDD(self, option: int) -> str:
        for destination in self.destination_list:
            if (option == destination.DDD):
                return destination.destination

    def __str__(self) -> str:
        formatText = "{0:<5} {1:<15}\n"
        menu = formatText.format("DDD", "Destination")

        for destination in self.destination_list:
            menu += formatText.format(destination.DDD, destination.destination)

        return menu
