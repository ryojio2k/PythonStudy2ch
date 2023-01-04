import sys
import Gcd
import random

def lsm(a, b):
  """最小公倍数を求める

  最小公倍数lsm(a,b)は、最大公約数gcd(a,b)に対し
  lsm(a,b) * gcd(a,b) = ab
  つまり、最大公約数を使った最小公倍数は下記で求められる
  lsm(a,b) = ab / gcd(a,b)

  Args:
      a (int): 自然数
      b (int): 自然数
  """
  return int(a*b / Gcd.gcd(a, b))


# コマンドライン起動
if __name__ == '__main__':
  args = sys.argv
  a = random.randrange(2, 100)
  b = random.randrange(2, 100)
  if len(args) > 2:
    a = int(args[1])
    b = int(args[2])
  
  print(f'a:{a} b:{b} lsm:{lsm(a, b)}')