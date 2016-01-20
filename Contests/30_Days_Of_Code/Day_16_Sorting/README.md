<h3>Problem Statement</h3>

Start learning about Exceptions in Day 16's video or just jump into this sorting challenge!

Sorting is an important basic algorithmic concept used to organize data so coders can better solve problems. You may find our interactive article on widely-used sorting algorithms and this article on Insertion Sort helpful in solving today's problem.

The absolute difference between two integers, a and b, is |a−b|. The minimum absolute difference between two integers in a list A of positive integers, is the smallest absolute difference between any two integers in A.

Given a list A={a0,a1,…,aN−1} of unsorted integers, find and print the pair (or pairs) of elements having the minimum absolute difference.

Note: More than one pair of elements may have the same absolute difference.

<h5>Input Format</h5>

The first line contains a single integer N, denoting the length of list A. 
The second line contains N space-separated integers, a0,a1,…,aN−1, representing the elements in A.

<h6>Constraints</h6>

2≤N≤2×105
−107≤Ai≤107
Ai≠Aj,where 0≤i<j≤N−1

<h5>Output Format</h5>

Print the space-separated pair of elements having the minimum absolute difference in ascending order. If more than one pair meets this criterion, print them consecutively, separated by a space, in ascending order on a single line. Because we are printing space-separated pairs, some elements may appear more than once in your output.

<h6>Sample Input 1</h6>

10
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 

<h6>Sample Output 1</h6>

-20 30

<h6>Explanation </h6>

The minimum absolute difference is 50 (ABS(30−(−20))=50). The only pair having this difference is (−20,30).

<h6>Sample Input 2</h6>

12
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470 

<h6>Sample Output 2</h6>

-520 -470 -20 30

<h6>Explanation</h6> 

Our minimum absolute difference is 50. The pairs (−470,−520) and (−20,30) both have this difference.

<h6>Sample Input 3</h6>

4
5 4 3 2

<h6>Sample Output 3</h6>

2 3 3 4 4 5

<h6>Explanation </h6>

Our minimum absolute difference is 1. The pairs (2,3), (3,4), and (4,5) all have this difference. Notice that 3 and 4 appear multiple times, because they are components of more than one pair.

Note: Recall that pairs in the output must be printed in ascending order.

<h5>Result</h5>

Work perfectly!