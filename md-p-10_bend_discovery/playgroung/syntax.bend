def add:
  return lambda x, y: x + y

def sub(x, y):
  return x - y

def max(a, b):
  if a > b:
    return a
  else:
    return b

def main:
  return max(3, 2)