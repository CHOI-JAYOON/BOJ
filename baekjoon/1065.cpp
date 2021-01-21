#include <stdio.h>
int hansu();

int main() {

	hansu();
	return 0;
}
int hansu() {
	int N;
	int arr[1001] = { 0 };
	int i;
	int count = 0;
	scanf("%d", &N);
	for (i = 1; i <= N; i++) {
		if (i < 100) {
			arr[i] = 1;
		}
		else if (i < 1000) {
			if ((i % 10) - ((i / 10) % 10) == ((i / 10) % 10) - (i / 100)) {
				arr[i] = 1;
			}
		}
	}

	for (i = 1; i <= N; i++) {
		if (arr[i] == 1) {
			count++;
		}
	}
	printf("%d\n", count);
	return count;
}