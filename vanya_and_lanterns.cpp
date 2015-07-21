#include <stdio.h>

#define N 1000

int main (int argc, char * argv[])
{
    int n, l, lantern[N];
    int i, j, tmp;
    float d, maximum_distance, left_border, right_border;

    scanf("%d%d", &n, &l);

    for(i=0; i<n; i++)
        scanf("%d", &lantern[i]);

    /* ordering lantern[N] in a crescent order */
    for(i=0; i<n-1; i++)
        for(j=i; j<n; j++)
            if(lantern[j]<lantern[i]){
                tmp=lantern[i];
                lantern[i]=lantern[j];
                lantern[j]=tmp;
            }

    /* finding maximum distance between lantern i and i+1 */

    for(i=0, maximum_distance=0; i<n-1; i++) {
        if( (lantern[i+1]-lantern[i])>=maximum_distance )
            maximum_distance=lantern[i+1]-lantern[i];
    }


    d=maximum_distance/2;


    left_border=lantern[0];
    right_border=l-lantern[n-1];

    if(left_border>=d){
        d=left_border;
    } if (right_border>=d){
        d=right_border;
    }

    printf("%f\n", d);

    return 0;
}
