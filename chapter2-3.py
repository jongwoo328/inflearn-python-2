class Car:
    """
    Car Class
    Author : Lee Jongwoo
    Date : 2021-06-21
    """

    car_count = 0
    price_per_raise = 1.0

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

    # Instance Method
    # self -> 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print(
            "Car Detail Info : {} {}".format(self._company, self._details.get("price"))
        )

    def get_price(self):
        return "Before Car Price -> company : {}, price : {}".format(
            self._company, self._details.get("price")
        )

    def get_price_calc(self):
        return "After Car Price -> company : {}, price : {}".format(
            self._company, self._details.get("price") * Car.price_per_raise
        )

    @classmethod
    def raise_price(cls, per):
        cls.price_per_raise = per


car1 = Car("Ferrari", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})


# 전체정보
car1.detail_info()

# 가격정보 (인상 전)
print(car1.get_price())

# 가격인상 (클래스메소드 미사용)
Car.price_per_raise = 1.4
print(car1.get_price_calc())

# 가격인상 (클래스메소드)
Car.raise_price(1.5)
print(car1.get_price_calc())
