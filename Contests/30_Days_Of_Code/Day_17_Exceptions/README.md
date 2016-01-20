<h3>Problem Statement</h3>

Welcome to Day 17! Learn how to use try-catch blocks in Day 16 and how to create your own exceptions in Day 17 or just jump right into the problem.

Create a class Calculator which consists of a single method power(int,int). This method takes two integers, n and p, as parameters and finds np. If either n or p is negative, then the method must throw an exception which says "n and p should be non-negative".

Code for handling Input/Output is already provided in the editor. Please read the partially completed code in the editor and complete it.

Note: The class Calculator mustn't be public.

No need to worry about constraints, there won't be any overflow if your code is correct.

If you enjoyed this challenge, here's a java only Exception Challenge

<h5>Input Format</h5>

First line contains T, the number of test cases. Next T lines contain two integers n and p separated by a space.

<h5>Output Format</h5>

Output T lines. For each test case if n and p are positive then print np else print "n and p should be non-negative" without quotes.

<h6>Sample Input</h6>

4
3 5
2 4
-1 -2
-1 3

<h6>Sample Output</h6>

243
16
n and p should be non-negative
n and p should be non-negative

<h6>Explanation</h6>

T=4 
In the first test case both integers are positive hence the output is 35=243 
In the second test case both integers are positive hence the output is 24=16 
In the third test case both the integers are negative hence the output is "n and p should be non-negative" 
In the fourth test case n is negative hence the output is "n and p should be non-negative"

<h5>Result</h5>

Work perfectly!