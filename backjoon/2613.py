# My Turn
N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
start = max(nums)
end = sum(nums)
group = []
ans = 0

while True:
    if start > end:
        break
    
    mid = (start + end) // 2 # mid는 최대값

    # 최댓값으로 그룹을 나누는 로직
    group_cnt = 0

    idx = 0
    group = []
    while idx < N:
        sub_sum = 0
        sub_count = 0

        while idx < N and sub_sum + nums[idx] <= mid:
            sub_sum += nums[idx]
            sub_count += 1
            idx += 1
            if M - group_cnt == N - (idx - 1):
                break 
        group_cnt += 1
        group.append(sub_count)

    if group_cnt <= M: # 그룹이 적으면 최댓값을 줄인다
        end -= 1
    else: # 그룹이 많으면 최댓값을 높인다.
        start += 1
    ans = mid

print(ans)
for i in group:
    print(i, end=" ")