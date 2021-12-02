def part_one(input_file):
    with open(input_file, 'r') as f:
        depth, dist = 0, 0
        for line in f:
            dir, steps = line.split(' ')
            steps = int(steps)
            if dir == 'forward':
                dist += steps
            elif dir == 'up':
                depth -= steps
            elif dir == 'down':
                depth += steps
        return dist * depth

print(part_one('input.txt'))

def part_two(input_file):
    with open(input_file, 'r') as f:
        depth, dist, aim = 0, 0, 0
        for line in f:
            dir, steps = line.split(' ')
            steps = int(steps)
            if dir == 'forward':
                dist += steps
                depth += aim * steps
            elif dir == 'up':
                aim -= steps
            elif dir == 'down':
                aim += steps
        return dist * depth

print(part_two('input.txt'))