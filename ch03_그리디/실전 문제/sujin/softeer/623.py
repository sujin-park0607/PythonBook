# 비밀메뉴
import sys

input = sys.stdin.readline
m, n, k = map(int, input().split(" "))

m_array = list(map(int, input().split(" ")))
n_array = list(map(int, input().split(" ")))

secret = False
for i in range(n-m+1):
    print("i=========", i)
    if n_array[i] == m_array[0]:
        print("hihi")
        for j in range(len(m_array)):
            print("n_array, m_array: ", n_array[i+j], m_array[j])
            if n_array[i+j] == m_array[j]:
                secret = True
            else:
                secret = False
    else:
        continue

if secret: print("secret")
else: print("normal")

            
    
    