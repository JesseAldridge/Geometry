
class Component:
  def __init__(self, *args):
    if not args:
      self.x, self.y = 0,0
    elif len(args) == 2:
      self.x, self.y = args[0], args[1]
    elif hasattr(args[0], 'get_center'):
      self.set(args[0].get_center())
    else:
      self.set(args[0])
#

if __name__ == "__main__":
  from jca import stubs
  
  def new_stub(args):
    return stubs.make_stub(__file__, args=args)
  point = new_stub([])
  print point
  print new_stub([point])
  print new_stub([10,10])