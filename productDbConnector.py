from fakeDbProduct import FakeDbProduct


class ProductDbConnector:
    def __init__(self):
        db = FakeDbProduct()
        self.products = db.products

    def get_product_by_code(self, code):
        try:
            return next(item for item in self.products if item["code"] == code)

        except Exception as e:
            return None
