#include <stdio.h>
#include <string.h>

long long a, b, c, ans;
long long rec(long long A, long long B, long long C ) {
	if (B == 1) return A % C;
	else {
		long long k = rec(A, B / 2, C);
		if (B % 2 == 1) return (k * k ) % C * A % C;
		else return (k * k) % C;
	}
	
}
int main() {

	scanf("%lld %lld %lld",&a,&b,&c);
	printf("%lld", rec(a,b,c));

	return 0;
}