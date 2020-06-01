# solution (needs to go between the 2 your code here lines!)

while True:
    email = input("email address?")
    r, err_str = is_valid(email)

    if r == None:
        print(email, "is valid!")
        break
    
    # error
    attempts_left -= 1

    # no attempts left - bail out 
    if attempts_left == 0:
        gave_up = True
        print("No attempts left, bailing out")
        break

    print(email, "is invalid!")
    print("Reason:", err_str)
    print(f"Try again, {attempts_left} attempts left")
