# our third program To-Do List application.
class Todo:
  def __init__(self, name):
    self.name = name
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def remove_task(self, task):
    self.tasks.remove(task)

  def save(self):
    with open(self.name + '.pkl', 'wb') as f:
      pickle.dump(self, f)

  def load(self):
    with open(self.name + '.pkl', 'rb') as f:
      return pickle.load(f)

def main():
  todo = Todo('my_todo_list')
  while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. Save")
    print("4. Load")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
      task = input("Enter task: ")
      todo.add_task(task)
    elif choice == '2':
      task = input("Enter task to remove: ")
      todo.remove_task(task)
    elif choice == '3':
      todo.save()
    elif choice == '4':
      todo = todo.load()
    elif choice == '5':
      break
    else:
      print("Invalid choice")

  print("Exiting program...")

if __name__ == "__main__":
  main()
