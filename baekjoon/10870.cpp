#include <stdio.h>

int fibo(int num) {
	if (num > 1)
		return fibo(num - 1) + fibo(num - 2);
	else
		return num;
}
int main() {
	int n;

	scanf("%d", &n);
	printf("%d", fibo(n));
	return 0;
}