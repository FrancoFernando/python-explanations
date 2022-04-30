from collections import OrderedDict 

def test_orderddict():
  dict = OrderedDict() 
  dict['a'] = 1
  dict['b'] = 2
  dict['c'] = 3
  dict['d'] = 4

  for key, value in dict.items(): 
      print(key, value) 
  # a 1 b 2 c 3 d 4  
  dict['c'] = 5
  for key, value in dict.items(): 
      print(key, value)
  # a 1 b 2 c 5 d 4 
