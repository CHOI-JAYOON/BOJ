#include <stdio.h>

int main() {
	int N;
	int arr[1000];
	int i;
	int sum = 0;
	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		scanf("%1d", &arr[i]);
	}
	for (i = 0; i < N; i++) {
		sum += arr[i];
	}
	printf("%d", sum);
	return 0;
}