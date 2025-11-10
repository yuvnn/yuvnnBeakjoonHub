n, k = map(int, input().split())
dp = [0] * (k + 1)  # DP 테이블 크기 수정

for _ in range(n):
    w, v = map(int, input().split())  # 입력 순서 수정 (무게 W 먼저, 가치 V 나중)
    
    # DP 배열을 뒤에서부터 업데이트 (역순 순회)
    for j in range(k, w-1, -1):  
        dp[j] = max(dp[j], dp[j-w] + v)  

print(dp[k])  # 최대 가치 출력
