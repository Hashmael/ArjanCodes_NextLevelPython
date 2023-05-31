"""
Complete the program so that:

It generates all possible permutations of the data list
It then filters the permutations to only keep those where the first element is prime
Finally, it chains together the filtered permutations and then prints the sum
The expected output of this program is 1080.
"""
from itertools import chain, permutations
from functools import cache

@cache
def is_prime(n: int) -> bool:
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def main() -> None:
  # Test data
  data = [1, 2, 3, 4, 5]
  permutations_starting_with_a_prime = filter(lambda i: is_prime(i[0]), permutations(data))
  chained_permutations = chain(*permutations_starting_with_a_prime)

  # Print the sum of the chained permutations
  answer = sum(chained_permutations)
  print("Sum of chained permutations:", answer)
  assert answer == 1080


if __name__ == "__main__":
 main()
