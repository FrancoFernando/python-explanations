from collections import namedtuple

def test_namedtuple():
  Point = namedtuple('Point','x,y')
  A = Point(1,3)
  B = Point(2,4)
  dot_product = (A.x * B.x) + (A.y * B.y)
  print(dot_product) #14
