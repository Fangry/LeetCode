#include <stdio.h>
#include <stdlib.h>

int main() {
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int *)malloc(num * sizeof(int));
    for (i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }

    int start = 0;
    int end = num - 1;

    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start += 1;
        end -= 1;
    }

    for (i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}