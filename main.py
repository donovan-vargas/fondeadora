import os

from util import array_flatten


message = "Welcome to the array flatten function: \n"
test_message = "To run all the test cases go \
to the shell -> \n and type 'python -m unittest'"

# change the next value as you want
array = [1, [2, [3, [4, 5]]]]

if __name__ == "__main__":
  print(message)
  print(array_flatten.__doc__)
  print(f"input: {array}")
  print(f"output: {array_flatten(array)}")
  print("\n")
  os.system("python -m unittest")
  print("\n")
  print(test_message)