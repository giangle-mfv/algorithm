you have just rolled a dice sevaral times. The N roll results that you remember are described by an array A. However there are F rolls whose results you have forgotten. The arithmetric mean of all the roll results (the sum of all roll results divided by the number of rolls) equals M
What are the possible results of the missing rolls?
write the function:
def solution (A, F, M)
that, given an arrray A of length N, an integer F and an integer M, returns an array containing possible results of the missed rolls. The returned array should contain F integers from 1 to 6 (valid dice rolls). If such an array does not exist then the function should return [0]
Examples:
1. A = [3,2,4,3], F = 2, M=4. Function should return [6,6]. the arithmetic mean of all the rolls is (3+2+4+3+6+6)/6 = 4
2. A = [1,5,6], F = 4, M = 3, function should return [2,1,2,4] or [6,1,1,1]
3. A = [1,2,3,4], F= 4, M= 6. Function should return [0]. It is not possible to abtain such a mean.
4. A = [6,1], F = 1, M=1. Function should return [0]. It is not possible to abtain such a mean.
write an efficient algorithm for the followings assumptions:
 + N and F are intergers within the range [1..1000000]
 + each element of array A in an interger within the range [1..6];
 + M is an interger within the range [1..6]