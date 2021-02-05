#include <stdio.h>

int main() {

	int N;
	int i,num,j;
	int count = 0;
	int flags;

	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%d", &num);
		flags = 0;

		if (num == 1) {
			continue;
		}
		for (j = 2; j < num; j++) {
			if (num % j == 0) {
				flags = 1;
			}
		}
		if (flags == 0) {
			count++;
		}
	}
	
	printf("%d", count);
	return 0;
}