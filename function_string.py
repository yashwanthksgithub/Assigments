w= input('enter a string :\n')
d = dict()

def most_frequent(string):
#    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1      
    return d

dic2=dict(sorted(most_frequent(w).items(),key= lambda x:x[1]))

res =dict(reversed(list(dic2.items())))
print(res)
