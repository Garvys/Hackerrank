<h3>Problem Statement</h3>

Welcome to Day 22! Check out a video review of binary search trees and heaps here, or just jump right into the problem.

The height of a binary tree is the number of nodes on the largest path from root to any leaf. You are given a pointer root pointing to the root of a binary search tree. Return the height of the tree. 
You only have to complete the function getHeight given in the editor.

<h5>Input Format</h5>

First line contains T, the number of test cases. Next T lines contain an integer data to be added to the binary search tree.

<h5>Output Format</h5>

Output the height of the binary search tree.

<h6>Sample Input</h6>

7
3
5
2
1
4
6
7

<h6>Sample Output</h6>

4

<h6>Explanation</h6>

The Binary Search tree formed with the given values is

      3  
     /  \
    2    5
   /    /  \
  1    4    6
             \
              7
The maximum length root to leaf path is 3->5->6->7. There are 4 nodes in this path. Therefore the height of the binary tree = 4.

<h5>Result</h5>

Work perfectly!
