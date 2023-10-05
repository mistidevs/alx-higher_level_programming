import magic_calculation

def magic_calculation(a, b):
  """Performs a magic calculation on two numbers.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The result of the magic calculation.
  """

  add = magic_calculation.add
  sub = magic_calculation.sub

  if a < b:
    c = add(a, b)
    for i in range(4, 6):
      c = add(c, i)
    return c
  else:
    return sub(a, b)

