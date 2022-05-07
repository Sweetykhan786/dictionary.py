# "Using while loop"
# l="MISSISSIPPI"
# a=list(l)     
# i=0
# b=[]
# while i<len(a):
#     j=0
#     b1=[]
#     count=0
#     while j<len(a):
#         if a[i] in a:
#             if a[i]==a[j]:
#                 count+=1
#             j+=1
#     b1.append(a[i])
#     b1.append(count)
#     if b1 not in a:
#         b.append(b1)
#     i+=1
# print(dict(b))

# "Using for loop"
# a=list(l)
# c={}
# for i in a:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1
# print(c)


    
    
    
# a={1:10,2:20,3:30}
# b=a.pop(1)  
# print(a)


a={"sum":{1:3,
          2:6,
          3:9,
          4:12
          }
}
key=int(input("Enter key: "))
value=int(input("Enter value: "))
for i,j in a.items():
    for k in j:
        if k==key:
            j[k]+=value
            print(a)
    

            
# a={"sum":{'a':'Hi',
#           'b':'my name',
#           'c':'is',
#           'd':'Sanjna'}
#    }
# for i,j in a.items():
#     for k in j:
#         print(j[k],end=" ")
#     print()

# a={'kuch':30,'No':50,'Yes':'No'}
# v=a
# print(v)
# c=v.pop('kuch')
# b=a
# print(a)

# p
# c=a
# del c['No']
# print(c)


