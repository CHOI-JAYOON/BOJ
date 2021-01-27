#include <stdio.h>

int main() {
	int T, k,n;
	int i,j;
	int apt[15][15] = { 0 };

	for (j = 0; j < 15; j++) {
		apt[0][j] = j;
	}
	for (i = 1; i < 15; i++) {
		for (j = 1; j < 15; j++) {
			apt[i][j] = apt[i - 1][j] + apt[i][j - 1];
		}
	}
	scanf("%d", &T);

	for (i = 0; i < T; i++) {
		scanf("%d", &k);
		scanf("%d", &n);

		printf("%d\n", apt[k][n]);
	}
	return 0;
}