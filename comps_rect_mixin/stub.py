
class Stub:
  def __init__(self):
    self.left_, self.top_, self.right_, self.bottom_ = (100,100,200,200)
      
  def left(self): return self.left_
  def top(self): return self.top_
  def right(self): return self.right_
  def bottom(self): return self.bottom_
  
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
  
  def set_left(self, left): 
    self.right_ = left + self.width()
    self.left_ = left
    return self
  def set_top(self, top):
    self.bottom_ = top + self.height()
    self.top_ = top
    return self
        
  def set_indep(self, dir_string, new_val):
    setattr(self, dir_string + "_", new_val)
    
  def set_bounds(self, *args):
    self.left_,self.top_,self.right_,self.bottom_ = args    
    
  def width(self):
    return self.right() - self.left()
  def height(self):
    return self.bottom() - self.top()    
  def x_center(self):
    return (self.left() + self.right()) / 2
  def y_center(self):
    return (self.top() + self.bottom()) / 2    
  def center(self):
    return [self.x_center(), self.y_center()]    
  def xywh(self):
    return [self.left(), self.top(), self.width(), self.height()]
  def bounds(self):
    return [self.left(), self.top(), self.right(), self.bottom()]
  ltrb = bounds    
  def __repr__(self):  return unicode(self.bounds())
  
if __name__ == "__main__":
  stub = Stub()
  stub.set_bounds(0,0,100,100)
  print stub.center()