from domain.repository import DrinkRepository
from domain.model import Drink

class ServeUseCase():
  def __init__(self, drink_repository: DrinkRepository) -> None:
    self.drink_repository = drink_repository

  def serve_drink(self, drink: Drink) -> None:
    self.drink_repository.serve_drink(drink)
