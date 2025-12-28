def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    count_zeros = 0
    # list of non-zero elements
    nz=[]
    for i in nums:
        if i==0:
            count_zeros+=1
            continue
        nz.append(i)
    # print(nz)

    # list of zero elements
    zeros = [0]*count_zeros
    nz.extend(zeros)

    # for i in range(count_zeros):
    #     nz.append(0)
    return nz


# nums = [0, 1, 0, 3, 12]
# nums = [0, 0, 1]
nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
print(move_zeroes(nums))