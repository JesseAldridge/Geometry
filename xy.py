
import inspect

def extract(*args):
  if len(args) == 1:
    var = args[0]
    if hasattr(var, "x"):
      if callable(var.x):
        return var.x(), var.y()
      return var.x, var.y
    return var
  return args
#

if __name__ == "__main__":
  from PyQt4 import QtCore
  
  print extract((3,5))
  print extract(3,5)
  print extract(QtCore.QPoint(3,5))