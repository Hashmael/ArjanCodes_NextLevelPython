from dataclasses import dataclass
from math import pi
from functools import cached_property
import random

@dataclass
class Circle:
  _radius: float
  

  @property
  def radius(self) -> float:
    return self._radius


  @radius.setter
  def radius(self, radius_value: float) -> None:
   if radius_value < 0:
     raise ValueError('Radius must be a non-negative number')
   self._radius = radius_value
   # Clear the cached properties whenever the radius changes
   del self.area
   del self.circumference
   del self.diameter

  @cached_property
  def diameter(self) -> float:
    print('Calculating diameter')
    return 2 * self.radius
  
  @cached_property
  def area(self) -> float:
    print('Calculating area')
    return pi * self.radius ** 2
  
  @cached_property
  def circumference(self) -> float:
    print('Calculating circumference')
    return 2 * pi * self.radius
  
  def print_properties(self) -> None:
    print("Radius:", self.radius)
    print("Diameter:", self.diameter)
    print("Area:", self.area)
    print("Circumference:", self.circumference)

def test_radius_setter_valid(circle: Circle) -> None:
  new_radius = circle.radius + 1
  circle.radius = new_radius
  assert circle.radius == new_radius

def test_radius_setter_invalid(circle: Circle) -> None:
  try:
    circle.radius = float(random.choice(range(-1024, -1)))
    raise ValueError('Circle class does not validate for negative radius values')
  except ValueError:
    print('Circle class validates for negative radius values')

def test_circle_class() -> None:
  circle = Circle(5)
  circle.print_properties()
  test_radius_setter_invalid(circle)
  test_radius_setter_valid(circle)
  print("Check this output to ensure that values are recalculated after changing the radius...")
  circle.print_properties()
  print("Check this output to ensure that values are *not* recalculated...")
  circle.print_properties()

if __name__ == '__main__':
  test_circle_class()
