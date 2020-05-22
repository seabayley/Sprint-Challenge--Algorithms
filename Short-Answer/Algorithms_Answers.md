#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This function is Linear O(n). As n increases, the number of iterations required to complete increases directly with n. For instance, if n = 2, 2 iterations are required. If n = 3, 3 iterations are required. if n = 5, 5 iterations are required and so on.

b) This function is logarithmic. O(log n). As n increases, the number of iterations required increases at a much slower rate than n. For example, here is a list of of required iterations considering that the first number in the list is n = 1, and each successive number is an increment of n. 2, 2, 3, 3, 4, 4, 4, 4...and so on, when n = 128, only 8 iterations are required. N must double to increase required iterations by 1.

c) This function is Linear O(n). Required iterations are always equal to n as each recursive iteration reduces n by 1 until it reaches 0.

## Exercise II


In order to solve this problem I would start by dropping an egg from n/2. If it breaks, remove all floors higher than n/2 and then repeat the process with n=n/2. If it does not break, we remove all floors lower than n/2 and repeat the process.

This algorithm is Logarithmic O(log n) as we are effectively performing a recursive binary search of list [0...n] until we discover the correct floor.