from functools import reduce

# forとrangeによる算出
forsum = 0
for i in range(1,51):
  forsum += i
  print('i:',i,'forsum:',forsum)

# sumとrangeによる算出
print('sum:',sum(range(1,51)))

# generator式
print('generator:',sum(x for x in range(1, 51)))

# reduce
# functools.reduce(function, iterable, option initializer)
print('reduce:',reduce(lambda x,y: x+y, range(1,51)))