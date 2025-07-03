import sys

file_path = sys.argv[1]

with open(file_path, 'r') as f:
    nums = [int(line.strip()) for line in f if line.strip()]

nums.sort()
n = len(nums)
median = nums[n // 2] if n % 2 == 1 else nums[n // 2]
moves = sum(abs(num - median) for num in nums)
print(moves)