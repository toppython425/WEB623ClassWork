def with_tax(value: (int, float), tax_percentage: float) -> float:
    total = value + value * tax_percentage / 100
    return total


if __name__ == '__main__':
    print(f'Сумма с налогом: {with_tax(10000, 6)}')
    price = 60000
    sale_tax = 20
    print(f'Сумма с налогом: {with_tax(price, sale_tax)}')
