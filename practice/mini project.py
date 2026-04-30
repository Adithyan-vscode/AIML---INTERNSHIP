task=[]
def add_task():
    name = input("enter the name of task: ")
    priority = input("enter priority(high/medium/low): ")
    time = float(input("enter time required to complete (in hours: "))
    data={"name" : name ,
         "priority" : priority,
         "time" : time ,
         "status" : "pending"}
    task.append(data)
    print("task added successfully")

def view_task():
    if not task:
        print("no task available")
    for i,data in enumerate(task):
      print(f"{i+1}.{data['name']}priority:{data['priority']} time: {data['time']}hrs status: {data['status]}")
            print() 
add_task()
view_task()
   