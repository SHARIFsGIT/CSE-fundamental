#include <stdio.h>
int main()
{
    long long int eye, mouth, bodies;
    scanf("%lld %lld %lld", &eye, &mouth, &bodies);
    
    if (eye <= mouth && eye <= bodies)
        printf("%lld", eye);
    else if (bodies <= eye && bodies <= mouth)
        printf("%lld", bodies);
    else if ((eye - mouth) / 2 <= bodies - mouth)
        printf("%lld", mouth + (eye - mouth) / 2);
    else
        printf("%lld", bodies);
}
