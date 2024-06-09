#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Function to check if a number is prime
bool isPrime(int num)
{
    if (num <= 1) return false; // Numbers less than or equal to 1 are not prime
    if (num == 2) return true;  // 2 is the only even prime number
    if (num % 2 == 0) return false; // Even numbers greater than 2 are not prime
    
    // Check for factors from 3 up to the square root of the number
    for (int i = 3; i * i <= num; i += 2)
    {
        if (num % i == 0) return false;
    }
    return true;
}

// Function to generate the first 'count' prime numbers and store them in an array
void generatePrimes(int *primes, int count)
{
    int num = 2; // Start checking for primes from 2
    int found = 0; // Counter for the number of primes found

    while (found < count)
    {
        if (isPrime(num))
        {
            primes[found++] = num; // Store the prime number in the array
        }
        num++; // Move to the next number
    }
}

// Function to generate an n x n spiral pattern of prime numbers
void generateSpiralPattern(int n)
{
    int totalNumbers = n * n; // Total numbers needed for the n x n matrix
    int *primes = (int *)malloc(totalNumbers * sizeof(int)); // Allocate memory for the prime numbers array

    generatePrimes(primes, totalNumbers); // Generate the required prime numbers

    int spiral[n][n]; // 2D array to store the spiral pattern
    int idx = 0; // Index for the primes array

    int k = 0, l = 0; // Start row and column
    int m = n, r = n; // End row and column

    // Loop to fill the 2D array in a spiral order
    while (k < m && l < r)
    {
        // Fill the top row from left to right
        for (int i = l; i < r; ++i)
        {
            spiral[k][i] = primes[idx++];
        }
        k++; // Move to the next row

        // Fill the right column from top to bottom
        for (int i = k; i < m; ++i)
        {
            spiral[i][r - 1] = primes[idx++];
        }
        r--; // Move to the previous column

        // Fill the bottom row from right to left
        if (k < m)
        {
            for (int i = r - 1; i >= l; --i)
            {
                spiral[m - 1][i] = primes[idx++];
            }
            m--; // Move to the previous row
        }

        // Fill the left column from bottom to top
        if (l < r)
        {
            for (int i = m - 1; i >= k; --i)
            {
                spiral[i][l] = primes[idx++];
            }
            l++; // Move to the next column
        }
    }

    // Print the spiral pattern
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d ", spiral[i][j]);
        }
        printf("\n");
    }

    free(primes); // Free the allocated memory for primes
}

int main()
{
    int n;
    scanf("%d", &n); // Input the size of the spiral

    generateSpiralPattern(n); // Generate and print the spiral pattern

    return 0;
}
