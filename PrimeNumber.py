def prime_number():
  """素数を求める

  10000以下の素数リストを作成する

  """
  primes = list(range(2, 10000))
  for i in primes:
    for j in primes:
      if (j>i) and (j%i == 0):
        primes.remove(j)
  return primes

if __name__ == '__main__':
  print(prime_number())
