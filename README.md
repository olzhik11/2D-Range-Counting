# 2D-Range-Counting

2D range counting is the algorithm that counts the number of **points** that are within the given **rectangle**. 
Here I'm using the 2D range tree data structure to solve this problem.

## Input

**Points** - are given as the list of points: [[x1, y1], [x2, y2], [x3, y3], ..., [xN, yN]]

**Rectangle** - is the list of 2 lists where each represents x and y boundaries: [[x1, x2], [y1, y2]]

## Output

Output is the number of points that lay within the given rectangle'

## Complexity

* The time to build a such tree takes O(nlog(n))
* Time complexity of Quering is O(log^2(n) + k)

## Usage Examples
* In the main you can adjust the set of points. The result can be invoked by initializing object of class 
**Solution** and calling **.query** with set of **points** as argument.
