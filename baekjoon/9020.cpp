#include <stdio.h>
#include <math.h>

#define size 10001
int main() {
	int n,T;
	int i,j;
	int num[size]={ 0, };

	for (i = 2; i <= (int)sqrt(size); i++) {
		for (j = i * i; j <= size; j += i) {
			if (num[j] % i == 0) {
				num[j] = 1;
			}
		}
	}
	scanf("%d", &T);

	for (i = 0; i < T; i++) {
		scanf("%d", &n);

		for (j = n / 2; j > 0; j--) {
			if (num[j] != 1 && num[n - j] != 1) {
				printf("%d %d\n", j, n - j);
				break;
			}
		}
	}
	return 0;
}