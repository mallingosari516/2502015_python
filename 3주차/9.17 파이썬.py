'''
for y in range(5):
    for x in range(10):
        print("*", end="")
    print("#")
'''
'''
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")
'''

#continue는 3일 때 aaa가 출력되지 않음
'''
for i in range(10):
    if i % 3==0:
        continue
    else:
        print(i)
    print("aaa")
'''

#pass 일 때는 3일때도 aaa가 출력
for i in range(10):
    if i % 3==0:
        pass
    else:
        print(i)
    print("aaa")
