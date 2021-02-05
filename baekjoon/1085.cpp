#include <stdio.h>

int main() {
	int x, y, w, h;
	int arr[4] = { 0 };
	int i;
	int min = 0;
	scanf("%d %d %d %d", &x, &y, &w, &h);
	arr[0] = x;
	arr[1] = w - x;
	arr[2] = y;
	arr[3] = h - y;

	for (i = 0; i < 3; i++) {
		if (arr[i] <= arr[i + 1]) {
			min = arr[i];
			arr[i + 1] = min;
		}
		else 
			min = arr[i + 1];
	}

	printf("%d", min);
	return 0;
}