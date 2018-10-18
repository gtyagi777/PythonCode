def retTrue(strings, expressions):
    xx = False;
    for i in list(strings):
        if xx == False:
            xx= eval("i" +"." + expressions)
    return xx



if __name__ == '__main__':
    s = input()
    print(retTrue(s,"isalnum()"))
    print(retTrue(s,"isalpha()"))
    print(retTrue(s,"isdigit()"))
    print(retTrue(s,"islower()"))
    print(retTrue(s,"isupper()"))