#include <stdio.h>

int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int can_achieve_height(int heights[], int n, long long k, int mid)
{
    long long required_taka = 0;

    for (int i = 0; i < n; ++i)
    {
        if (heights[i] < mid)
        {
            required_taka += (mid - heights[i]);
        }
        if (required_taka > k)
        {
            return 0;
        }
    }
    return 1;
}

int maximize_min_height(int heights[], int n, long long k)
{
    qsort(heights, n, sizeof(int), compare);

    int low = heights[0];
    int high = heights[0] + k;
    int answer = low;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (can_achieve_height(heights, n, k, mid))
        {
            answer = mid;
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    return answer;
}

int main()
{
    int n;
    long long k;
    scanf("%d %lld", &n, &k);

    int heights[1000];
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &heights[i]);
    }

    int result = maximize_min_height(heights, n, k);

    printf("%d\n", result);

    return 0;
}
