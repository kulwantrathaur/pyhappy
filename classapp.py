"""
Example 2:
"""

class Employee:
    """
    Class Emp
    """
    def __init__(self):
        print("Employee")

class Manager(Employee):
    """
    Class Manager
    """
    def __init__(self):
        print("Manager")
        super().__init__()

Manager()
