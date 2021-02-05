#include <stdio.h>
#include <math.h>
#define pi 3.14159265358979323846

int main() {
	int  R;
	scanf("%d", &R);

	printf("%.6f\n", R * R * pi);
	printf("%.6f", 2.0 * R * R);
	return 0;
}