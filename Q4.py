n = input()
result = 0
# 0 제거

n = n.replace('0', '')

for i in range(len(n)):
    num = int(n[i])
    if i == 0:
        result += num    
    elif num == 1:
        result += 1
    else:
        result *= num
print(result)
