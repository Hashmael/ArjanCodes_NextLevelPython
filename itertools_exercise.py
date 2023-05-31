"""
Use a function from the itertools package to generate all possible combinations of length 2 from the data list.
Then calculate the average of each combination and store the results in a new list averages.
"""

from statistics import mean
from itertools import combinations
from functools import cached_property

class AveragedTuple(tuple):

  def __init__(self, *_unused_args) -> None:
    """
    Tried doing this with calling super() and super(tuple, self); apparently that is both unnecessary and will
    result in an exception. Seems like something interesting going on with tuple's MRO? 
    """
    if not all(isinstance(arg, float) or isinstance(arg, int) for arg in self):
      raise TypeError(f'TypeError: All values of an AveragedTuple must be of type int or float. Given values: {self}')

  @cached_property
  def average(self) -> float:
    """
    Might as well be cached, tuples are immutable
    """
    return mean(self)
  
def print_combo_pair_averages(data: list[int | float]) -> None:
  print(f'{data = }')
  combos: map[AveragedTuple] = map(AveragedTuple, combinations(data, 2))
  for combo in combos:
    print(f'{combo = } {combo.average = }')


def main() -> None:
  bad_data = [1, 2, 3, 4, 'a']
  try:
    print_combo_pair_averages(bad_data)
  except TypeError as te:
    print(te)
  good_data = range(1, 6)
  print_combo_pair_averages(good_data)

if __name__ == "__main__":
  main()