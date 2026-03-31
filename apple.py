print("please enter apple of amount")
n= int(input())
if n==0:
    print(0,0)
else:
    apples=list(range(1,n+1))
    day=0
    target_day=0

    while apples:
        day+=1
        
        index_num=list(range(0,len(apples),3))
        for i in reversed (index_num):
            removed_num=apples.pop(i)
            if removed_num == n and target_day == 0:
                target_day=day

    print(day,target_day)





   