def twosum(nums, target):
    seen = {}

    for i in range(len(nums)):
        diff = target -nums[i]
        if nums[i] not in seen:
            seen[nums[i]] = i
        if diff not in seen:
            continue
        return [seen[diff], i]
    return []
    
print(twosum([2, 7, 11, 15], 9))
print(twosum([3, 5, 1, 6, 8], 11))
print(twosum([8, 9, 0, 1], 9))


