#Profile Link: https://www.upwork.com/freelancers/~014ec66c9b52cdfc1a

PinKnockDown = 0
totalScore = 0
shot = 1
RemainingPin = 10

# Function to take a valid input
def Input():
    global PinKnockDown,RemainingPin, Probability
    PinKnockDown = int(input("Total no of pins down in the shot : "))
    if PinKnockDown > RemainingPin:
        print(f"Input should be lower than or equal to {RemainingPin}")
        Input()
    else:
        RemainingPin = RemainingPin - PinKnockDown
        
         
    return PinKnockDown


def Bowling():
    global shot, PinKnockDown, Probability, RemainingPin, totalScore
    while (shot > 0):
        shot -= 1
        print("Remaining shots = ",shot+1)
        PinKnockDown = Input()
            
        # Condition to integrate the spare logic
        try:
            if Probability <= 2:
                Probability -= 1

                if RemainingPin == 0:
                    shot += 1        
                    print("You score Spare")
                
        except:
            pass
             
        if PinKnockDown == 10:
            print("You Score Strike")
            Probability = 2
                   
        if RemainingPin == 0:
            RemainingPin = 10
        
        print("Balance pin - ",RemainingPin)
        
        # Check strike logic
        if (PinKnockDown == 10):
            shot += 2   
            totalScore += PinKnockDown
            print("Total totalScore = ",totalScore)
            return Bowling()           
            
        else:             
            totalScore += PinKnockDown
            print("Total totalScore = ",totalScore)
            return Bowling()
        
    else:
        print("Game Exit")
                   
            

Bowling()     
     
    