#find Mode
n=int(input())
mylist=input().split()
for i in range(n):
    mylist[i]=int(mylist[i])
maxCount=0
maxEle=mylist[0]
for currEle in mylist:
    currCount=0
    for eachEle in mylist:
        if eachEle==currEle:
            currCount += 1
    if currCount > maxCount:
        maxCount= currCount
        maxEle=currEle
print("Mode",maxEle,"MaxCount",maxCount)
