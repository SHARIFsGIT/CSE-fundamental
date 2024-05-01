#include <stdio.h>
int main()
{
    int x = 100;
    int *ptr = &x;

    printf("Value of x: %d\n", x);
    printf("Address of x: %p\n", &x);

    printf("Value of ptr: %p\n", ptr);
    printf("Address of ptr: %p\n", &ptr);
    printf("Size of ptr: %d\n", sizeof(ptr));

    x = 200;
    printf("Value of new x: %d\n", x);
    printf("Value of new ptr: %d\n", *ptr);
    printf("So value of x = value of *ptr\n");
    printf("Address of new x: %p\n", &x);
    printf("Value of new ptr: %p\n", ptr);

    double y = 5.50;
    double *ptry = &y;
    printf("Value of y: %0.2lf\n", y);
    printf("Value of *ptry: %0.2lf\n", *ptry);
    printf("Size of ptry: %d\n", sizeof(ptry));

    *ptry = 10.20;
    printf("Value of new y: %0.2lf\n", y);

    double *ptr3 = ptry;
    *ptr3 = 50.55;
    printf("Value of latest y: %0.2lf\n", y);
    printf("Value of latest *ptry: %0.2lf\n", *ptry);
    printf("Value of latest ptr3: %0.2lf\n", *ptr3);


    return 0;
}