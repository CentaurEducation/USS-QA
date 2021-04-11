#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main ( int argc, char *argv [] )
{
int N, L;
char f [1000], g [10000], op [10000];

FILE *Out = fopen ( "Output.txt" , "w" );
strcpy ( f, argv [1] );
/*Besides this, we also have to read the number of levels, L, this quantity is discretised to, to complete the description. Preferably, this number is a positive power of 2.*/
L = atoi ( argv [2] );
/*We store the final expression in a string named op, for "operator". Understandably, this string is quite immense, so we have split its specification in our computation from our notes into a function of a smaller string, g. Accordingly, the below code will reflect that. However, the output will be a single formula.*/
itoa ( L, g, 10 );
strcat ( g, "\\sum_{r=0}^{\\infty} \\binom{-1}{r} ( \\hat{I} + \\sum_{n=0}^{\\infty} \\frac{1}{n!}(- " );
strcat ( g, f );
strcat ( g, ")^{n})^{r}" );

strcpy ( op, "\\hat{I} + " );
strcat ( op, g );
strcat ( op, "-\\sum_{j=1}^{\\infty}2^{-j}(\\frac{\\hat{I}}{2}-2\\sum_{\\nu=1}^{\\infty}\\frac{\\nu mod 2}{\\pi\\nu}" );
strcat ( op, "\\sum_{i=1}^{\\infty}\\frac{(-1)^{m+1}(2\\pi\\nu)^{2m-1}}{(2m-1)!}" );
strcat ( op, g );
strcat ( op, ")^{2m-1})" );

;
fprintf ( Out, "%s", op );

return 0;
}
