"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # Your implementation here
    unique_ids = set(product_ids)
    if len(unique_ids) == len(product_ids):
        return False
    else: 
        return True

#A set is a good structure choice for this problem because it ignores duplicate values. because we know this, we can compare the
#set to the original list of numbers. If they are the same size, this means the set function did not remove any duplicates meaning there were not any duplicates
#therefor we can return False. If the lengths are different, this means the set operator removed a duplicate value meaning we can return true
    


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        # Your initialization here
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)



    def remove_oldest_task(self):
        if not self.task:
            return None
        else:
            return self.task.pop(0)
    

    #this was my first attempt. I used a list but I think a queue may be faster. While appending to the end of a list is relatively fast O(1) time
    # removing from the front of the list is slow O(n) because the other elements now have to be slid down in the array. 

    # i beleive you should use a queue. but the built in structure of the file did not seem like we should be using a queue implemented with a linked list because there was not
    #a node class. there was only a TaskQueue class.
    #i beleive there is a deque built into python that would work. 


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.integers = []

    def add(self, value):
       self.integers.append(value)

    def get_unique_count(self):
        self.unique_int = list(set(self.integers))
        return len(self.unique_int)

#fast verison

'''

class UniqueTracker:
    def __init__(self):
        self.unique_ints = set()

    def add(self, value):
        self.unique_ints.add(value)  # set ignores duplicates automatically

    def get_unique_count(self):
        return len(self.unique_ints)

'''
#a set is used because it already returns the unique values. Then we just count the length of the set for the total number
#However my version is slow because I am storing them into a list every time  get_unique_count is called. this is slow 
# you can convert directly into a set but I did not know you could do this. I put a faster version in comments. 