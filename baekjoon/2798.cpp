#include <stdio.h>

int main() {
	int N, M;
	int i,j,k;
	int sum = 0;
	int max = 0;
	int arr[101] = { 0 };

	scanf("%d %d", &N, &M);
	for (i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	for (i = 0; i < N; i++) {
		for (j=i + 1; j < N; j++) {
			for (k = j + 1; k < N; k++) {
				sum = arr[i] + arr[j] + arr[k];
				if (sum > max && sum <= M) {
					max = sum;
				}
			}
		}
	}
	printf("%d", max);
	return 0;
}