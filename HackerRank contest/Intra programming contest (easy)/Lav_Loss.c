#include <stdio.h>

int main() {
    double X, Y, Z;
    scanf("%lf %lf %lf", &X, &Y, &Z);

    double CP = X / (1 - Y / 100);

    double newSP = CP * (1 + Z / 100);

    printf("%.2lf\n", newSP);

    return 0;
}
