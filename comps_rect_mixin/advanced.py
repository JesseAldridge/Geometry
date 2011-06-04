
from jca.geometry import xy

from stub import Stub

class Advanced:
  def set2(self, attr_name, *args):
    attrs_to_funcs = {"top_left":[self.set_left, self.set_top],
              "bottom_right":[self.set_right, self.set_bottom],
              "center":[self.set_x_center, self.set_y_center],
              "move":[lambda x:self.set_left(self.left() + x),
                  lambda y:self.set_top(self.top() + y)]}
    x_func, y_func = attrs_to_funcs[attr_name]
    x_val, y_val = xy.extract(*args)
    x_func(x_val)
    y_func(y_val)
    return self
  
  def enlarge(self, amount):
    self.set_indep("left", self.left() - amount)
    self.set_indep("top", self.top() - amount)
    self.set_indep("right", self.right() + amount)
    self.set_indep("bottom", self.bottom() + amount)
    return self
  expand = enlarge

  def __repr__(self):
    bounds = self.bounds()
    s = "<%s: " % self.__class__.__name__
    for bound in bounds:
      str_bound = unicode(round(bound))[:-2]
      s += str_bound + ', '
    s = s[:-2] + ">"
    return s

if __name__ == "__main__":  
  class MyStub(Advanced, Stub):  pass
  stub = MyStub()
  for s, x, y in [("top_left", 100, 100), ("bottom_right", 100, 100),
                  ("center", 100, 100), ("move", 10,10)]:
    print stub.set2(s, x, y)
  print stub.expand(10)