
from jca.geometry import angle_dist, point_angle

class Component:
  def move_toward(self, point, dist=4):
    self.move_angle(angle_dist.angle(self, point), dist)

  def move_angle(self, angle, dist):
    p = point_angle.point_at_angle(base=(0,0), angle=angle, dist=dist)
    self.move_xy(p.x, p.y)

  def move_xy(self, x, y):
    self.x += x
    self.y += y  

if __name__ == "__main__":
  from jca import stubs
  from jca.geometry import point
  
  stub = stubs.make_stub(__file__, args=[0, 0])
  print stub
  stub.move_toward(point.Point(10,0))
  print stub
  stub.move_angle(angle=45, dist=4)
  print stub
  stub.move_xy(1,1)
  print stub