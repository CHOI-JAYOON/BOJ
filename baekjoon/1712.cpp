#include <stdio.h>

int main() {
	long A, B, C;
	scanf("%ld %ld %ld", &A, &B, &C);
	int i=1;
	if (C <= B) {
		printf("-1");
	}
	else {
		printf("%d", A / (C - B) + 1);
	}
	
	return 0;
}