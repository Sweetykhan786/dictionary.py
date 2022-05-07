dic={}
for i in range(1,11):
    name=input("Enter name of students: ")
    marks=int(input("Enter marks: "))
    dic.update({name:marks})
print(dic)