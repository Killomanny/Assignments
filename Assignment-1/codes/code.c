#include <stdio.h>
#include <math.h>

//need to prove ( sec(x)^2 + cosec(x)^2 )^{1/2} = tan(x) +  cot(x)
//rather we do (RHS-LHS) and show that value is nearly zero or zero

double RHS(double x) // gives RHS value for a given x
{
 double a;
 a=tan(x)+(1/tan(x));
 return a;
}

double LHS(double x) // gives LHS value for a given x
{
 double a;
 a=(1/cos(x))*(1/cos(x))+(1/sin(x))*(1/sin(x));
 a=sqrt(a);
 return a;
}

int main()
{
    /*

     need to prove ( sec(x)^2 + cosec(x)^2 )^{1/2} = tan(x) +  cot(x)

     LHS-RHS need to be zero or nearly zero
     ( it can't be exactly zero always
       because computer calculations because of some precision in calculating sqrt() and cot...  )

     let that error lies between -0.001 and 0.001

    */

    double x;
    scanf("%lf",&x);

    double c;
    c=RHS(x)-LHS(x);

    if(  c < 0.001  && c > -0.001  && RHS(x) > 0  )
    {
      printf("LHS=RHS so the statement is true ");
    }
    if( RHS(x) < 0 )
    {
      printf("x is not in the range where the condition is true as RHS(x) < 0 ");
    }

    return 0;
}
