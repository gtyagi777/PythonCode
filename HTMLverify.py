from Stack import Stack

def is_matched(raw):
    S = Stack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>',j+1) 
        if k ==-1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.isEmpty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<',k+1)
    return S.isEmpty()


x = input()
print(is_matched(x))