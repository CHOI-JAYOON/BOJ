#include <stdio.h>

int main() {
	int n;
	int i,j;
	int a[250000] = { 0 };
	int count = 0;

	while (1) {
		scanf("%d", &n);
		count = 0;
		if (n == 0) {
			break;
		}

		for (i = 2; i <= 2*n; i++) {
			for (j = 2; i * j <= 2*n; j++) {
				a[i * j] = 1;
			}
		}
		for (i = n+1; i <= 2*n; i++) {
			if (!a[i])
				count++;
		
		}

		printf("%d\n", count);
	}
	return 0;
}