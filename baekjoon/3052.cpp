#include <stdio.h>

int main() {
	int A,n,i;
	int count = 0;
	int arr[100] = { 0 };
	
	for (i = 0; i < 10; i++) {
		scanf("%d", &A);
		n = A % 42;
		arr[n]++;
	}
	for (i = 0; i < 100; i++) {
		if (arr[i] != 0) {
			count++;
		}
	}
	printf("%d", count);
	return 0;
}