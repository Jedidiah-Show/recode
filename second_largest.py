import sys

def step(largest, second_largest, x) -> (int, int):
    if x > largest:
        largest = x
    elif x < largest and x > second_largest:
        return largest, x
    return largest, second_largest
    
def second_largest(nums):
    if len(nums) <=1:
        return
    largest, second_largest = nums[0], -sys.maxsize - 1
    for num in nums:
        largest, second_largest = step(largest, second_largest, num)
    return second_largest

    largest, second_largest = reduce(step(largest,second_largest,larh))

print(second_largest([10, 5, 8, 20, 15]))
print(second_largest([10, 22, 22, 18, 17, 14, 18]))
print(second_largest([4, 9, 2, 9, 7]))
