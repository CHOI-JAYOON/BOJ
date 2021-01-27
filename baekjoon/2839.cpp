#include <stdio.h>

int main() {
	int N;
	int d=0;
	scanf("%d", &N);
	
	while (N > 0) {
		if (N % 5 == 0) {
			N -= 5;
			d++;
		}
		else if (N % 3 == 0) {
			N -= 3;
			d++;
		}
		else if (N > 5) {
			N -= 5;
			d++;
		}
		else {
			d = -1;
			break;
		}
	}
	printf("%d", d);
	
	return 0;
}
