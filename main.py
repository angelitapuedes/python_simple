from calculator import add

def is_good(var):
    if var == 1:
        return True
    else:
        return False

def numbers():
    number = [-9, 1, 2, 3, 5, 7, 9, 20]
    print(number)
    number.sort()
    print("After sorted:" + str(number))
    number.reverse()
    print("After reverse:" + str(number))
    number.append(38)
    print("After append:" + str(number))
    number.clear()
    print("After I cleared the list:"+ str(number))

    


if __name__ == "__main__":  
    ans = is_good(2)
    x = 0
    for x in range(5,10):
        if x == 9:
            break
        if x % 2 == 1:
            print(str(x) + "is odd")
        else:
            print(str(x) + "is even")
        x = x + 1
    
    ans2 = numbers()
    print(add(5,5))