A = list(map(int,input().split()))
max_element = max(A)
total_time = 0
for num in A:
    total_time += max_element - num
print(total_time) 
