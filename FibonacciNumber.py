def fibonacci_number():
  """フィボナッチ数の表示

  フィボナッチ数を、2**31より小さい範囲まで表示する
  F0 = 0
  F1 = 1
  F(N+2) = F(N) + F(N+1)(N>-0)
  """
  fibs = []
  a = 0
  fibs.append(a)
  b = 1
  fibs.append(b)
  c = a+b
  while c < 2**31:
    fibs.append(c)
    a = b
    b = c
    c = a+b

  return fibs

def fibonacci_number2():
  """フィボナッチ数の表示(タプル使用)

  フィボナッチ数を、2**31より小さい範囲まで表示する
  Pythonのタプルを使って構成する
  """
  a, b = 0, 1
  fibs = []
  while a < 2**31:
    fibs.append(a)
    a, b = b, a+b
  
  return fibs


if __name__ == '__main__':
  print(fibonacci_number())
  print(fibonacci_number2())