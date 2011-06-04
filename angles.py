""" Angles should be in degrees """

import angle_dist

def wrap_angle(angle):
  angle %= 360
  if angle < 0:
    angle += 360
  return angle

def rotate_clockwise(angle, rot_amount):
  angle -= rot_amount
  return wrap_angle(angle)

def rotate_counterwise(angle, rot_amount): 
  return rotate_clockwise(angle, -rot_amount)

def is_1_clockwise_from_2(ang1, ang2):
  return angle_dist.angle_dist(ang1, ang2) < 0

def is_1_counterwise_from_2(ang1, ang2):
  return angle_dist.angle_dist(ang1, ang2) > 0
  
def clockwise(angle): return -angle
def counterwise(angle): return angle
  

if __name__ == "__main__":
  print wrap_angle(361)
  print rotate_clockwise(60, 5)
  print rotate_counterwise(60, 5)
  assert is_1_clockwise_from_2(60, 70)
  assert is_1_counterwise_from_2(60, 45)
  