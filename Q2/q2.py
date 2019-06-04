def func(a, b, *args, **keywords):
    print(a, b)
    for arg in args:
        print(f'arg = {arg}')
    for key in keywords:
        print(f'key = {key} & value = {keywords[key]}')

if __name__ == '__main__':
    func(12, 45, 4, 35, 6, d=65, f=13)
# 12 45
# arg = 4
# arg = 35
# arg = 6
# key = d & value = 65
# key = f & value = 13
