
while True:
    user_choice = input("enter add, show, edit, complete or exit:")
    user_choice = user_choice.strip()

    match user_choice:
        case 'add':           
            
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            user_input = input("enter a todo:") + "\n"
            todos.append(user_input)

            file2 = open('todos.txt', 'w')
            file2.writelines(todos)
            file2.close()


        case 'show' | 'display':
            file3 = open('todos.txt', 'r')
            todos = file3.readlines()
            file3.close()
            
            new_todos = [item.strip("\n") for item in todos]  #list comprehension
            todos = new_todos

            for index, item in enumerate(todos):
                item = item.title()
                #item = item.strip('\n')
                print(f"{index+1}-{item}")
                #print(f"{index+1}-{item.strip('\n')}")

        case 'edit':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            number = int(input("enter the number to be edited:"))
            number = number-1
            todos[number] = input("enter a new to do")

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            
        case 'complete':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            number = int(input("enter the number to be completed:"))
            todos.pop(number-1)

            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()

        case 'exit':
            break
        case _:
            print("wrong comand")             
print("bye!")

    








#while True: 

    #todo = input(user_prompt)
    #todos.append(todo)
    #print(todos)



#print("the new todo is:", userinput)
#userinput2 = input(user_prompt)
#userinput3 = input(user_prompt)

#make a list

#todos = [userinput1, userinput2, userinput3]

#print(todos)

#print(type(userinput1))
#print(type(todos))  


