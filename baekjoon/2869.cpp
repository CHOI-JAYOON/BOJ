#include <stdio.h>

int main() {
	int A, B, V;
	int i=2;
	int D;
	scanf("%d %d %d", &A, &B, &V);

	D = (V - B - 1) / (A - B) + 1;

	printf("%d", D);
	return 0;
}