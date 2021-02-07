#include <stdio.h>
#define minFinder(a,b) a<b?a:b

int main() {
	int M, N;
	int i, j,a,b;
	char arr[50][50];
	int min = 80, cntB = 0, cntW = 0;

	scanf("%d %d", &N, &M);
	for (i = 0; i < N; i++) {
		scanf("%s", &arr[i]);	
	}

	for (i = 0; i < N-7; i++) {
		for (j = 0; j < M - 7; j++) {
			cntB = 0;
			cntW = 0;
			for (a = i; a < i + 8; a++) {
				for (b = j; b < j + 8; b++) {
					if ((a + b) % 2 == 0) {
						if (arr[a][b] == 'B')
							cntW++;
						else
							cntB++;
					}
					else {
						if (arr[a][b] == 'B')
							cntB++;
						else
							cntW++;
					}
				}
			}
			min = minFinder(min, cntB);
			min = minFinder(min, cntW);
		}
	}
	printf("%d\n", min);

	return 0;
}