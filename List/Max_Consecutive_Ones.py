def find_max_consecutive_ones(nums):
  
  """
  Function to find the maximum number of consecutive 1's in a binary array.
  :param nums: List[int] -> A binary array where each element is either 0 or 1
  :return: int -> The maximum number of consecutive 1's
  """
  maxones = []
  maxlen = 0
  for i in nums:
    if i == 1:
        maxones.append(i)
        if len(maxones) > maxlen:
            maxlen = len(maxones)
    else:
        maxones.clear()
  return maxlen
  
# nums = [0, 0, 0, 0]
nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
# nums = [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1]
print(find_max_consecutive_ones(nums))