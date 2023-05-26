from dataclasses import dataclass, FrozenInstanceError
from math import pi
from warnings import warn
from functools import cached_property

@dataclass(frozen=True)
class Circle:
  radius: float
  
  """
  As a side effect of assuming read-only, we can freeze the dataclass instead of relying on a protected naming convention and a property
  """
#   @property
#   def radius(self) -> float:
#     return self._radius

  """
  Under normal circumstances this is a smell indicating _radius should be public instead;
  I'm going to assume that the assignment's underlying intention was that radius be read-only,
  and comment out this setter
  """
#   @radius.setter
#   def radius(self, radius_value_in_unknown_units: float) -> None:
#    self._radius = radius_value_in_unknown_units

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
    print("Diameter:", self.diameter)
    print("Area:", self.area)
    print("Circumference:", self.circumference)


# Create an instance of Circle
circle = Circle(5)

# Test the properties
print("Radius:", circle.radius)
# Per comments above
try:
  circle.radius = 10
  warn('Are you sure that you want Circle\'s radius attribute to be mutable?')
  print(f"New radius: {circle.radius}")
except FrozenInstanceError:
  print('Good job freezing your dataclass!')
circle.print_properties()
print("Verifying that values are not recalculated...")
circle.print_properties()
