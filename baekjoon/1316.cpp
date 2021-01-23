#include <stdio.h>
#include <string.h>

int main() {
	int N;
	int i,j;
	char str[100][101];
	int arr[26] = { 0 };
	int count = 0;
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%s", str[i]);
	}

	for (i = 0; i < N; i++) {
		for (j = 0; j < 26; j++) {
			arr[j] = 0;
		}
		for (j = 0; j < strlen(str[i]); j++) {
			if (j > 0 && str[i][j - 1] == str[i][j]) {
				if (j == strlen(str[i]) - 1) {
					count++;
					break;
				}
				else
					continue;
			}
			else {
				if (arr[str[i][j] - 'a'] == 1) {
					break;
				}
				else {
					arr[str[i][j] - 'a'] = 1;
					if (j == strlen(str[i]) - 1) {
						count++;
						break;
					}
				}
			}
		}
	}
	printf("%d", count);
	return 0;
}