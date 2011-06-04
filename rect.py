
from jca.geometry import xy

from comps_rect_mixin import basics, advanced

class RectMixin(basics.Basics, advanced.Advanced):  pass
class Rect(RectMixin):
  def __init__(self, *args):
    if len(args) == 4:
      l,t,r,b = args
    elif len(args) == 2:
      if hasattr(args[0], "__int__"):
        l,t = 0,0
        r,b = args[0], args[1]
      l,t = xy.extract(args[0])
      r,b = xy.extract(args[1])
    elif len(args) == 1:
      other = args[0]
      if hasattr(other, "ltrb"):
        l,t,r,b = other.ltrb()
      elif hasattr(other, 'left'):
        l,t,r,b = (other.left(), other.top(), other.right(), other.bottom())
      else:
        self.__init__(*other)
        return
    else:
      l,t, r,b = 0,0, 20,20

    self.left_, self.top_, self.right_, self.bottom_ = l,t,r,b
    
    self.fill_color = (255, 255, 255)
    self.border_color = (0,0,0)

  def left(self): return self.left_
  def top(self): return self.top_
  def right(self): return self.right_
  def bottom(self): return self.bottom_
  def set_bounds(self, l,t,r,b):
    self.left_, self_top_, self.right_, self.bottom_ = l,t,r,b
    
  def set_left(self, left):
    self.right_ = left + self.width()
    self.left_ = left
    return self
  
  def set_top(self, top):
    self.bottom_ = top + self.height()
    self.top_ = top
    return self
  
  def set_left_indep(self, left):
    self.left_ = left
  def set_top_indep(self, top):
    self.top_ = top
  def set_right_indep(self, right):
    self.right_ = right
  def set_bottom_indep(self, bottom):
    self.bottom_ = bottom

if __name__ == '__main__':
  rect = Rect([40,40,50,50])
  for args in [(10,10, 20,20), [(20,20), (30,30)], [rect], []]:
    print Rect(args)
  print rect.set_left(10)
  print rect.set_top(100)