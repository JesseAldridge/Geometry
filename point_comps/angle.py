
import math

from jca.geometry import point_angle

class Component:
  def rotate(self, angle):
    angle = math.radians(angle)

    #~ """
    #~ The inverted y-axis makes things clockwise instead of 
    #~ counter-clockwise.
    #~ """
    #~ angle *= -1

    self.set(math.cos(angle) * self.x - math.sin(angle) * self.y,
         math.sin(angle) * self.x + math.cos(angle) * self.y)
  
  def angle(self): 
    return point_angle.angle((0,0), self)

if __name__ == "__main__":
  from jca import stubs
  
  stub = stubs.make_stub(__file__, args=[1, 1])
  stub.set(1, 0)
  results = []
  for i in range(13):
    results.append(round(stub.angle()))
    stub.rotate(30)
  print results
  
  stub.set(200, 100)
  print stub.angle()