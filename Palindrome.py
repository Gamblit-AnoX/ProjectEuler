i=0
j=0
goal=0
for i in range(999):
    i+=1
    for j in range(999):
        j+=1
        mafia=i*j
        mafia2=str(mafia)
        if(mafia2==mafia2[::-1]):
            if(mafia>goal):
                goal=mafia
                print(goal)    
       
                    
                    
                
                    
                
