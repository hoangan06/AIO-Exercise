def sliding_max(num_list, sliding_size):
    if (type(sliding_size) != int) or (sliding_size < 1) or (sliding_size > len(num_list)):
        return "Sliding size must be a positive integer, less than or equal to the length of num_list"
    result = []
    for i in range(len(num_list) - sliding_size + 1):
        result.append(max(num_list[i:i+sliding_size]))
    return result


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
sliding_size = 3
print(sliding_max(num_list=num_list, sliding_size=sliding_size))
