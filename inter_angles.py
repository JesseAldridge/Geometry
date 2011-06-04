
import angles, angle_dist

def move_toward(curr_angle, target_angle, inc):
  if abs(angle_dist.angle_dist(target_angle, curr_angle)) < inc:
    return target_angle
  elif angles.is_1_clockwise_from_2(target_angle, curr_angle):
    return curr_angle + clockwise(inc)
  else:
    return curr_angle + angles.counterwise(inc)

def transist(start_angle, end_angle, t, max_t):
  if t >= max_t:
    return end_angle
    
  angle_dist_ = angle_dist.angle_dist(start_angle, end_angle)
  print "angle_dist: ", angle_dist_
  delta = (float(angle_dist_) / max_t * t)
  print "delta: ", delta
  return move_toward(start_angle, end_angle, delta)

if __name__ == "__main__":
  print move_toward(30, 60, 10)
  print transist(start_angle=30, end_angle=60, t=5, max_t=10)