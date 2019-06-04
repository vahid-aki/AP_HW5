def Func(input_nums):
    dict1 = {}
    n, a, j = 0, 0, 0
    for i in input_nums:
        if i == ' ':
            dict1[n] = input_nums[a:j]
            a = j+1
            n += 1
        j += 1
        if j == len(input_nums):
            dict1[n] = input_nums[a:j]

    k = 0
    dict = {}
    for i in range(n+1):
        if (i+1)%6 == 0:
            if int(dict1[i])%6 == 0:
                dict[k] = int(dict1[i])
                k +=1

    dict = sorted(dict.values())

    list = []
    for i in range(len(dict)):
        if dict[i] not in dict[i+1:]:
            list.append(dict[i])

    output_nums = ""
    for i in range(len(list)):
        output_nums += str(list[i]) + ' '

    return output_nums

if __name__ == '__main__':
    input_nums = input("enter the numbers: ")
    print(f'output num(s): {Func(input_nums)}')
