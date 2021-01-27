#include <stdio.h>
#include <string.h>
#define StoD(X) (X==0?0:X-'0')

char A[100000];
char B[100000];
char S[100000];
void reverse(char*, int);
char* add(char*, char*);

int main() {
	
	scanf("%s %s", A, B);
	printf("%s", add(A, B));
	
	return 0;
}
void reverse(char* arr, int len) {
	char temp;

	for (int i = 0; i < len / 2; i++) {
		temp = arr[i];
		arr[i] = arr[len - 1 - i];
		arr[len - 1 - i] = temp;
	}
	return;
}
char* add(char* A, char* B) {
	int len = 0, up = 0;
	if (strlen(A) > strlen(B)) {
		len = strlen(A);
	}
	else
		len = strlen(B);

	reverse(A, strlen(A));
	reverse(B, strlen(B));

	for (int i = 0; i <= len; i++) {
		S[i] = (StoD(A[i]) + StoD(B[i]) + up) % 10 + '0';
		if ((StoD(A[i]) + StoD(B[i]) + up) > 9)
			up = 1;
		else 
			up = 0;
	}

	if (S[len] == '0')
		S[len] = 0;

	reverse(S, strlen(S));
	return S;
}