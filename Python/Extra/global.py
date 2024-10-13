c = 258
print('id of global c: ', id(c))

def test():
  global c
  print('before id of local c: ', id(c))
  c = 258
  print('after id of local c: ', id(c))
  #print(c)

test()
print('id of global c after func call: ', id(c))
#print(c)
