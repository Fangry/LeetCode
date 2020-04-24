#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);
    int width = 2 * n - 1;
    int center = n - 1;

    for (int i = 0; i < width; ++i) {
        int y_dist = abs(i - center);
        for (int j = 0; j < width; ++j) {
            int x_dist = abs(j - center);
            int dist_from_center = 0;
            if (x_dist > y_dist) {
                dist_from_center = x_dist;
            } else {
                dist_from_center = y_dist;
            }
            printf("%d ", dist_from_center + 1);
        }
        printf("\n");
    }
}