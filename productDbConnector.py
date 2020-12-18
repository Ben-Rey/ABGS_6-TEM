from fakeDbProduct import FakeDbProduct

products = [
    {
        "code": "1111",
        "name": "Drill",
        "price": 5
    },
    {
        "code": "2222",
        "name": "Screw",
        "price": 5
    },
    {
        "code": "3333",
        "name": "Hammer",
        "price": 5
    },
]


class ProductDbConnector:
    def __init__(self):
        db = FakeDbProduct()
        self.products = db.products

    @staticmethod
    def get_product_by_code(code):
        try:
            return next(item for item in products if item["code"] == code)

        except Exception as e:
            return None
