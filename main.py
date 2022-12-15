AccountStatus = input("Login Or Register (Case Sensetive)\n")
if(AccountStatus == "Login"):
  UserNameRegister = input("Please Enter UserName: ")
  PasswordRegister = input("Please Enter Password: ")
  savefile = open("save.txt", "r")
  for line in savefile:
    userinf = line.split("whatwhowherewhyhowuser23")
    if(UserNameRegister == userinf[0] and PasswordRegister == userinf[1]):
      UserLoggedIn = True
      break 
    else:
      
      UserLoggedIn = False
  savefile.close()  



  if(UserLoggedIn == True):
    print("Hello, "+UserNameRegister+"!")
    print("Welcome to the system!")
  else:
    print("Username and/or password invalid!")
elif(AccountStatus == "Register"):
  
  UserNameRegister = input("Please Enter In A Username: ")
  PasswordRegister = input("Please Enter In A Password: ")
  savefile = open("save.txt", "a")
  savefile.write("\n"+UserNameRegister+"whatwhowherewhyhowuser23"+PasswordRegister)
  savefile.close()
  print("You Are Sucessfully Registered!")
  
  
  
