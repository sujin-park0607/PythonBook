'''[문자열 재정렬]'''
import sys

input = sys.stdin.readline

input_str = input().rstrip()
sorted_input = sorted(input_str)

sum = 0
char_list = []
for s in sorted_input:
    if s.isdigit():
        sum += int(s)
        # sorted_input.remove(s) --- 리스트를 돌면서 처리하는 경우, 요소를 제거하면 리스트의 길이와 인덱스가 바뀌어 문제 발생.
    else:
        char_list.append(s)

sorted_char = ''.join(map(str, sorted(char_list)))

print(f"{sorted_char}{sum}")
