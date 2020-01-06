#include <stdio.h>

int main() {
    char ch;
    char s[100];
    char sen[100];

    scanf("%c", &ch);
    scanf("%s", &s);

    // added a space before % because it will read a newline character from previous line
    // the space tells scanf to ignore the newline character
    scanf(" %[^\n]%*c", &sen);

    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s", sen);

    return 0;
}