N, K = map(int, input().split())
people = list(range(1, N + 1))
result = []
index = 0

while people:
    # 현재 리스트에서 K번째 사람을 제거
    index = (index + K - 1) % len(people)  # 순환구조로 인덱스 조정
    result.append(people.pop(index))  # K번째 사람 제거하고 결과에 추가

print("<", ", ".join(map(str, result)), ">", sep="")
