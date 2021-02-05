#include <stdio.h>

int main() {
	int M, N;
	int i,j;
	int a[1000001] = { 0,};

	scanf("%d %d", &M, &N);

	for (i = 2; i <= N; i++) {
		for (j = 2; i*j <= N; j++) {
			a[i*j] = 1;
		}
	}
	for (i = M; i <= N; i++) {
		if (!a[i])
			printf("%d\n", i);
	}
	return 0;
}