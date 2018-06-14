"""
Write a function that returns both the minimum and maximum number of the given list/array.
"""

def min_max(lst):
  lst.sort()
  return [lst[0], lst[-1]]
