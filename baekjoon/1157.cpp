#include <stdio.h>
#include <string.h>

int main() {
	char S[1000000];
	scanf("%s", S);
	int i,j;
	int arr[26]={ 0 };
	int max=0;
	int res = 0;
	int select = 0;
	int len;
	len = strlen(S);
	for (i = 'a'; i <= 'z'; i++) {
		for (j = 0; j < len; j++) {
			if (i == S[j]) {
				arr[i - 'a']++;
			}
		}
	}
	for (i = 'A'; i <= 'Z'; i++) {
		for (j = 0; j < len; j++) {
			if (i == S[j]) {
				arr[i - 'A']++;
			}
		}
	}

	for (i = 0; i < 26; i++) {
		if (arr[i] > max) {
			max = arr[i];
			select = i;
		}
	}
	
	for (i = 0; i < 26; i++) {
		if (arr[i] == max) {
			res++;
		}
	}
	if (res > 1) {
		printf("?\n");
	}
	else
		printf("%c", select + 'A');

	return 0;
}