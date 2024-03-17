# Lockboxes

## Must Know
- For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here’s a list of concepts and resources that will be instrumental in tackling this project:

---

# Concept Needed:

1. Lists and List Manipulation:
    - Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
    - [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

2. Graph Theory Basics:
    - Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.
    - [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)

3. Algorithmic Complexity:
    - Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.
    - [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)

4. Recursion:
    - Some solutions might require a recursive approach to traverse through the boxes and keys.
    [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

5. Queue and Stack:
    - Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.
    - [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)

6. Set Operations:
    - Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
    - [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)


# Additional Resources
- [Mock Technical Interview](https://www.youtube.com/watch?v=V8DGdPkBBxg)



# Tasks
```py
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

1. Prototype: def canUnlockAll(boxes)
2. boxes is a list of lists
3. A key with the same number as a box opens that box
4. You can assume all keys will be positive integers
    a. There can be keys that do not have boxes
5. The first box boxes[0] is unlocked
6. Return True if all boxes can be opened, else return False



carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

```

```py
carrie@ubuntu:~/0x01-lockboxes$
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```
 


 ---



 # Solution

 ```py

 def canUnlockAll(boxes):
    if not boxes or type(boxes) is not list:
        return False

    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
 ```

