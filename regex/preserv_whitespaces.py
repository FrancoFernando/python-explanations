import re

def test_preserve():
  s = " my  favourite color   is red"
  l = re.split(r'(\s+)', s)
  print(l)
  capitalized = ''.join(w.capitalize() for w in l)
  print(capitalized)
