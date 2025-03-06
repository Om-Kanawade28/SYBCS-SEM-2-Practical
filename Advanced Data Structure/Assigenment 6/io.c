#include <stdio.h>

void main() {
    int m[5][5], i, j, n, v, total, sumin, sumout;
    
    printf("How many vertices: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            m[i][j] = 0;
            if (i != j) {
                printf("Is there an edge between %d -> %d (1/0): ", i + 1, j + 1);
                scanf("%d", &m[i][j]);
            }
        }
    }

    printf("\nVertex\tIn-degree\tOut-degree\tTotal degree\n");

    for (v = 0; v < n; v++) {
        sumin = 0;
        sumout = 0;

        for (i = 0; i < n; i++) {
            sumin += m[i][v];
            sumout += m[v][i];
        }

        total = sumin + sumout;
        printf("%d\t%d\t\t%d\t\t%d\n", v + 1, sumin, sumout, total);
    }
}
