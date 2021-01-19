#include <stdio.h>

int main() {
	int N, i;
	double M = 0.0;
	double sum=0.0;
	double avg = 0.0;
	scanf("%d", &N);
	double score[1001] = { 0 };
	for (i = 0; i < N; i++) {
		scanf("%lf", &score[i]);	
	}
	for (i = 0; i < N; i++) {
		if (score[i] > M) {
			M = score[i];
		}
	}
	for (i = 0; i < N; i++) {
		sum += score[i] / M * 100.0;
	}
	avg = sum/ (double)N;

	printf("%.2lf", avg);

	return 0;
}