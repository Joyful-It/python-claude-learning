first_line = input().split()
n = int(first_line[0])
m = int(first_line[1])
T = int(first_line[2])

collectors = []
for _ in range(n):
    treasure_line = list(map(int, input().split()))
    collectors.append(treasure_line)

for _ in range(T):
    op_line = input().split()
    op = int(op_line[0])
    
    if op == 1:
        x = int(op_line[1]) - 1
        a = int(op_line[2]) - 1
        b = int(op_line[3]) - 1
        collectors[x][a], collectors[x][b] = collectors[x][b], collectors[x][a]
    
    else:
        x = int(op_line[1]) - 1
        res = collectors[x].pop(0)
        print(res)