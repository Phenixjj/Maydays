def add:
  return lambda x, y: x + y

def fib(x):
  if x == 0:
    return 1
  else:
    p = x - 1
    if p == 0:
      return 1
    else:
      return fib(p) + fib(p - 1)

def main():
  return fib(30)