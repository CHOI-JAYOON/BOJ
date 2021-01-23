#include <stdio.h>

int main() {
	int A, B;
	int a, b;
	scanf("%d %d", &A, &B);
	a = (A % 10) * 100 + ((A / 10) % 10) *10 + (A / 100);
	b = (B % 10) * 100 + ((B / 10) % 10) * 10 + (B / 100);
	if (a > b) {
		printf("%d", a);
	}
	else
		printf("%d", b);

	return 0;
}