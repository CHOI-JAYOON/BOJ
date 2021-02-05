#include <stdio.h>
#define size 3000

char flags[size][size] = { NULL };

int star(int num, int n_num) {
	int i, j;
	if (n_num == num * 3) {
		return 0;
	}
	else {
		if (n_num == 3) {
			for (i = 0; i < num; i++) {
				for (j = 0; j < num; j++) {
					if (i % 3 == 1 && j % 3 == 1) {
						flags[i][j] = ' ';
					}
					else
						continue;
				}
			}
		}
		else {
			for (i = 0; i < num; i++) {
				for (j = 0; j < num; j++) {
					if (n_num / 3 <= i && i < 2 * n_num / 3 && n_num / 3 <= j&&j<2*n_num/3) {
						flags[i][j] = ' ';
					}
					else
						flags[i][j] = flags[i % n_num][j % n_num];
				}
			}
		}
		star(num, n_num * 3);
	}
}

int main() {
	int N,i;
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			flags[i][j] = '*';
		}
	}
	star(N, 3);
	for (i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			printf("%c", flags[i][j]);
		}
		printf("\n");
	}
	return 0;
}