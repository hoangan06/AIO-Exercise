def words_count(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    result = {}
    for line in data:
        line = line.lower().split()
        for i in range(len(line)):
            result.setdefault(line[i], 0)
            result[line[i]] += 1
    return result


file_path = 'P1_data.txt'
result = words_count(file_path)
print(result['man'])
