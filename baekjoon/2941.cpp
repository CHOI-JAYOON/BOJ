#include <stdio.h>
#include <string.h>

int main() {
	char str[100];
	scanf("%s", str);
	int i,len;
	len = strlen(str);
	int count = 0;
	for (i = 0; i < len; i++) {
		if (str[i] == 'c') {
			if (str[i + 1] == '='|| str[i + 1] == '-')
				i++;
		}
		else if (str[i] == 'd') {
			if (str[i + 1] == 'z'&& str[i + 2] == '=') {
				i++;
				i++;
			}
			else if (str[i + 1] == '-') {
				i++;
			}
		}
		else if (str[i] == 'l') {
			if (str[i + 1] == 'j') {
				i++;
			}
			
		}
		else if (str[i] == 'n') {
			if (str[i + 1] == 'j') {
				i++;
			}
		}
		else if (str[i] == 's') {
			if (str[i + 1] == '=') {
				i++;
			}
		}
		else if (str[i] == 'z') {
			if (str[i + 1] == '=') {
				i++;
			}
		}
		count++;
	}
	printf("%d", count);
	return 0;
}