def twosum(nums, target):
    seen, diff = {}, 0

    for num in nums:
        diff= target -num
        if diff in seen:
            return diff
            
