#include <stdio.h>

int main() {

	int max = 0,min=100;
	int i,a,n;
	for (i = 0; i < 9; i++) {
		scanf("%d", &a);
		if (a > max) {
			max = a;
			n = i;
		}	
	}
	printf("%d\n", max);
	printf("%d", n+1);
	return 0;
}