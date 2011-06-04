
from jca.geometry import xy

class Stub:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  #
  
  def set(self, *args):
    self.x, self.y = xy.extract(*args)
  
  def __repr__(self):
    return "<PointStub: %f %f>" % (self.x, self.y)
    
  def angle(self):
    return 45
#

if __name__ == "__main__":
  stub = Stub(0,0)
  print stub