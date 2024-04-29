#include <stdio.h>

int global_value = 100;
void fun(void)
{
    int value = 100;
    printf("Fun value: %p\n", &value);
    printf("Fun global value: %p\n", &global_value);
}
int main()
{
    int value = 100;
    printf("Main value: %p\n", &value);
    printf("Main global value: %p\n", &global_value);
    fun();
    return 0;
}