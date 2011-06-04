
from my_test import *

def scaled_points(lines, width, height):
  # Store the min value, max value and scale for each dimension.
  if not lines:  return
  class Dimension:  pass
  dims = x_dim, y_dim = Dimension(), Dimension()
  for x_vals_y_vals in lines:
    for vals, dim in zip(x_vals_y_vals, dims):
      for val in vals:
        if not hasattr(dim, 'min') or val < dim.min:  dim.min = val
        if not hasattr(dim, 'max') or val > dim.max:  dim.max = val
  for dim in dims:
    additional = (dim.max - dim.min) * .10
    dim.min, dim.max = dim.min - additional, dim.max + additional
  y_dim.max, y_dim.min = y_dim.min, y_dim.max
  x_dim.scale, y_dim.scale = width, height

  # Map the real coordinates to widget coordinates.
  sc_lines = []
  for x_vals_y_vals in lines:
    sc_line = []
    for vals, dim in zip(x_vals_y_vals, dims):
      sc_vals = []
      for val in vals:
        total_delta = dim.max - dim.min
        if total_delta == 0:  val = 0
        else:  val = (val - dim.min) / total_delta * dim.scale
        sc_vals.append(val)
      sc_line.append(sc_vals)
    sc_lines.append(sc_line)
  return sc_lines, dims
  
if __name__ == '__main__':
  print scaled_points(test_lines, 100, 100)