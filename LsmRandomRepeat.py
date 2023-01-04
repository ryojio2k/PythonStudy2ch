import sys
import Lsm
import random

def lsm_random_repeat():
  """最小公倍数をランダムで求め続ける

  ランダムで生成した整数2つを用いて最小公倍数を求め続ける
  最小公倍数が2桁以下になった場合は停止
  """
  while 1:
    a = random.randrange(2, 100)
    b = random.randrange(2, 100)
    value = Lsm.lsm(a, b)
    print(f'a:{a} b:{b} value:{value}')
    if value < 100:
      break

if __name__ == '__main__':
  lsm_random_repeat()