
from jca.geometry import xy

class Component:
  # Arithmetic operators for points.
  def __add__(self, other):
    x, y = xy.extract(other)
    return self.__class__(self.x + x, self.y + y)
  def __sub__(self, other):
    x,y = xy.extract(other)
    return self.__class__(self.x - x, self.y - y)
  def __mul__(self, scalar):
    return self.__class__(self.x * scalar, self.y * scalar)
  def __div__(self, other):
    if type(other) == type(1.0) or type(other) == type(1):
      return self * (1. / other)
    else:
      return self.__class__(float(self.x) / other.x, 
                  float(self.y) / other.y)

if __name__ == "__main__":
  from jca import stubs
  
  stub, other = [stubs.make_stub(__file__, args=[1,1]) for i in range(2)]
  print stub + other
  print stub - other
  print stub * 3
  print stub / other