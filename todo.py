class TodoList :

    def __init__(self):
        self.TodoList = []

    def add_item(self,item):
        self.TodoList.append(item)

    def view_item(self):
        return self.TodoList

    def remove_item(self,index):
        try:
            removed_item = self.TodoList.pop(index)
            return "removed: {}".format (removed_item)
        except  IndexError :
            return "Invalid index.Item not removed"

    def Todolist_actions():
         todo_list = TodoList()

         while True:

            print("\nTodo List Menu:")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. View Items")
            print("4. Exit")

            choice = input("enter your choice (1-4):")


            if choice==1 :
                item = input("enter your task:")
                todo_list.add_item(item)
            elif choice == "2":
                try:
                    index = int(input("Enter the index of the item to remove: "))
                    result = todo_list.remove_item(index)
                    print(result)
                except IndexError:
                    print("Invalid input. Please enter a valid index.")
            elif choice == "3":
                  items = todo_list.view_item()
                  print("To-Do Items:")
                  for i, item in enumerate(items):
                      print("{0}. {1}".format(i,item))

            elif choice == "4":
                print("exit")
                break
            else :
                print("invalid choice")







    
