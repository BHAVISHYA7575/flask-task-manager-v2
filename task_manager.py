print("Running Task Manager")



# Task class to manage individual tasks
class Task:
    def __init__(self, name, description, completed=False):
        self.name = name
        self.description = description
        self.completed = completed
    
    def mark_completed(self):
        self.completed = True
    
    def update_task(self, new_name=None, new_description=None):
        if new_name:
            self.name = new_name
        if new_description:
            self.description = new_description

# UrgentTask class inheriting from Task, with added priority
class UrgentTask(Task):
    def __init__(self, name, description, priority="High", completed=False):
        super().__init__(name, description, completed)
        self.priority = priority
    
    def show_priority(self):
        return f"{self.name} has a priority level of {self.priority}"

# Testing the Task and UrgentTask classes
if __name__ == "__main__":
    # Create a regular task
    task1 = Task("Learn Flask", "Complete the basics of Flask framework")
    task1.mark_completed()
    print(f"Task: {task1.name}, Completed: {task1.completed}")
    
    # Create an urgent task
    urgent_task = UrgentTask("Fix bugs", "Fix critical bugs in the system", "Critical")
    print(urgent_task.show_priority())










# OOP example for task management

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"Task: {self.name}, Completed: {self.completed}"

# Create a new task
task1 = Task("Learn Flask")
task2 = Task("Fix bugs", completed=True)

# Print task details
print(task1)
print(task2)

# Mark task1 as completed and print again
task1.mark_completed()
print(task1)
