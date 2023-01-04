import sys
import random
import Gsd

def gsd_RandomRepeat(r = 10):
  """最大公約数を繰り返し算出する

  ランダムで選出した2つの整数に対し、最大公約数を求める

  Args:
      r (int, optional): 繰り返す回数
  """
  for i in range(r):
    a = random.randrange(1000)
    b = random.randrange(1000)
    print(f'a:{a} b:{b}')
    print(f'gsd:{Gsd.gsd(a,b)}')

# コマンドライン呼び出し
if __name__ == "__main__":
  args = sys.argv
  if len(args) < 2:
    gsd_RandomRepeat()
  else:
    gsd_RandomRepeat(int(args[1]))
