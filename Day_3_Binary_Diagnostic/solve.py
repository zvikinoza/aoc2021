import operator

def part_one(input_file):
    with open(input_file) as f:
        count_ones = dict()
        file_len = 0
        for line in f:
            file_len += 1
            for i, c in enumerate(line):
                if c == '1':
                    count_ones[i] = count_ones.get(i, 0) + 1
        gamma = '0' * len(count_ones)
        epsilon = '0' * len(count_ones)
        for k, v in count_ones.items():
            if v >= file_len / 2:
                gamma = gamma[:k] + '1' + gamma[k+1:]
            else:
                epsilon = epsilon[:k] + '1' + epsilon[k+1:]
        return int(gamma, 2) * int(epsilon, 2)

print(f"First part's solution={part_one('input.txt')}")


def bit_criteria(input_file, comparator):
    with open(input_file) as f:
        most_common = [l.strip() for l in f.readlines()]
        i = 0
        while len(most_common) > 1:
            common = '1'
            n_common = sum(1 for l in most_common if l[i] == common)
            if comparator(n_common, len(most_common) / 2):
                common = '0'
            most_common = [line for line in most_common if line[i] == common]
            i += 1
        return int(most_common[0], 2)

def part_two(input_file):
    return bit_criteria(input_file, operator.lt) * bit_criteria(input_file, operator.ge)

print(f"Second part's solution={part_two('input.txt')}")