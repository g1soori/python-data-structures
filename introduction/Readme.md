BigO
- Use for comparing two codes
- Time complexity
- Space complexity. Ex- lesser memory
- Omega beta and omicron
-  O(n) O(n2) O(1) O(log n)
- o(1) most efficient while o(n2) least efficient
- o(n2) - loop within a loop
- o(n) - propotional, a loop
- o(log n) - devide and conquer
- o(1) - constant

integers are immutable while dictionaries are mutable.
m = 10
n = m
n = 3 # This will save value 3 in new memory location

m = {'key':3}
n = m
n['key'] = 5 # This updates original m dictionary

Data Structures

1. Linked lists
- linked lists doesn't have indexes
- They are not contiguously stored in memory compared to lists

2. Doubly linked Lists

3. Stacks and Queues

4. Trees
- Binary search trees considered O(log n) with perfect or complete trees but O(n) in worst case (= linked list)

5. Hash Trees

6. Graphs
- Graphs can be represented as adjacency matrix or adjacency list
- Adjacency list is less space complexity compared to matrix
- Adjacency list prefered over matrix


Algorithms
1. Recursion
- Function call itself until resolves
- Everytime it does the same job
- Each time runs it, makes the problem smaller
- base case is where function exit from itself
- recursive case where function call itself
- its important to have base case otherwise stack overflow will occur

2. Basic Sorts
i. Bubble Sort
- Choose item and compare it with next item and move if bigger
ii. Selection Sort
- Use indexes to sort
- Start from min index and find lesser than that and swap values
iii. Insertion sort
- Start from 2nd item and compare backward. And swap values if bigger

BigO for sorting is O(n2) but its not for almost sorted list

3. Merge sort
- Devide the list into two and sort them, then combine
- Since merge sort devide the list its space complexity is O(n)
- Time complexity 
    - Deviding list O(log n)
    - combining O(n)
    - Hence final is O(n logn)
- Above basic sorts are O(n2) hence merge sort is more efficient

4. Quick Sort
- Use 3 functions
    - swap - swap values of two indexes
    - pivot - take list, first and last indexes and return pivot after half sorting
    - merge_sort - run recursively 
- time complexity is O(nlogn) for average and best cases
- In worst case O(n2) for already sorted data

5. Tree traversal
i. breadth first search - Go by levels
ii. Depth first search - Start from all the way from bottom left of each branch
    - Preorder