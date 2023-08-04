#변속기

import sys
input = sys.stdin.readline

array = list(map(int, input().split(" ")))

ascending = False
descending = False
for i in range(1,len(array)):
    if array[i-1] + 1== array[i]:
        ascending = True
    else:
        descending = True

if ascending and descending:
    print("mixed")
elif ascending: print("ascending")
else: print("descending")