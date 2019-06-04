import os

def create_dir(name, address):
    if os.path.isdir(os.path.join(address, name)):
        print('this directory has already exists.')
    else:
        os.mkdir(os.path.join(address, name))

def create_file(name, address):
    if os.path.isfile(os.path.join(address, name)):
        print('this file has already exists.')
    else:
        with open(os.path.join(address, name), 'w'):
            pass

def delete(name, address):
    if not os.path.isfile(os.path.join(address, name)):
        print("there isn't such file or directory.")
    else:
        os.remove(os.path.join(address, name))

ListOfDirs = []
def find(name, address):
    ListOfFiles = os.listdir(address)
    for entry in ListOfFiles:
        if os.path.isdir(os.path.join(address, entry)):
            find(name, os.path.join(address, entry))
        if os.path.join(address, name) == os.path.join(address, entry):
            ListOfDirs.append(os.path.join(address, name))


if __name__ == '__main__':
    path = os.getcwd()
    name1 = 'test.txt'
    # path = input ("enter the address: ")
    # name1 = input ("enter the file name: ")
    create_dir('new folder', os.getcwd())
    create_file('test.txt', os.path.join(os.getcwd(), 'new folder'))
    find(name1, path)
    print(ListOfDirs)
    delete('test.txt', os.path.join(os.getcwd(), 'new folder'))
