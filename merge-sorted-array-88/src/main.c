#include <stdio.h>
#include "main.h"

void print_array(int *nums, int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", nums[i]);
    }
    printf("\n");
}

void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n)
{
    int p1 = m - 1, p2 = n - 1, p = nums1Size - 1;

    while (p1 >= 0 && p2 >= 0)
    {
        if (nums1[p1] > nums2[p2])
        {
            nums1[p] = nums1[p1];
            p1 -= 1;
        }
        else
        {
            nums1[p] = nums2[p2];
            p2 -= 1;
        }
        p -= 1;
    }

    while (p2 >= 0)
    {
        nums1[p] = nums2[p2];
        p -= 1;
        p2 -= 1;
    }
}