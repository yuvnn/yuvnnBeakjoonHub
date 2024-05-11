#include <stdio.h>
#include<stdlib.h>

int main() {
	int i, j, N, color = 1;
	scanf("%d", &N);
	int* ans = (int*)calloc(N+1, sizeof(int)); 
	ans[1] = 1;
	for (i = 2; i <= N; i++) {
		if (ans[i] != 0) continue;
		color++;
		for (j = i; j <= N; j += i) {
			ans[j] = color;
		}
	}
	printf("%d\n", color);
	for (i = 1; i <= N; i++) {
		printf("%d ",ans[i]);
	}
}
