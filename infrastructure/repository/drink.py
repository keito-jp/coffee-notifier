from domain.model import Drink
from domain.repository import DrinkRepository
from slackweb import Slack
from os import environ

class DrinkRepositoryImpl(DrinkRepository):
  def serve_drink(self, drink: Drink):
    slack = Slack(url=environ["SLACK_URL"])
    slack.notify(text=drink.get_name() + "!")
    print(drink.get_name() + "!")
