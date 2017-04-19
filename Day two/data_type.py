def data_type(n):
  if isinstance(n, str):
    return len(n)
  elif isinstance(n, bool):
    return n
  elif isinstance(n, int):
    if n == 100:
      return 'equal to 100'
    elif n > 100:
      return 'more than 100'
    elif n < 100:
      return 'less than 100'
  elif isinstance(n, list):
    return n[2] if -len(n) <= 2 < len(n) else None
  elif n is None:
    return 'no value'