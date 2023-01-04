import sys

DEBUG = 0

def gsd(a, b):
  """最大公約数を求める

  ユークリッドの互除法を用いて、再帰的に最大公約数を求める

  Args:
      a (int): 被除算対象
      b (int): 除数(0の場合はaが最大公約数となる)
  """
  # デバッグ出力
  if DEBUG:
    print("gsd(",a,b,")")

  # 除算値が0の場合
  if(b == 0):
    # 最大公約数はa
    return a
  
  # 大小が逆転している場合
  if(b > a):
    # 反転してやり直す
    return gsd(b, a)

  # 除算の余りを算出
  div = a / b
  mod = a % b

  # 再起呼び出し
  return gsd(b, mod)

# コマンドライン呼び出し
if __name__ == "__main__":
  args = sys.argv
  if(len(args)) < 2:
    print('input error: Not enough input arguments.')
  else:
    print('gsd:', gsd(int(args[1]), int(args[2])))