from time import strptime


class Food:
    def __init__(self, expiration_date):
        self.expiration_date = expiration_date
        # self.expiration_date_as_date = strptime(expiration_date, "%d/%m/%y")


# food = Food("31/10/  22")
# print(food.expiration_date)
# print(food.expiration_date_as_date)
