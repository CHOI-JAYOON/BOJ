#include <stdio.h>

long long sum(int* a, int n) {
	long long ans = 0;
	int i;
	for (int i = 0; i < n; i++) {
		ans += a[i];
	}
	return ans;
}
