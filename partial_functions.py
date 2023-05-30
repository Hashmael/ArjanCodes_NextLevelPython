from functools import partial

def power(base: float, exponent: float) -> float:
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

def main() -> None:
  print("Square of 5:", sq5:=square(5))
  assert sq5 == 25
  print("Cube of 3:", cb3:=cube(3))
  assert cb3 == 27

if __name__ == "__main__":
  main()