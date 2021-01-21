#include <stdio.h>
#include <string.h>

int main() {
	int n;
	char arr[80];
	int count;
	int combo;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		count = 0;
		combo = 1;
		scanf("%s", arr);
		for (int j = 0; j < strlen(arr); j++) {
			if (arr[j] == 'O') {
				count += combo;
				combo++;
			}
			if (arr[j] == 'X') {
				combo = 1;
			}
		}
		printf("%d\n", count);
	}
	return 0;
}