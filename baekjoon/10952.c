#include <stdio.h>

int main() {
	
	int A=1, B=1;

	while (1) {
		scanf("%d %d", &A, &B);
		if (A == 0 && B == 0) break;
		else printf("%d\n", A + B);

		

	}

	


	return 0;
}