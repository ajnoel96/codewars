"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
"""

def filter_list(l):
  ans = []
  for x in l:
    if isinstance(x, int):
      ans.append(x)
  return ans
