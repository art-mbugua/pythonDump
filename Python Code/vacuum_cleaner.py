# 0 --> CLEAN 
# 1--> NOT CLEAN
#THERE ARE TWO ROOMS A AND B 

#defining a function and introducing a goal state.

def vacuum_cleaner():
  goal = {"A":"0","B":"0"}
  cost = 0

  location = input("enter the location of the vacuum  ")
  status = input(("enter the status of " + location))
  status_complement = input("enter the status of the other room  ")
  print("Desired Location Condition " + str(goal))

  if location=="A":
    print("The vaccum is in room A")
    if status == "1":
      print("######Current state is A:Dirty######")
      goal["A"] = "0"
      cost = cost + 1 
      print("Room A has been cleaned and the cost for cleaning A room is " + str(cost))

        
      if status_complement == "1": #this is for the input of room B where it is first initiated as being dirty (1)
        print("######Current state is B:dirty######")
        print("The Vacuum Cleaner is moving right to location B")
        goal["B"] = "0"
        cost = cost + 1 
        print("Room B has been cleaned and the cost for cleaning B room is " + str(cost))

      else: 
        print("NO ACTION NEEDED AS ROOM B IS ALREADY CLEANED. THE COST IS " + str(cost))

      
    if status == "0":
        print("The location A is already Clean, The vacuum Cleaner will move to the next room")        
        if status_complement == "1":
            print("######Current state is B:dirty######")
            print("The Vacuum CLeaner is moving right to location B")
            goal["B"] = "0"
            cost = cost + 1 
            print("Room B has been cleaned and the cost for cleaning B room is " + str(cost))

        else: 
            print("NO ACTION NEEDED AS ROOM B IS ALREADY CLEANED. THE COST IS " + str(cost))

  else: 
    print("Vacuum is in Room B")
    if status == "1":
      print("######Current state is B:dirty######")
      goal["B"] = "0"
      cost = cost + 1 
      print("Room B has been cleaned and the cost for cleaning B room is " + str(cost))

        
      if status_complement == "1": # this is for the time that the room A is dirty hence it will be cleaned
        print("######Current state is A:dirty######")
        print("moving left to location A")
        goal["A"] = "0"
        cost = cost + 1 
        print("Room A has been cleaned and the cost for cleaning A room is " + str(cost))

      else: 
        print("NO ACTION NEEDED AS ROOM A IS ALREADY CLEANED. THE COST IS " + str(cost)) #this is for the time that the room A is already cleaned, there is no action that is needed

      
    if status == "0":
      print("The location B is already Clean, no cleaning action is needed")
        
      if status_complement == "1":
        print("The state of location A:dirty")
        print("The Vacuum is moving left to location A")
        goal["A"] = "0"
        cost = cost + 1 
        print("Room A has been cleaned and the cost for cleaning A room is " + str(cost))

      else: 
        print("NO ACTION NEEDED AS ROOM A IS ALREADY CLEANED. THE COST IS " + str(cost))

  print()
  print("Final goal state is " + str(goal))
  print("perfomance measurement is  " + str(cost))
        
vacuum_cleaner()