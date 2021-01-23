#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
	char S[1000000];
	int arr = 0;
	gets_s(S,1000001);
	int len, i, j;
	len = strlen(S);

	for (i = 0; i < len; i++) {
		if (isspace(S[i])) {
			arr++;
		}
	}
	j = arr + 1;
	if (len == arr) {
		j = 0;
		printf("%d", j);
	}
	else {
		if (isspace(S[0])) {
			j--;
		}
		if (isspace(S[len - 1])) {
			j--;
		}
		printf("%d", j);
	}
	return 0;
}