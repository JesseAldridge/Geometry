
from jca import directions

import xy, dist

def nearest_edge(rects, *args):
  x,y = xy.extract(*args)
  
  class Result:
    min_dist = nearest_rect = nearest_edge = None

  result = Result()

  for rect in rects:
    edge = directions.west
    for midpoint in rect.midpoints():
      d = dist.dist([x,y], midpoint)
      if result.min_dist == None or d < result.min_dist:
        result.min_dist = d
        result.nearest_rect = rect
        result.nearest_edge = edge
      edge += 1
  return result
#

if __name__ == "__main__":
  import rect
  
  print nearest_edge([rect.Rect()], [1,10]).nearest_edge