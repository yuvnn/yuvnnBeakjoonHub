#include<stdio.h>
#include<stdlib.h>

int isPrimenum(int n) {
	if (n <= 1) return 0;
	if (n <= 3) return 1;
	else {
		for (int i = 2; i < n; i++) {
			if (!(n % i)) return 0;
		}
	}
	return 1;
}

int main() {
	int T,num,a,b;
	scanf("%d", &T);
	int* ans = (int*)malloc(2 * T * sizeof(int));

	int i = T;
	while (i--) {
		scanf("%d", &num);
		a = num / 2; 
		b = num / 2;
		if (!(T % 2)) b++;
		while (a) {
			if (isPrimenum(a) && isPrimenum(b)) {
				ans[i] = a;
				ans[i + T] = b;
				break;
			}
			else { a--; b++; }
		}
	}

	i = T;
	while (i--) {
		printf("%d %d\n", ans[i],ans[i+T]);
	}
}
