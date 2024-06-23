def count_chars(string):
    result = {}
    for i in range(len(string)):
        result.setdefault(string[i], 0)
        result[string[i]] += 1
    return result


string = 'smiles'
print(count_chars(string))
