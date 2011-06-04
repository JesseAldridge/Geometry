
from jca.geometry import xy, directions
from jca.geometry.point import Point

class Basics:
  # Getters
  def x(self):  return self.left()
  def y(self):  return self.top()
  def x_center(self):  return (self.left() + self.right()) / 2
  def y_center(self):  return (self.top() + self.bottom()) / 2
  def bounds(self):
    return [self.left(), self.top(), self.right(), self.bottom()]
  ltrb = bounds
  def xywh(self):  return self.left(), self.top(), self.width(), self.height()
  def width(self):  return self.right() - self.left()
  def height(self):  return self.bottom() - self.top()
  def size(self):  return (self.width(), self.height())
    
  # Setters
  def set_right(self, right):
    self.set_left(right - self.width())
    return self
  def set_bottom(self, bottom):
    self.set_top(bottom - self.top())
    return self
  def set_x_center(self, x):
    self.set_left(x - self.width() / 2)
    return self
  def set_y_center(self, y):
    self.set_top(y - self.height() / 2)
    return self
  def set_indep(self, dir_string, new_val):
    new_vals = self.ltrb()
    new_vals[directions.string_to_dir(dir_string)] = new_val
    self.set_bounds(*new_vals)
    return self
  
  # Intersections  
  def is_collision(self, other):
    return (self.left() < other.right() and 
            self.right() > other.left() and
            self.top() < other.bottom() and 
            self.bottom() > other.top())

  def is_point_in(self, *args):
    x,y = xy.extract(*args)
    return (x > self.left() and x < self.right() and 
        y > self.top() and y < self.bottom())
  
  # Point getters.  
  def points(self):
    x,y,w,h = self.xywh()
    return [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]
  def top_left(self):  return Point(self.left(), self.top())
  def top_right(self):  return Point(self.right(), self.top())
  def bottom_right(self):  return Point(self.right(), self.bottom())
  def bottom_left(self):  return Point(self.left(), self.bottom())
  def center(self):  return Point(self.x_center(), self.y_center())
  def midpoint(self, index):  return self.midpoints()[index]  
  def mid_left(self): return self.midpoint(0)
  def mid_top(self): return self.midpoint(1)
  def mid_right(self): return self.midpoint(2)
  def mid_bottom(self): return self.midpoint(3)
  def midpoints(self):
    return (Point(self.left(), self.y_center()),
            Point(self.x_center(), self.top()),
            Point(self.right(), self.y_center()),
            Point(self.x_center(), self.bottom()))

if __name__ == "__main__":
  from stub import Stub
  class MyStub(Basics, Stub):  pass
  stub = MyStub()
  stub.left_, stub.top_, stub.right_, stub.bottom_ = (100,100,200,200)

  print "original: ", stub
  print 'set x center: ', stub.set_x_center(100)
  print 'set y center: ', stub.set_y_center(100)
  print 'set indep: ', stub.set_indep("left", 100)

  other = MyStub()
  print 'other: ', other
  print 'is collision: ', stub.is_collision(other)
  print 'is point in: ', stub.is_point_in(other.center())
  
  for s in ["center", "points", "top_left", "top_right", "bottom_right",
            "bottom_left", "midpoints"]:
    print "%s: %s" % (s, unicode(getattr(stub, s)()))