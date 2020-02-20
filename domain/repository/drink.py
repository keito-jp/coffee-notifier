from typing import Protocol
from abc import abstractclassmethod
from domain.model.drink import Drink

class DrinkRepository(Protocol):
  @abstractclassmethod
  def serve_drink(self, drink: Drink):
    ...
