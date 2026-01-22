""""""


"""
DeliveryPerson
BicycleCourier, ScooterCourier и CarCourier
BicycleCourier = 15 min
ScooterCourie = 8 min
CarCourier = 18 min
"""

class DeliveryPerson:
    def __init__(self, name):
        self.name = name

    def calculate_time(self):
        raise NotImplementedError('Подкласс должен реализовать метод transport')

class BicycleCourier(DeliveryPerson):
    def calculate_time(self):
        return f'Курьер {self.name} на велосипеде доставит ваш заказ через 15 мин'

class ScooterCourier(DeliveryPerson):
    def calculate_time(self):
        return f'Курьер {self.name} на мопеде доставит ваш заказ через 8 мин'


class CarCourier(DeliveryPerson):
    def calculate_time(self):
        return f'Курьер {self.name} на машине доставит ваш заказ через 18 мин'

bicycle_courier = BicycleCourier('Иван')
print(bicycle_courier.calculate_time())

scooter_courier = ScooterCourier('Сергей')
print(scooter_courier.calculate_time())





