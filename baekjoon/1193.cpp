#include <stdio.h>

int main() {
	int x,i,idx=0;
	int top, bot;
	int num[5000] = { 0 };
	scanf("%d", &x);
	num[idx++] = 2;
	while (1) {
		num[idx] = num[idx - 1] + idx + 1;
		if (num[idx] > 10000000)
			break;
		idx++;
	}
	if (x == 1) {
		printf("1/1\n");
	}
	else {
		for (i = 0; i < idx; i++) {
			if (num[i] <= x && x < num[i + 1]) {
				if (i == 0 || i % 2 == 0) {
					top = 1 + (x - num[i]);
					bot = (i + 2) - (x - num[i]);
				}
				else {
					bot = 1 + (x - num[i]);
					top = (i + 2) - (x - num[i]);
				}
			}
		}
		printf("%d/%d\n", top, bot);
	}
	return 0;
}