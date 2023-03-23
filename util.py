
def array_flatten(array):
  """Function for flatten arrays of integers using 'function recursion'
  e.g from [1, [2, [3, [4, 5]]]] to [1, 2, 3, 4, 5]

  Parameters:
    array (list): Array of arrays
  Returns:
    result (list): Flatten list
  """
  if not isinstance(array, list):
    raise TypeError('array must be a list object')
  
  result = []
  for x in array:
    if isinstance(x, list):
      result.extend(array_flatten(x))
    elif isinstance(x, int):
      result.append(x)
    else:
      raise TypeError('The array values must be integers')
  return result