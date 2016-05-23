import time
high_score = 50
name = "Liam"
count_time = 0
z_time = 0

while True:
    print("Count to 100, with only x's.")
    print("Ready...")
    time.sleep(1)
    print("Set...")
    time.sleep(1)
    print("GO");
    
    if str(input()) == 'z':
        while count_time < 100:
            if count_time == 50:
                print("Halfway there");
                break;
            elif count_time == 100:
                print("You made it!");

        z_time += 1 
            
            
