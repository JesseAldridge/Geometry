
import math

import xy
from point_comps import init, math_ops, move

class Point(init.Component, math_ops.Component, move.Component):
  def __getitem__(self, index):
    return [self.x, self.y][index]

  def set(self, *args):
    self.x, self.y = xy.extract(*args)
    
  def __cmp__(self, other):    
    if other is None:
      return -1

    other_x, other_y = xy.extract(other)
    if abs(self.x - other_x) < .01 and abs(self.y - other_y) < .01:
      return 0
      
    return cmp(self.x, other.x)
    
  def xy(self):  return (self.x, self.y)    
  def __repr__(self):  return "<Point: %f %f>" % (self.x, self.y)
    
  def rotate(self, angle):
    angle = math.radians(angle)
    # The inverted y-axis makes things clockwise instead of 
    # counter-clockwise.
    # angle *= -1
    self.set(math.cos(angle) * self.x - math.sin(angle) * self.y,
         math.sin(angle) * self.x + math.cos(angle) * self.y)
  
  def angle(self):  return point_angle.angle((0,0), self)

if __name__ == '__main__':
  p = Point(10, 20)
  p.set([30, 40])
  p = Point(p)
  print p
  print Point(10, 20).xy()
  print p[1]
  print p