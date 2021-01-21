#include <stdio.h>
int self_num();

int main() {
	self_num();
	return 0;
}
int self_num() {
	int sum = 0;
	int n[10001] = { 0 };
	int i;
	for (i = 1; i <= 10000; i++) {
		if (i < 10) {
			sum = i + i;
			n[sum] = 1;
		}
		else if (i < 100) {
			sum = i + (i % 10) + (i / 10);
			n[sum] = 1;
		}
		else if (i < 1000) {
			sum = i + (i % 10)+ (i / 10) % 10 +(i/100);
			n[sum] = 1;
		}
		else if (i < 10000) {
			sum = i + (i % 10) + (i/10)%10 + ((i-(i%100))/100)%10 + i / 1000;
			if(sum<=10000) n[sum] = 1;
		}
		
	}
	for (i = 1; i <= 10000; i++) {
		if (n[i] != 1) {
			printf("%d\n", i);
		}
	}
	return 0;

}