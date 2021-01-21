#include <stdio.h>

int main() {
	int C=0;
	int N=0;
	int score[1000] = { 0 };
	double tot=0.0;
	double avg=0.0;
	double count=0.0;
	int i, j;
	scanf("%d", &C);
	for (i = 0; i < C; i++) {
		tot = 0.0;
		avg = 0.0;
		count = 0.0;
		scanf("%d", &N);

		for (j = 0; j < N; j++) {
			scanf("%d", &score[j]);
			tot += score[j];
		}
		avg = tot / (double)N;
		for (j = 0; j < N; j++) {
			if (score[j] > avg) {
				count++;
			}
		}
		printf("%.3lf%%\n", count / (double)N * 100);
	}
	
	return 0;
}