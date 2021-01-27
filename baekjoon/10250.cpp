#include <stdio.h>

int main() {
	int T, H, W, N;
	int F,i;
	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		scanf("%d %d %d", &H, &W, &N);
		if (N % H == 0) {
			printf("%d\n", H * 100 + (N / H));
		}
		else {
			F = (N % H) * 100 + (N / H) + 1;
			printf("%d\n", F);
		}
			
	}	
	return 0;
}