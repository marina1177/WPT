
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define _USE_MATH_DEFINES // for C
#include <math.h>

int loop(){
int cnt = 0;
int w =3;
//for(int j = 0; j<=w; j++){
//	for(int p=-j; p<=j;p++){
//		for (int h = -j; h<=j;h++){
//		cnt++;
//		printf("%d: %d,%d\n", j, p,h);
//		}
//	}
//}
for (int j = 0; j <= w; j++) {
            for (int p = 0; p <= 2*j; p++) {
                for (int h = 0; h <= 2*j; h++) {
                   	cnt++;
					printf("%d: %d,%d\n", j, p,h);
                }
            }

        }
return cnt;
}

int			main(int argc, char **argv)
{
	printf("cnt: %d",loop());
	return (0);
}