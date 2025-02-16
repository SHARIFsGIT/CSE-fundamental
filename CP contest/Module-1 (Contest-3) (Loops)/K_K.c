#include <stdio.h>
int main()
{
    int numOperations, glassCapacity, mugCapacity;
    scanf("%d %d %d", &numOperations, &glassCapacity, &mugCapacity);

    int currentGlassVolume = 0;
    int currentMugVolume = 0;

    for (int i = 0; i < numOperations; i++)
    {
        if (currentGlassVolume == glassCapacity)
        {
            currentGlassVolume = 0;
        }
        else if (currentMugVolume == 0)
        {
            currentMugVolume = mugCapacity;
        }
        else
        {
            int spaceLeftInGlass = glassCapacity - currentGlassVolume;
            if (spaceLeftInGlass >= currentMugVolume)
            {
                currentGlassVolume += currentMugVolume;
                currentMugVolume = 0;
            }
            else
            {
                currentMugVolume -= spaceLeftInGlass;
                currentGlassVolume = glassCapacity;
            }
        }
    }

    printf("%d %d\n", currentGlassVolume, currentMugVolume);
    return 0;
}