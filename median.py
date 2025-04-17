#find Median
num=int(input("Enter the number"))
mylist= list(map(int, input().split()))
mylist.sort()
if num % 2 == 1:
    print(mylist[num // 2])
else:
    ele1=mylist[num//2-1]
    ele2=mylist[num//2]
    print((ele1 + ele2) /2)
    print(mylist)
