from Destination import Destination
from DestinationRepository import DestinationRepository
from UserInterface import UserInterface

destination_repository = DestinationRepository()
destination_repository.set_destination_option(Destination(61, "Brasilia"))
destination_repository.set_destination_option(Destination(71, "Salvador"))
destination_repository.set_destination_option(Destination(11, "Sao Paulo"))
destination_repository.set_destination_option(Destination(21, "Rio de Janeiro"))
destination_repository.set_destination_option(Destination(32, "Juiz de Fora"))
destination_repository.set_destination_option(Destination(19, "Campinas"))
destination_repository.set_destination_option(Destination(27, "Vitoria"))
destination_repository.set_destination_option(Destination(31, "Belo Horizonte"))

print(destination_repository)

user_interface = UserInterface(destination_repository)

while True:
    output = user_interface.interface_output()

    print(output)

    if (output == "DDD not registered"):
        break
