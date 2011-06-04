
from jca.geometry import xy

class Component:

    
if __name__ == "__main__":
  from jca import stubs
  
  stub = stubs.make_stub(__file__)
  other = stubs.make_stub(__file__)
  def comp():
    print [stub > other, stub == other, stub < other]
  stub.set(1,1)
  other.set(1,1)
  comp()
  other.set(0,0)
  comp()
  other.set(2,2)
  comp()