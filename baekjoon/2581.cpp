#include <stdio.h>

int main() {
	int M, N;
	int i,j;
	int flags;
	int count = 0;
	int sum=0;
	int min = 10000;
	scanf("%d", &M);
	scanf("%d", &N);

	for (i = M; i <= N; i++) {
		flags = 0;
		
		if (i == 1) {
			continue;
		}
		for (j = 2; j < i; j++) {
			if (i % j == 0) {
				flags = 1;
			}
		}
		if (flags == 0) {
			if (min > i) {
				min = i;
			}
			sum += i;
			count++;
		}
	}
	if (count == 0) {
		printf("-1");
	}
	else {
		printf("%d\n", sum);
		printf("%d", min);
	}
	

	return 0;
}