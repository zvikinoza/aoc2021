
def part_one(input_file):
    with open(input_file, 'r') as f:
        prev = float('inf')
        count = 0
        for num in map(int, f.readlines()):
            if prev < num:
                count += 1
            prev = num
        return count

print(part_one('input.txt'))

def part_two(input_file):
    with open(input_file) as f:
        count = 0
        nums = list(map(int, f.readlines()))
        for i in range(3, len(nums)):
            if nums[i] > nums[i - 3]:
                count += 1
        return count

print(part_two('input.txt'))