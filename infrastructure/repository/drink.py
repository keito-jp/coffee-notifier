from domain.model import Drink
from domain.repository import DrinkRepository
from slackweb import Slack
from os import environ

class DrinkRepositoryImpl(DrinkRepository):
  def serve_drink(self, drink: Drink):
    slack = Slack(url=environ['SLACK_URL'])
    text = drink.get_name() + 'が出来上がりました。'
    slack.notify(
      username = 'Coffee Notifier',
      icon_url = environ['SLACK_ICON_URL'],
      text = text
    )
