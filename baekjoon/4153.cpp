#include <stdio.h>
#include <math.h>

int main() {
	int a, b, c;
	int max;
	int res;
	while (1) {
		res = 0;
		scanf("%d %d %d", &a, &b, &c);
		if (a == 0 && b == 0 && c == 0) {
			break;
		}
		if (a > b && a > c) {
			res = pow(a, 2) - pow(b, 2) - pow(c, 2);
		}
		else if (b > a && b > c) {
			res = pow(b, 2) - pow(a, 2) - pow(c, 2);
		}
		else if (c > a && c > b) {
			res = pow(c, 2) - pow(a, 2) - pow(b, 2);
		}

		if (res == 0) {
			printf("right\n");
		}
		else
			printf("wrong\n");

	}
	
	return 0;
}