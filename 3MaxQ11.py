my_dict={
'a':50, 
'b':58, 
'c':56,
'd':40, 
'e':100, 
'f':20
}
b=0
for i in my_dict:
    if my_dict[i]>b:
        b=my_dict[i]
        b1=0
        for j in my_dict:
            if my_dict[j]>b1 and my_dict[j]!=b:
                b1=my_dict[j]
                b2=0
                for k in my_dict:
                    if my_dict[k]>b2 and my_dict[k]!=b1 and my_dict[k]!=b:
                        b2=my_dict[k]
print([b,b1,b2])