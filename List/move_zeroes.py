def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    # Step 1: Pointer for next non-zero position
    non_zero_pos = 0

    # Step 2: Move all non-zeros to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos] = nums[i]
            non_zero_pos += 1

    # Step 3: Fill the rest with zeros
    for i in range(non_zero_pos, len(nums)):
        nums[i] = 0
    return nums
            
    
            
        
# nums = [0, 1, 0, 3, 12]
# nums = [0, 0, 1]
nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
print(move_zeroes(nums))