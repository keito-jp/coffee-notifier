from domain.model import Drink
from domain.repository import DrinkRepository

class DrinkRepositoryImpl(DrinkRepository):
  def serve_drink(self, drink: Drink):
    print(drink.get_name() + "!")
