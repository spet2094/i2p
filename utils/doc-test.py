def square(x):
  """Return the square of x.
  >>> square(2)
  4
  >>> square(-2)
  4
  >>> square(-3)
  6
  """
  return x * x

print("Printing")

if __name__ == '__main__':
  import doctest
  print("In main")
  doctest.testmod()
