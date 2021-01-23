#include <stdio.h>
#include <string.h>

int main() {
	char S[15];
	int i;
	int len;
	int time=0;
	scanf("%s", S);
	len = strlen(S);
	for (i = 0; i < len; i++) {
		if ('A' <= S[i] && S[i] <= 'C') {
			time += 3;
		}
		else if ('D' <= S[i] && S[i] <= 'F') {
			time += 4;
		}
		else if ('G' <= S[i] && S[i] <= 'I') {
			time += 5;
		}
		else if ('J' <= S[i] && S[i] <= 'L') {
			time += 6;
		}
		else if ('M' <= S[i] && S[i] <= 'O') {
			time += 7;
		}
		else if ('P' <= S[i] && S[i] <= 'S') {
			time += 8;
		}
		else if ('T' <= S[i] && S[i] <= 'V') {
			time += 9;
		}
		else if ('W' <= S[i] && S[i] <= 'Z') {
			time += 10;
		}
		else if (S[i] == 1) {
			time += 2;
		}
		else if (S[i] == 0) {
			time += 11;
		}
		

	}
	printf("%d", time);
	return 0;
}