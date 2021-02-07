#include <stdio.h>
#include <math.h>

int main() {
	int N;
	int idx = 0;
	int num = 665;
	int i;

	scanf("%d", &N);
	while (1) {
		if (idx == N) {
			break;
		}
		num++;
		for (i = 0; i < 10; i++) {
			if (num / (int)pow(10, i) % 1000 == 666) {
				idx++;
				break;
			}
		}
	}
	printf("%d", num);
	return 0;
}