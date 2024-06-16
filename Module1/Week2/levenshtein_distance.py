def levenshtein_distance_with_operations(str1, str2):
    m, n = len(str1), len(str2)

    # Tạo một bảng (ma trận) với kích thước (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    operations = [[[] for _ in range(n + 1)] for _ in range(m + 1)]

    # Khởi tạo giá trị cho hàng đầu tiên và cột đầu tiên
    for i in range(1, m + 1):
        dp[i][0] = i
        operations[i][0] = operations[i-1][0] + \
            [(f"xóa '{str1[i-1]}' từ vị trí {i-1}")]

    for j in range(1, n + 1):
        dp[0][j] = j
        operations[0][j] = operations[0][j-1] + \
            [(f"chèn '{str2[j-1]}' vào vị trí {j-1}")]

    # Điền giá trị vào bảng và theo dõi các thao tác
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                operations[i][j] = operations[i - 1][j - 1]
            else:
                insertion = dp[i][j - 1] + 1
                deletion = dp[i - 1][j] + 1
                substitution = dp[i - 1][j - 1] + 1

                min_cost = min(insertion, deletion, substitution)
                dp[i][j] = min_cost

                if min_cost == insertion:
                    operations[i][j] = operations[i][j - 1] + \
                        [(f"chèn '{str2[j-1]}' vào vị trí {j-1}")]
                elif min_cost == deletion:
                    operations[i][j] = operations[i - 1][j] + \
                        [(f"xóa '{str1[i-1]}' từ vị trí {i-1}")]
                else:
                    operations[i][j] = operations[i - 1][j - 1] + \
                        [(f"thay '{str1[i-1]}' bằng '{str2[j-1]}' tại vị trí {i-1}")]

    # Khoảng cách Levenshtein là giá trị ở góc dưới bên phải của bảng
    distance = dp[m][n]
    ops = operations[m][n]

    return distance, ops


str1 = "hola"
str2 = "hello"
distance, operations = levenshtein_distance_with_operations(str1, str2)
print(f"Khoảng cách Levenshtein giữa '{str1}' và '{str2}' là {distance}")
print("Các thao tác biến đổi cần thiết là:")
for op in operations:
    print(op)
