
import shape, point

class Polygon(shape.Shape):
  def __init__(self, points):
    self.points = [point.Point(p) for p in points]

  def polygon_interst
	public boolean polygon_intersect( List<? extends Point> myPoints,
			List<? extends Point> linePoints) {
	  for(int i = 0; i < myPoints.size(); i ++) {
	    // the end vertex of the edge

	    int j = (i+1); if (j == myPoints.size()) j = 0;

	    // a vector perpendicular to the edge,

	    // which defines a potential separation axis

	    Point p1 = myPoints.get(i),
	        p2 = myPoints.get(j);

	    Point N = new Moving_Point( p1.get_y() - p2.get_y(),
	    		p2.get_x() - p1.get_x() );

	    // the edge separates the polygons, they are therefore disjoint

	    if ( !spanOverlap(N, myPoints, linePoints) ) {
	      return false;
	    }
	  }

	  for(int i = 0; i < linePoints.size(); i ++) {
	    // the end vertex of the edge

	    int j = (i+1); if (j == linePoints.size()) j = 0;

	    // a vector perpendicular to the edge,

	    // which defines a potential separation axis

	    Point p1 = linePoints.get(i),
	    	  p2 = linePoints.get(j);

	    Moving_Point N = new Moving_Point( p1.get_y() - p2.get_y(),
	    		p2.get_x() - p1.get_x() );

	    // the edge separates the polygons, they are therefore disjoint

	    if ( !spanOverlap(N, myPoints, linePoints) )
	      return false;
	  }

	  // there are no possible lines that separates the triangles.

	  // they must intersect.

	  return true;
	}


  def is_point_in(self, p):
    n = len(self.points)
    inside = False

    p1x,p1y = self.points[0]
    for i in range(n+1):
      p2x,p2y = self.points[i % n]
      if y > min(p1y,p2y):
        if y <= max(p1y,p2y):
          if x <= max(p1x,p2x):
            if p1y != p2y:
              xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
            if p1x == p2x or x <= xinters:
              inside = not inside
      p1x,p1y = p2x,p2y

    return inside
#

if __name__ == "__main__":
  poly1, poly2 = [Polygon([[-1,1], [0,2], [1,1], [1,-1], [-1,-1]])
          for i in range(2)]
  print poly1.is_point_in(poly2)