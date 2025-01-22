
while True:
    # get user input and remove space charaters from this
    user_choice = input("enter add, show, edit, complete or exit:")
    user_choice = user_choice.strip()

    match user_choice:
        case 'add':     
            #file = open('todos.txt', 'r')
            #todos = file.readlines()
            #file.close()
            with open('todos.txt', 'r') as file:     #with as context manager, no need to close file
                todos = file.readlines()

            user_input = input("enter a todo:") + "\n"
            todos.append(user_input)

            #file2 = open('todos.txt', 'w')
            #file2.writelines(todos)
            #file2.close()


        case 'show' | 'display':            
            with open('todos.txt', 'r') as file:     #with as context manager, no need to close file
                todos = file.readlines()   

            new_todos = [item.strip("\n") for item in todos]  #list comprehension
            todos = new_todos
            
            for index, item in enumerate(todos):    #item = item.strip('\n')
                item = item.title()                 
                print(f"{index+1}-{item}")          #print(f"{index+1}-{item.strip('\n')}")         
                                                    

        case 'edit':
             with open('todos.txt', 'r') as file:     #with as context manager, no need to close file
                todos = file.readlines()

             number = int(input("enter the number to be edited:"))
             number = number-1
             todos[number] = input("enter a new to do") + "\n"
            
             with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
            
        case 'complete':            
            with open('todos.txt', 'r') as file:     #with as context manager, no need to close file
                todos = file.readlines()

            number = int(input("enter the number to be completed:"))
            donetask = todos.pop(number-1)

            print(f"the item {donetask.strip("\n")} is now finished. well done")
            
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

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


