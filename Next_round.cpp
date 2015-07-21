#include <stdio.h>
int main()
{
  int n, k, ranks[100] = {0}, i, count = 0;
  scanf( "%d %d", &n, &k );
  k--;
  for( i = 0; i < n; i++ )
    scanf( "%d", &ranks[i] );
  for( i = 0; i < n; i++ ){
    if( ranks[i] >= ranks[k] && ranks[i] > 0 )
      count++;
  }
  printf( "%d\n", count );
  return 0;
}
