def esprimo (num):
    if (num == 1):
        res = False
    else:
        res = True
        for i in range (2,num):
            if num % i == 0:
                res = False
                break
    return res

if __name__ == "__main__":
    num = int(input("tell me a number: "))
    res = esprimo(num)
    if (res):
        print ("Terrible primo")
    else:
        print("not primo") 