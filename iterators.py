import time
class prime():
  def __init__(self, max=None):
    self.max = max
    self.n = 2
    self.count = 0
  
  def __iter__(self):
    return self
  
  def __next__(self):
    temp = [i for i in range(2, self.n) if self.n % i == 0]
    aux = self.n

    if self.max:
      if self.count < self.max:
        if not temp:
          self.n += 1
          self.count += 1
          return aux
        else:
          self.n += 1
          return self.__next__()
      else:
        raise StopIteration
    else:
      if not temp:
          self.n += 1
          return aux
      else:
          self.n += 1
          return self.__next__()
      
res = prime()
for i in res:
  print(i)
  time.sleep(.5)