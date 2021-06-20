class Car:
    """
    Car Class
    Author : Lee Jongwoo
    Date : 2021-06-21
    """

    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return "str: {} - {}".format(self._company, self._details)

    def __repr__(self):
        return "repr: {} - {}".format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print(
            "Car Detail Info : {} {}".format(self._company, self._details.get("price"))
        )


car1 = Car("Ferrari", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})

# dir & __dict__

# print(car1.__dict__)
# print(dir(car1))

# print(Car.__doc__)

car1.detail_info()
