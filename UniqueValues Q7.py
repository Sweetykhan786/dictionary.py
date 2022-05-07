dic=[
{"first":"1"}, 
{"second": "2"}, 
{"third": "1"}, 
{"four": "5"}, 
{"five":"5"}, 
{"six":"9"},
{"seven":"7"}
]
a=[]
for i in range (len(dic)):
    for j in dic[i]:
        if dic[i][j] not in a:
            a.append(dic[i][j])
print(a)