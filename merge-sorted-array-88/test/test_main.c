#include "unity.h"
#include "main.h"

void setUp(void) {}
void tearDown(void) {}

void test_example1(void)
{
    int nums1[6] = {1, 2, 3, 0, 0, 0};
    int m = 3;
    int nums2[3] = {2, 5, 6};
    int n = 3;

    int expected[6] = {1, 2, 2, 3, 5, 6};

    merge(nums1, 6, m, nums2, 3, n);

    TEST_ASSERT_EQUAL_INT_ARRAY(expected, nums1, 6);
}

void test_example2(void)
{
    int nums1[1] = {1};
    int m = 1;
    int *nums2 = NULL;
    int n = 0;

    int expected[1] = {1};

    merge(nums1, 1, m, nums2, 0, n);

    TEST_ASSERT_EQUAL_INT_ARRAY(expected, nums1, 1);
}

void test_example3(void)
{
    int nums1[1] = {0};
    int m = 0;
    int nums2[1] = {1};
    int n = 1;

    int expected[1] = {1};

    merge(nums1, 1, m, nums2, 1, n);
    TEST_ASSERT_EQUAL_INT_ARRAY(expected, nums1, 1);
}

void test_example4(void)
{
    int nums1[8] = {2, 2, 3, 0, 0, 0, 0, 0};
    int m = 3;
    int nums2[5] = {1, 2, 2, 5, 6};
    int n = 5;

    int expected[8] = {1, 2, 2, 2, 2, 3, 5, 6};

    merge(nums1, 8, m, nums2, 5, n);
    TEST_ASSERT_EQUAL_INT_ARRAY(expected, nums1, 8);
}

int main(void)
{
    UNITY_BEGIN();
    RUN_TEST(test_example1);
    RUN_TEST(test_example2);
    RUN_TEST(test_example3);
    RUN_TEST(test_example4);
    return UNITY_END();
}
