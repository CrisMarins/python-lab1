todo= ["study", "study a lot", "have lunch", "drink milk"]
flag=0
while flag==0 :
    com=input(( """Insert the number corresponding to the action you want to perform:
    1. insert a new task;
    2. remove a task;
    3. show all the tasks;
    4. close the program.
Your choice: """))

    j = len(todo)

    if com == "1":
        todo.append(input("type the task you want to insert "))
        print("task successfully added to the list ")

    elif com == "2":
        rem=input("type exactly the task you want to remove ")
        p=0

        for tod in todo:
            if rem == tod:
                todo.remove(rem)
                print("Task successfully removed from the list ")
                p=1
        if p==0:
            print("The task isn't in the list ")


    elif com == "3":
        print(todo)

    elif com == "4":
        flag = 1
        print("Goodbye!")

    else:
        print("Please type a number from the action menu ")

