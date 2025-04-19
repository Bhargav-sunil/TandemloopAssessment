# Problem-3: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5
#     5) input a = 5, then output : 1, 3, 5, 7, 9
#     6) input a = 6, then output : 1, 3, 5, 7, 9
#     .
#     .
#     7) input a = x, then output : 1, 3, 5, 7, .......

input_ = int(input("Enter a number: "))

result = []
count = 1

for i in range(1,2 * input_, 2):
    result_2 = result.copy()
    if count % 2 != 0:
        result.append(str(i))
        print(", ".join(result))
    else:
        result.append(str(i))
        print(", ".join(result_2))

    count += 1
    