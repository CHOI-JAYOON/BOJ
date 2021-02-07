#include <stdio.h>
#include <math.h>

int main() {
	int N;
	int i,j;
	int sum = 0, res = 0;

	scanf("%d", &N);

	for (i = 1; i < N; i++) {
		sum = 0;
		for (j = 5; j >= 0; j--) {
			sum += (i / (int)pow(10, j) % 10);
		}
		sum += i;
		if (sum == N) {
			res = i;
			break;
		}
	}
	printf("%d", res);
	return 0;
}