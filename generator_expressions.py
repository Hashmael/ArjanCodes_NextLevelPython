"""
The expected output of the program is:

Orders larger than $100:
  $300.00
  $180.00
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Generator

SOLUTION_PRICES = (Decimal("300.00"), Decimal("180.00"))

@dataclass
class Order:
  product: str
  quantity: int
  unit_price: Decimal

  @property
  def total_price(self) -> Decimal:
    """
    Encapsulate to the order
    """
    return self.quantity * self.unit_price

def main() -> None:
  sales_orders = [
    Order(product="A", quantity=5, unit_price=Decimal("60.00")),
    Order(product="B", quantity=3, unit_price=Decimal("15.00")),
    Order(product="C", quantity=2, unit_price=Decimal("20.00")),
    Order(product="D", quantity=4, unit_price=Decimal("45.00")),
  ]

  # Use a generator expression to generate a sequence of total prices for each sales order
  total_prices: Generator[Decimal, None, None] = (sales_order.total_price for sales_order in sales_orders)

  # Use another generator expression to filter the total prices sequence
  # and keep only the orders with a price greater than $100
  filtered_prices: filter[Decimal] = filter(lambda tp: tp > Decimal("100.00"), total_prices)

  # Print all total prices above $100
  print("Orders larger than $100:")
  for price, solution_price in zip(filtered_prices, SOLUTION_PRICES):
    print(f" ${price:.2f}")
    assert price == solution_price


if __name__ == "__main__":
  main()