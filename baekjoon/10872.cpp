#include <stdio.h>

int fact(int num) {
	if (num > 1)
		return num * fact(num - 1);
	else
		return 1;
}

int main() {
	int N;

	scanf("%d", &N);
	printf("%d", fact(N));

	return 0;
}