## 문제
## 가운데를 기점으로 양 문자열의 합이 같으면 LUCKY 출력 nor READY

n = int(input())
condition = input()

print(n//2)
left = sum(list(map(int,condition[:n//2])))
right = sum(list(map(int,condition[n//2:])))

if left == right :
    print("LUCKY")
else :
    print("READY")