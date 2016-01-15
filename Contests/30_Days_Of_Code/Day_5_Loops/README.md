<h3>Problem Statement</h3>

Welcome to Day 5! Check out the video review of loops here, or just jump right into the problem.

In this problem you will test your knowledge of loops. Given three integers a, b, and N, output the following series:

a+20b,a+20b+21b,......,a+20b+21b+...+2N−1b
<h5>Input Format</h5>

The first line will contain the number of testcases T. Each of the next T lines will have three integers, a, b, and N.

<h6>Constraints</h6>

0≤T≤500
0≤a,b≤50
1≤N≤15

<h5>Output Format</h5>

Print the answer to each test case in a separate line.

<h6>Sample Input</h6>

2    
5 3 5
0 2 10

<h6>Sample Output</h6>

8 14 26 50 98
2 6 14 30 62 126 254 510 1022 2046

<h6>Explanation</h6>

There are two test cases. 
In the first case: a=5, b=3 ,N=5 
1st term =   5+(20×3)=8 
2nd term = 5+(20×3)+(21×3)=14 
3rd term =  5+(20×3)+(21×3)+(22×3)=26 
4th term =  5+(20×3)+(21×3)+(22×3)+(23×3)=50 
5th term =  5+(20×3)+(21×3)+(22×3)+(23×3)+(24×3)=98

<h5>Result</h5>

Work perfectly!