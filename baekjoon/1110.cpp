#include <stdio.h>

int main() {

	int N;
	int A,B;
	int C = 0;
	scanf("%d", &N);
	A = N;
	while (1) {
		B = (A / 10) + (A% 10);

		if (B < 10) {
			A = (A % 10 * 10) + B;
			C++;
			if (A == N) {
				printf("%d", C);
				break;
			}
		}
		else {
			A = (A % 10) * 10 + (B % 10);
			C++;
			if (A == N) {
				printf("%d", C);
				break;
			}
		}
	}
	return 0;
}