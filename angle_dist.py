
import angles

def angle_dist(ang1, ang2):
  """ Return the shortest distance between the two angles """
  angle = abs(ang1 - ang2) % 360
  
  if angle > 180:
    angle = 360 - angle;
    
  return angle

def angle(a, b):
  return angle_dist(a.angle(), b.angle())

if __name__ == "__main__":
  import point
  
  print angle_dist(30, 60)
  print angle_dist(350, 10)
  p = point.Point
  print angle(p(1,0), p(0,1))
  print angle(p(100,100), p(200,100))