
import math

from jca.geometry import xy

def dist(p1, p2):
  return math.sqrt(square_dist(p1, p2))

def square_dist(p1, p2):
  x1, y1 = xy.extract(p1)
  x2, y2 = xy.extract(p2)
  val = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
  return abs(val)

if __name__ == '__main__':   
  from jca.geometry import point  
  Point = point.Point
  print dist(Point(0,0), Point(10,20))
  print square_dist(Point(-10,-10), Point(0,0))
