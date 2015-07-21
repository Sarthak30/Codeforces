#include <stdio.h>

#define MAX_LEN 110

int main() {
    int n;
    scanf("%d", &n);
    char mat[MAX_LEN][MAX_LEN];
    for (int i=0; i < n; ++i) {
        scanf("%s", mat[i]);
    }
    for (int i=0; i < n; ++i) {
        for (int j=0; j < n; ++j) {
            int count = 0;
            if (i > 0 && mat[i-1][j] == 'o') {
                count++;
            }
            if (i < n-1 && mat[i+1][j] == 'o') {
                count++;
            }
            if (j > 0 && mat[i][j-1] == 'o') {
                count++;
            }
            if (j < n-1 && mat[i][j+1] == 'o') {
                count++;
            }
            if (count % 2 != 0) {
                printf("NO\n");
                return 0;
            }
        }
    }
    printf("YES\n");
    return 0;
}
