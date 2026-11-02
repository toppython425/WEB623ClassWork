class Cart:

    def __init__(self, goods_prices):
        self.goods_prices = goods_prices
        self.total_prices = self.calculate_total_prices()

    def calculate_total_prices(self):
        total_price = 0
        for price in self.goods_prices.values():
            total_price += price
        return total_price


if __name__ == '__main__':
    cart1 = Cart({
        'мясо': 1000,
        'сыр': 600,
        'молоко': 400
    })
    print(cart1.total_prices)
