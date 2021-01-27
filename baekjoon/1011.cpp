#include <stdio.h>
#include <math.h>

int main() {
	int T, i;
	long long x, y, a;
	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		scanf("%lld %lld", &x, &y);
		a = (int)sqrt(y - x);
		
		if ((y - x) == a * a) {
			printf("%lld\n", 2 * a - 1);
		}
		else if (a * a < (y - x) && (y - x) <= a * a + a) {
			printf("%lld\n", 2 * a);
		}
		else if (a * a + a < (y - x) && (y - x) < (a + 1) * (a + 1)) {
			printf("%lld\n",2*a+1);
		}

	}

	return 0;
}