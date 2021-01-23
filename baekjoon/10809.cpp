#include <stdio.h>
#include <string.h>
int main() {

	char S[101];
	int i,j;
	int arr[26] = { 0 };
	int a = 0;
	scanf("%s", S);

	for (i = 'a'; i <='z'; i++) {
		for (j = 0; j < strlen(S); j++) {
			if (S[j]==i) {
				arr[i-97] = j+1;
				break;
			}
		}
	}
	
	for (i = 0; i <26; i++) {
		printf("%d ", arr[i]-1);
	}
	return 0;
}