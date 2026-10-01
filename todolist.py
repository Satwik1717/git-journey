print("===================== TO DO LIST ==========================")
print("1 . add a task")
print("2 . view a task")
print("3 . remove a task")
print("4 . quit")

task=[]
while True :
    while True:
        try:
            a=int(input("choose an option : "))
            break
        except ValueError:
            print("wrong input, try again")

    match a :
        case 1:
            t=input("Task : ")
            task.append(t)
        case 2 :
            if len(task)!=0:
                for index,tasks in enumerate(task,start=1):
                    print(index,tasks)
            else : print("no tasks yet")
        case 3 :
            while True:
                    try:
                        pop=int(input("which one to remove : "))
                        break
                    except (ValueError):
                        print("wrong input , try again")
                        
            if 1<= pop <= len(task):
                task.pop(pop-1)
                print("deleted")
            else : print("doesnt exist")
        case 4 :
            break
        case _:
            print("not valid\n")

print("================== END ====================*")




