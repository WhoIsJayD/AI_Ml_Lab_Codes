nums = [2, 3, 4, 6, 8, 9, 1]
sum = 0
sumv = 0
n = len(nums)
for x in nums:
    sum += x
mean = sum / n
for i in range(len(nums)):
    diff = nums[i] - mean
    sumv += (diff * diff)
varrr = sumv / n
print(varrr)
