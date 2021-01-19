#include <stdio.h>

int main() {
	int A, B, C;
	int R,n,i;
	int arr[10] = {0, };
	scanf("%d %d %d", &A, &B, &C);
	R = A * B * C;
	while (R > 0) {
		n = R % 10;
		R = R / 10;
		arr[n]++;
	}
	for (i = 0; i < 10; i++) {
		printf("%d\n", arr[i]);
	}
	return 0;
}