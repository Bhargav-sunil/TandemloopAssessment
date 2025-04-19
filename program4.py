# Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
#   (examples)
#   input: [1,2,8,9,12,46,76,82,15,20,30]
#   Output: 
#     {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

input_ = input("Enter input: ")[1:-1]
input_list = list(map(int,input_.split(',')))


dict_ = {i:0 for i in range(1,10)}

for num in range(1,10):
    for i in input_list:
        if  i % num == 0:
            dict_[num] += 1

print(dict_)