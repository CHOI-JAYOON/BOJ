#include <stdio.h>

int main() {
	int N;
	int i;
	scanf("%d", &N);

	for (i = 2; i * i <= N; i++) {
		if (N % i == 0) {
			printf("%d\n", i);
			N /= i;
			--i;
		}
	}
	if (N > 1) {
		printf("%d\n", N);
	}
	return 0;
}