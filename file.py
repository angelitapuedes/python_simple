with open('test.txt', 'r') as f:
    f.contents = f.readline()
    print(f.contents)