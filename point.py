
import math

import xy, angle_dist, point_angle

class Point:
  def __init__(self, *args):
    if not args:
      self.x, self.y = 0,0
    elif len(args) == 2:
      self.x, self.y = args[0], args[1]
    elif hasattr(args[0], 'get_center'):
      self.set(args[0].get_center())
    else:
      self.set(args[0])
      
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
  
  # Move point
  def move_toward(self, point, dist=4):
    self.move_angle(angle_dist.angle(self, point), dist)

  def move_angle(self, angle, dist):
    p = point_angle.point_at_angle(base=(0,0), angle=angle, dist=dist)
    self.move_xy(p.x, p.y)

  def move_xy(self, x, y):
    self.x += x
    self.y += y  

# Test.
if __name__ == '__main__':
  p = Point(10, 20)
  p.set([30, 40])
  p = Point(p)
  print p
  print Point(10, 20).xy()
  print p[1]
  print p
  
  p.move_toward(Point(10,0))
  print p
  p.move_angle(angle=45, dist=4)
  print p
  p.move_xy(1,1)
  print p