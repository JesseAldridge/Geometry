
west, north, east, south = 0,1,2,3
left, up, right, down = 0,1,2,3
top, bottom = 1,3

def string_to_dir(s):
  return {"west":west, "north":north, "east":east, "south":south,
      "left":left, "up":up, "right":right, "down":down,
      "top":top, "bottom":bottom}[s]

def dir_to_angle(dir):  return [180, 90, 0, 270][dir]

def apply_direction(coords, direction, num_rows, num_cols ):  
  r,c = coords
  offset_map = {west:[-1,0], north:[0,-1], east:[1,0], south:[0,1]}
  offset = offset_map[direction]
  r += offset[1]
  c += offset[0]
  return [wrap(val, max) for val, max in 
          zip([r, c], [num_rows, num_cols])]

def wrap(num, max):
  if num < 0:  num += max
  elif num >= max:  num -= max
  return num

if '__main__' == __name__:
  print "south index: ", string_to_dir("south")
  print "south degress: ", dir_to_angle(south)
  
  print apply_direction([1,1], west, 2, 2)
  print apply_direction([0,1], north, 2, 2)
