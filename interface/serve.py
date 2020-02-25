from domain.model.drink import Drink
from application.usecase import ServeUseCase
from infrastructure.repository import DrinkRepositoryImpl

usecase = ServeUseCase(drink_repository = DrinkRepositoryImpl())
usecase.serve_drink(Drink(name = 'コーヒー'))
