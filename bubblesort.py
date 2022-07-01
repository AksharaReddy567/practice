def bubblesort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if(list[j]>list[j+1]):
                list[j],list[j+1]=list[j+1],list[j]
    print(list)
n=int(input("enter number of elements:"))
list=[]
for i in range(0,n):
    list.append(int(input()))
bubblesort(list)
