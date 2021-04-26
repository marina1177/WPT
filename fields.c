#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define _USE_MATH_DEFINES // for C
#include <math.h>



int w = 150;
int S = 51;
int V = 51;

static void	free_arr(double **arr, int i)
{
	while (i > -1)
		free(arr[i--]);
	free(arr);
}

double		*ft_doublearrnew(int size)
{
	double *arr;

	arr = (double *)malloc(sizeof(double) * size);
	return (arr);
}

double			**ft_doublematrixnew(int rows, int columns)
{
	double		**matrix;
	int		i;

	if (!(matrix = (double **)malloc(sizeof(double *) * rows)))
		return (NULL);
	i = 0;
	while (i < rows)
	{
		if (!(matrix[i] = ft_doublearrnew(columns)))
		{
			free_arr(matrix, i - 1);
			return (NULL);
		}
		i++;
	}
	return (matrix);
}

// create a 2d array from the 1d one
double ** convert2d(unsigned long len1, unsigned long len2, double * arr) {
    double ** ret_arr;

    // allocate the additional memory for the additional pointers
    ret_arr = (double **)malloc(sizeof(double*)*len1);

    // set the pointers to the correct address within the array
    for (int i = 0; i < len1; i++) {
        ret_arr[i] = &arr[i*len2];
    }

    // return the 2d-array
    return ret_arr;
}


void calculate_kpd(float a, float b, float c, float e, float lambda, float D, double **r1){
    long double kpd = 0;
//	double **r1 = ft_doublematrixnew(2*w+1,2*w+1);

for(int j = 0; j <= 2*w; j++)
{
    for(int i = 0; i <= 2*w; i++)
    {  
        r1[i][j] = 0;
    }
}

int size = 19;
double tArray[size];
double gArray[size];
double hArray[size];
double kArray[size];


for (int p = 0; p<=w ; p++){
    int h = 0;
    int u = 0;
    int o = 0;

//    for(int h = 0; h<=w;h++){

    memset (tArray, 0, size*sizeof(double));
    memset (gArray, 0, size*sizeof(double));
    memset (hArray, 0, size*sizeof(double));
    memset (kArray, 0, size*sizeof(double));

//            Расчет полей излучения отдельных модулей.
//            #1
           //printf("FIELD_1\n");

           for (int n = -(S / 2); n <= (S - 2) / 2; n++) {

                for (int m = -(V / 2); m <= (V - 2) / 2; m++) {
                    tArray[0] = tArray[0]
                            + ((a + b) / (S * V))
                            * cos((2 * M_PI/ (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[0] = gArray[0]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

            //            -----------------
//            #2
             //printf("FIELD_2\n");
            for (int n = (S / 2); n <= (3 * S - 2) / 2; n++) {
                for (int m = 0; m <= (V - 1); m++) {
                    tArray[1] = tArray[1]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[1] = gArray[1]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

            //            -----------------
//            #3
            //printf("FIELD_3\n");
            for (int n = (S / 2); n <= (3 * S - 2) / 2; n++) {
                for (int m = -V; m <= -1; m++) {
                    tArray[2] = tArray[2]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[2] = gArray[2]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

            //            -----------------
//            #4
            //printf("FIELD_4\n");
            for (int n = (-S / 2); n <= (S - 2) / 2; n++) {
                for (int m = -(3 * V / 2); m <= (-V - 2) / 2; m++) {
                    tArray[3] = tArray[3]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[3] = gArray[3]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

                       //            -----------------
//            #5
            //printf("FIELD_5\n");
            for (int n = (-3 * S / 2); n <= (-S - 2) / 2; n++) {
                for (int m = -V; m <= -1; m++) {
                    tArray[4] = tArray[4]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[4] = gArray[4]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

            //            -----------------
//            #6
            //printf("FIELD_6\n");
            for (int n = (-3 * S / 2); n <= (-S - 2) / 2; n++) {
                for (int m = 0; m <= V - 1; m++) {

                    tArray[5] = tArray[5]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[5] = gArray[5]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }
//            -----------------
//            #7
            //printf("FIELD_7\n");
            for (int n = (-S / 2); n <= (S - 2) / 2; n++) {
                for (int m = (V / 2); m <= ((3 * V - 2) / 2); m++) {

                    tArray[6] = tArray[6]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[6] = gArray[6]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

//            -----------------
//            #8
            //printf("FIELD_8\n");
            for (int n = (3 * S / 2); n <= (5 * S - 2) / 2; n++) {
                for (int m = (V / 2); m <= ((3 * V - 2) / 2); m++) {

                    tArray[7] = tArray[7]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[7] = gArray[7]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }

            }

//            -----------------
//            #9
            //printf("FIELD_9\n");
            for (int n = (3 * S / 2); n <= (5 * S - 2) / 2; n++) {
                for (int m = -(V / 2); m <= ((V - 2) / 2); m++) {
                    tArray[8] = tArray[8]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[8] = gArray[8]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                }
            }

//            -----------------
//            #10
            //printf("FIELD_10\n");
            for (int n = (3 * S / 2); n <= (5 * S - 2) / 2; n++) {
                for (int m = -(3 * V / 2); m <= ((5 * V - 2) / 2); m++) {
                    tArray[9] = tArray[9]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[9] = gArray[9]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }
//            -----------------
//            #11
            //printf("FIELD_11\n");
            for (int n = (S / 2); n <= (3 * S - 2) / 2; n++) {
                for (int m = -(2 * V / 2); m <= ((-V - 1) / 2); m++) {
                    tArray[10] = tArray[10]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[10] = gArray[10]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }
//            -----------------
//            #12
            //printf("FIELD_12\n");
            for (int n = (-S / 2); n <= (S - 2) / 2; n++) {
                for (int m = -(5 * V / 2); m <= ((-3 * V - 2) / 2); m++) {
                    tArray[11] = tArray[11]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[11] = gArray[11]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

//            -----------------
//            #13
            //printf("FIELD_13\n");
            for (int n = (-3 * S / 2); n <= (-S - 2) / 2; n++) {
                for (int m = -(2 * V / 2); m <= ((-V - 1) / 2); m++) {
                    tArray[12] = tArray[12]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[12] = gArray[12]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

//            -----------------
//            #14
            //printf("FIELD_14\n");
            for (int n = (-5 * S / 2); n <= ((-3 * S - 2) / 2); n++) {
                for (int m = -(3 * V / 2); m <= ((-V - 2) / 2); m++) {

                    tArray[13] = tArray[13]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[13] = gArray[13]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

//            -----------------
//            #15
            //printf("FIELD_15\n");
            for (int n = (-5 * S / 2); n <= ((-3 * S - 2) / 2); n++) {
                for (int m = -(V / 2); m <= ((V - 2) / 2); m++) {
                    tArray[14] = tArray[14]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[14] = gArray[14]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

//            -----------------
//            #16
            //printf("FIELD_16\n");
            for (int n = (-5 * S / 2); n <= ((-3 * S - 2) / 2); n++) {
                for (int m = (V / 2); m <= ((3 * V - 2) / 2); m++) {
                    tArray[15] = tArray[15]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[15] = gArray[15]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

//            -----------------
//            #17
            //printf("FIELD_17\n");
            for (int n = (-3 * S / 2); n <= ((-S - 2) / 2); n++) {
                for (int m = (V); m <= (2 * V - 1); m++) {

                    tArray[16] = tArray[16]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[16] = gArray[16]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                }
            }
//            -----------------
//            #18
            //printf("FIELD_18\n");
            for (int n = (-S / 2); n <= ((S - 2) / 2); n++) {
                for (int m = (3 * V / 2); m <= ((5 * V - 2) / 2); m++) {
                    tArray[17] = tArray[17]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[17] = gArray[17]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }

//            -----------------
//            #19
            //printf("FIELD_19\n");
            for (int n = (S / 2); n <= ((3 * S - 2) / 2); n++) {
                for (int m = (V); m <= (2 * V - 1); m++) {
                    tArray[18] = tArray[18]
                            + ((a * b) / (S * V))
                            * cos((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));

                    gArray[18] = gArray[18]
                            + ((a * b) / (S * V))
                            * sin((2 * M_PI / (lambda * D))
                            * (((2 * n + 1) * (p) * a / (2 * S))
                            + ((2 * m + 1) * b * h / (2 * V))));
                }
            }


            //        Расчет фазового распределения.
            //printf("PHASE_1\n");
            kArray[0] = atan2(
                    (tArray[0] + gArray[0] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[0] + tArray[0] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_2\n");
            kArray[1] = atan2(
                    (tArray[1] + gArray[1] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[1] + tArray[1] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_3\n");
            kArray[2] = atan2(
                    (tArray[2] + gArray[2] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[2] + tArray[2] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_4\n");
            kArray[3] = atan2(
                    (tArray[3] + gArray[3] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[3] + tArray[3] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_5\n");
            kArray[4] = atan2(
                    (tArray[4] + gArray[4] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[4] + tArray[4] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_6\n");
            kArray[5] = atan2(
                    (tArray[5] + gArray[5] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[5] + tArray[5] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_7\n");
            kArray[6] = atan2(
                    (tArray[6] + gArray[6] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[6] + tArray[6] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_8\n");
            kArray[7] = atan2(
                    (tArray[7] + gArray[7] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[7] + tArray[7] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_9\n");
            kArray[8] = atan2(
                    (tArray[8] + gArray[8] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[8] + tArray[8] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_10\n");
            kArray[9] = atan2(
                    (tArray[9] + gArray[9] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[9] + tArray[9] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_11\n");
            kArray[10] = atan2(
                    (tArray[10] + gArray[10] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[10] + tArray[10] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_12\n");
            kArray[11] = atan2(
                    (tArray[11] + gArray[11] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[11] + tArray[11] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_13\n");
            kArray[12] = atan2(
                    (tArray[12] + gArray[12] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[12] + tArray[12] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_14\n");
            kArray[13] = atan2(
                    (tArray[13] + gArray[13] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[13] + tArray[13] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_15\n");
            kArray[14] = atan2(
                    (tArray[14] + gArray[14] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[14] + tArray[14] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_16\n");
            kArray[15] = atan2(
                    (tArray[15] + gArray[15] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[15] + tArray[15] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_17\n");
            kArray[16] = atan2(
                    (tArray[16] + gArray[16] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[16] + tArray[16] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_18\n");
            kArray[17] = atan2(
                    (tArray[17] + gArray[17] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[17] + tArray[17] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));

            //printf("PHASE_19\n");
            kArray[18] = atan2(
                    (tArray[18] + gArray[18] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))),
                    (-gArray[18] + tArray[18] * tan((2 * M_PI * (D + ((p * p + h * h) / (2 * D))) / lambda))));


//            Расчет амплитудного распределения
            //printf("AMPLITUDES\n");
            hArray[0] = sqrt((e / (lambda * D * lambda * D)) * (pow(tArray[0], 2) + pow(gArray[0], 2)));
            hArray[1] = sqrt((e / (lambda * D * lambda * D)) * (pow(tArray[1], 2) + pow(gArray[1], 2)));
            hArray[2] = sqrt((e / (lambda * D * lambda * D)) * (pow(tArray[2], 2) + pow(gArray[2], 2)));
            hArray[3] = sqrt((e / (lambda * D * lambda * D)) * (pow(tArray[3], 2) + pow(gArray[3], 2)));
            hArray[4] = sqrt((e / (lambda * D * lambda * D)) * (pow(tArray[4], 2) + pow(gArray[4], 2)));
            hArray[5] = sqrt((e / (lambda * D * lambda * D)) * (pow(tArray[5], 2) + pow(gArray[5], 2)));
            hArray[6] = sqrt((e / (lambda * D * lambda * D)) * (pow(tArray[6], 2) + pow(gArray[6], 2)));
            hArray[7] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[7], 2) + pow(gArray[7], 2)));
            hArray[8] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[8], 2) + pow(gArray[8], 2)));
            hArray[9] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[9], 2) + pow(gArray[9], 2)));
            hArray[10] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[10], 2) + pow(gArray[10], 2)));
            hArray[11] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[11], 2) + pow(gArray[11], 2)));
            hArray[12] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[12], 2) + pow(gArray[12], 2)));
            hArray[13] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[13], 2) + pow(gArray[13], 2)));
            hArray[14] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[14], 2) + pow(gArray[14], 2)));
            hArray[15] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[15], 2) + pow(gArray[15], 2)));
            hArray[16] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[16], 2) + pow(gArray[16], 2)));
            hArray[17] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[17], 2) + pow(gArray[17], 2)));
            hArray[18] = sqrt((c * c * e / (lambda * D * lambda * D)) * (pow(tArray[18], 2) + pow(gArray[18], 2)));


//            Расчет суммарного поля.

            //printf("RESULT FIELD:\n");
            r1[p][h] = hArray[0]
                    + hArray[1] * cos(kArray[1] - kArray[0])
                    + hArray[2] * cos(kArray[2] - kArray[0])
                    + hArray[3] * cos(kArray[3] - kArray[0])
                    + hArray[4] * cos(kArray[4] - kArray[0])
                    + hArray[5] * cos(kArray[5] - kArray[0])
                    + hArray[6] * cos(kArray[6] - kArray[0])
                    + hArray[7] * cos(kArray[7] - kArray[0])
                    + hArray[8] * cos(kArray[8] - kArray[0])
                    + hArray[9] * cos(kArray[9] - kArray[0])
                    + hArray[10] * cos(kArray[10] - kArray[0])
                    + hArray[11] * cos(kArray[11] - kArray[0])
                    + hArray[12] * cos(kArray[12] - kArray[0])
                    + hArray[13] * cos(kArray[13] - kArray[0])
                    + hArray[14] * cos(kArray[14] - kArray[0])
                    + hArray[15] * cos(kArray[15] - kArray[0])
                    + hArray[16] * cos(kArray[16] - kArray[0])
                    + hArray[17] * cos(kArray[17] - kArray[0])
                    + hArray[18] * cos(kArray[18] - kArray[0]);

            //        Вывод результатов.
            printf("p: %d\n" , p);
            printf("h: %d\n" , h);
            printf("r1^2: %f\n",r1[p][h]*r1[p][h]);


	}

////       Расчет КПД.
//        printf("Calculate KPD\n");
//        for (int j = 0; j <= w; j++) {
//            kpd = 0;
//            for (int p = 0; p < 2*j; p++) {
//                for (int h = 0; h < 2*j; h++) {
////                    printf("%d: %d,%d\n", j, p,h);
//                    kpd = (kpd + r1[p][h] * r1[p][h] / (10.5 + 12 * 1.5 * c * c));
////                    printf("kpd: %Lf\n" ,kpd);
//                }
//            }
//
//        }
//    printf("kpd: %Lf\n" ,kpd);
//    return(r1);
}


//int			main(int argc, char **argv)
//{
//	calculate_kpd(1,1,1,1, 0.01,100);
//	return (0);
//}