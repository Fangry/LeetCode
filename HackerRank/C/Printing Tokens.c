#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);

    char *temp = s;
    while (*temp != '\0') {
        if (*temp == ' ') {
            printf("\n");
        } else {
            printf("%c", *temp);
        }
        temp += 1;
    }

    free(s);
}