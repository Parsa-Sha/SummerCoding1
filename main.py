# Algorithm Design - Write an efficient algorithm to find the maximum sum of contiguous subarray within a one-dimensional array of numbers.

import numpy as np

def main():
  array = [-384, -14, 162, -467, 1000, -5, 238,  -961, -761, 6, 100]
  barray = float('-inf')

  for i in range(len(array)):
    for j in range(i+1, len(array)+1):
      if barray < np.sum(array[i:j]):
        barray = np.sum(array[i:j])

  return print(barray)

main()