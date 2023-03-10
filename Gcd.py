import sys
import random

DEBUG = 0

def gcd(a, b):
  """最大公約数を求める

  ユークリッドの互除法を用いて、再帰的に最大公約数を求める

  Args:
      a (int): 被除算対象
      b (int): 除数(0の場合はaが最大公約数となる)
  """
  # デバッグ出力
  if DEBUG:
    print("gcd(",a,b,")")

  # 除算値が0の場合
  if(b == 0):
    # 最大公約数はa
    return a
  
  # 大小が逆転している場合
  if(b > a):
    # 反転してやり直す
    return gcd(b, a)

  # 除算の余りを算出
  mod = a % b

  # 再起呼び出し
  return gcd(b, mod)

# コマンドライン呼び出し
if __name__ == "__main__":
  args = sys.argv
  a = random.randrange(2, 1000)
  b = random.randrange(2, 1000)
  if(len(args)) > 2:
    a = int(args[1])
    b = int(args[2])

  print(f'a:{a} b:{b} gcd:{gcd(a, b)}')
