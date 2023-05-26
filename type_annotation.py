from typing import Sequence
from numbers import Number

def calculate_average(numbers: Sequence[Number]) -> Number:
  total = sum(numbers)
  return total / len(numbers)

def calculate_total_sales(sales: dict[str, Number]) -> Number:
  return sum(sales.values())

def main():
  data = [1, 2, 3, 4, 5]
  average = calculate_average(data)
  print("The average is:", average)

  sales_data = {"product_a": 100, "product_b": 250, "product_c": 80,  
                "product_d": 150}
  print("Sales data for product C:", sales_data["product_c"])
  total_sales = calculate_total_sales(sales_data)
  print("Total sales:", total_sales)

if __name__ == "__main__":
  main()