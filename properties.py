from dataclasses import dataclass, FrozenInstanceError
from math import pi
from warnings import warn

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

  @property
  def diameter(self) -> float:
    return 2 * self.radius
  
  @property
  def area(self) -> float:
    return pi * self.radius ** 2
  
  @property
  def circumference(self) -> float:
    return 2 * pi * self.radius


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
print("Diameter:", circle.diameter)
print("Area:", circle.area)
print("Circumference:", circle.circumference)
