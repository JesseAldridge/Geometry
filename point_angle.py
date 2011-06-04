
import math

import xy, angles

def point_at_angle(angle, dist=1, base=(0,0)):
  import point
  p = point.Point(dist, 0)
  p.rotate(angle)
  p = p + base
  return p

def angle(p1, p2):  
  x1, y1 = xy.extract(p1)
  x2, y2 = xy.extract(p2)
  rel_x, rel_y = x2 - x1, y2 - y1
  angle = math.atan2(rel_y, rel_x) * 180. / math.pi
  return angles.wrap_angle(angle)

if __name__ == "__main__":
  print point_at_angle(30)
  print point_at_angle(30, base=(100,100))
  print angle((0,0), (1,1))