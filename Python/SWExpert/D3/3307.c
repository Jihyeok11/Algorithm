#include <stdio.h>
 
int main(void)
{
    int test_case;
    int T;
    scanf("%d", &T);
 
    for (test_case = 1; test_case <= T; test_case++)
    {
        int n;
        scanf("%d", &n);
        int number[1001] = { 0, };
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &number[i]);
        }
        int max = 0;
        int opt[1001] = { 0, };
        for (int i = 0; i < n; i++) {
            opt[i] = 1;
            for (int j = 0; j < i; j++) {
                if (number[j] < number[i] && opt[i] < opt[j] + 1)
                    opt[i] = opt[j] + 1;
            }
            if (opt[i] > max)
                max = opt[i];
        }
        
        printf("#%d %d\n", test_case, max);
 
    }
    return 0;
}