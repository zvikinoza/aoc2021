
def count_increasing(nums) -> int:
    prev = float('inf')
    count = 0
    for num in nums:
        if prev < num:
            count += 1
        prev = num
    return count


def part_one(input_file):
    with open(input_file, 'r') as f:
        prev = float('inf')
        count = 0
        for num in map(int, f.readlines()):
            if prev < num:
                count += 1
            prev = num
        return count

# print(part_one('input.txt'))

def part_two(input_file):
    with open(input_file) as f:
        count = 0
        nums = list(map(int, f.readlines()))
        for i in range(3, len(nums)):
            # print(nums[i], type(nums[i]), nums[i-3], type(nums[i-3]))
            if nums[i] > nums[i - 3]:
                count += 1
        return count

print(part_two('input.txt'))