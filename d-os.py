import time
time.sleep(4)
print("verifying secure boot")
time.sleep(4)
print("verifying kernel")
time.sleep(4)
print("boot pass successfully!")

import time,replit,random
from PyDictionary import PyDictionary
dictionary = PyDictionary()

running = True
storage = 95
maximum_storage = 95
installed_packages = 0
i = 0

installed_echo = False
installed_calc = False
installed_dictionary = False
installed_trendbrowser = False
installed_dwhub = False
installed_webbrowser = False

trendbrowser_running = False

print(dictionary.meaning('cake'))
time.sleep(0.1)
replit.clear()
print()
print("Running D-DOS v1.1 (security patch: 1 November 2023)")
print("Type 'help' for a list of available commands")
print()

while running:
  cmd = input("> ")
  
  if cmd == "help":
    print()
    print("---------------")
    print("D-OS Help Menu")
    print("---------------")
    print("help - Display this menu")
    print("clear - Clear the console")
    print("storage - View amount of storage remaining.")
    print("install <package> - Install a certain package")
    print("uninstall <package> - Uninstall a certain package")
    print("uninstall all - Uninstall all packages")
    print("package list all - List all available packages")
    print("package list installed - List all installed packages")
    print("package info <package> - View information about a certain package")
    print()

  if cmd == "install echo":
    if storage >= 2.5:
      if installed_echo:
        print()
        print("Error: Echo is already installed!")
        print()
      else:
        print()
        print("Installing echo...")
        time.sleep(random.randint(5, 10))
        print("Installed echo!")
        storage -= 2.5
        print("You have " + str(storage) + "kb/" + str(maximum_storage) + "kb of storage left.")
        installed_echo = True
        print()
    else:
      print()
      print("Not enough storage remaining to install echo! Uninstall some programs to free up space on your device.")
      print()

  if cmd == "uninstall echo":
    if installed_echo:
      print()
      print("Uninstalling echo...")
      time.sleep(random.randint(5, 10))
      print("Uninstalled echo!")
      storage += 2.5
      print("You have " + str(storage) + "kb/" + str(maximum_storage) + "kb of storage left.")
      installed_echo = False
      print()
    else:
      print()
      print("Error: Echo is not installed!")
      print()

  if cmd == "install calc":
    if storage >= 11:
      if installed_calc:
        print()
        print("Error: Calc is already installed!")
        print()
      else:
        print()
        print("Installing calc...")
        time.sleep(random.randint(6, 12))
        print("Installed calc!")
        storage -= 11
        print("You have " + str(storage) + "kb/" + str(maximum_storage) + "kb of storage left.")
        installed_calc = True
        print()
    else:
      print()
      print("Error: Not enough storage remaining to install calc! Uninstall some programs to free up space on your device.")
      print()

  if cmd == "uninstall calc":
    if installed_calc:
      print()
      print("Uninstalling calc...")
      time.sleep(random.randint(6, 12))
      print("Uninstalled calc!")
      storage += 11
      print("You have " + str(storage) + "kb/" + str(maximum_storage) + "kb of storage left.")
      installed_calc = False
      print()
    else:
      print()
      print("Error: Calc is not installed!")
      print()
    
  if cmd == "install dictionary":
    if storage >= 15:
      if installed_dictionary:
        print()
        print("Error: Dictionary is already installed!")
        print()
      else:
        print()
        print("Installing dictionary...")
        time.sleep(random.randint(10, 16))
        print("Installed dictionary!")
        storage -= 15
        print("You have " + str(storage) + "kb/" + str(maximum_storage) + "kb of storage left.")
        installed_dictionary = True
        print()
    else:
      print()
      print("Error: Not enough storage remaining to install dictionary! Uninstall some programs to free up space on your device.")
      print()

  if cmd == "uninstall dictionary":
    if installed_dictionary:
      print()
      print("Uninstalling dictionary...")
      time.sleep(random.randint(6, 12))
      print("Uninstalled dictionary!")
      storage += 15
      print("You have " + str(storage) + "kb/" + str(maximum_storage) + "kb of storage left.")
      installed_dictionary = False
      print()
    else:
      print()
      print("Error: Dictionary is not installed!")
      print()

  if cmd == "install trendbrowser":
    if storage >= 22:
      if installed_trendbrowser:
        print()
        print("Error: Trendbrowser is already installed!")
        print()
      else:
        print()
        print("Installing trendbrowser (this may take a while)...")
        time.sleep(random.randint(13, 20))
        print("Installed trendbrowser!")
        storage -= 22
        print("You have " + str(storage) + "kb/" + str(maximum_storage) + "kb of storage left.")
        installed_trendbrowser = True
        print()
    else:
      print()
      print("Error: Not enough storage remaining to install trendbrowser! Uninstall some programs to free up space on your device.")
      print()

  if cmd == "uninstall trendbrowser":
    if installed_trendbrowser:
      print()
      print("Uninstalling trendbrowser...")
      time.sleep(random.randint(6, 12))
      print("Uninstalled trendbrowser!")
      storage += 22
      print("You have " + str(storage) + "kb/" + str(maximum_storage) + "kb of storage left.")
      installed_trendbrowser = False
      print()
    else:
      print()
      print("Error: Trendbrowser is not installed!")
      print()

  if cmd == "install dwhub":
    if storage >= 15:
      if installed_dwhub:
        print()
        print("Error: Dwhub is already installed!")
        print()
      else:
        print()
        areYouSure_dwhub = input("Dwhub is from an unofficial source and may affect system security. continue anyway? (Y/N): ")
        print()
        if areYouSure_dwhub == "y" or areYouSure_dwhub == "Y":
          print("Installing dwhub...")
          time.sleep(random.randint(10, 13))
          print("Installed dwhub!")
          storage -= 15
          print("You have " + str(storage) + "kb/" + str(maximum_storage) + "kb of storage left.")
          installed_dwhub = True
          print()
    else:
      print()
      print("Error: Not enough storage remaining to install trendbrowser! Uninstall some programs to free up space on your device.")
      print()

  if cmd == "install webbrowser":
    if storage >= 20:
      if installed_webbrowser:
        print()
        print("Error: Webbrowser is already installed!")
        print()
      else:
        print()
        print("Installing webbrowser (this may take a while)...")
        time.sleep(random.randint(7, 14))
        print("Installed webbrowser!")
        print()
        installed_webbrowser = True
    else:
      print()
      print("Error: Not enough storage remaining to install webbrowser! Uninstall some programs to free up space on your device.")

  if cmd == "uninstall dwhub":
    if installed_dwhub:
      print()
      print("Uninstalling dwhub...")
      time.sleep(random.randint(6, 10))
      print("Uninstalled dwhub!")
      storage += 15
      print("You have " + str(storage) + "kb/" + str(maximum_storage) + "kb of storage left.")
      installed_dwhub = False
      print()
    else:
      print()
      print("Error: Dwhub is not installed!")
      print()

  if cmd == "package list all":
    print()
    print("----------------------")
    print("All Available Packages")
    print("----------------------")
    print("echo")
    print("calc")
    print("dictionary")
    print("trendbrowser")
    print()

  if cmd == "package list installed":
    print()
    print("------------------")
    print("Installed Packages")
    print("------------------")
    if installed_echo:
      print("echo")
    if installed_calc:
      print("calc")
    if installed_dictionary:
      print("dictionary")
    if installed_trendbrowser:
      print("trendbrowser")
    if installed_dwhub:
      print("dwhub (Unofficial)")
    if not installed_echo and not installed_calc and not installed_dictionary and not installed_trendbrowser and not installed_dwhub and not installed_webbrowser:
      print("None")
    print()

  if cmd == "package info echo":
    print()
    print("Package name: Echo")
    print("Function: Echo gets user input and echoes it back as output.")
    print("File size: 2.5kb")
    print()

  if cmd == "package info calc":
    print()
    print("Package name: Calc")
    print("Function: Calc is a simple calculator capable of answering addition, subtraction, multiplication and division equations.")
    print("File size: 11kb")
    print()

  if cmd == "package info dictionary":
    print()
    print("Package name: Dictionary")
    print("Function: Dictionary outputs the definition of a word inputted by the user.")
    print("File size: 15kb")
    print()

  if cmd == "package info trendbrowser":
    print()
    print("Package name: Trendbrowser")
    print("Function: Trendbrowser is a simple web browser which lists all things that are trending.")
    print("File size: 22kb")
    print()

  if cmd == "echo" and installed_echo:
    print("----")
    print("Echo")
    print("----")
    text = input("Text: ")
    print("Output: " + str(text))
    print()

  if cmd == "calc" and installed_calc:
    print()
    print("----------")
    print("Calculator")
    print("----------")
    a = input("First number: ")
    b = input("Second number: ")
    op = input("Operator (+, -, /, *): ")
    if op == "+":
      result = int(a) + int(b)
      print(str(a) + " + " + str(b) + " = " + str(result))
    elif op == "-":
      result = int(a) - int(b)
      print(str(a) + " - " + str(b) + " = " + str(result))
    elif op == "/":
      result = int(a) / int(b)
      print(str(a) + " / " + str(b) + " = " + str(result))
    elif op == "*":
      result = int(a) * int(b)
      print(str(a) + " * " + str(b) + " = " + str(result))
    else:
      print("Error: Invalid operator") 
    print()

  if cmd == "dictionary" and installed_dictionary:
    print()
    word = input("Word: ")
    print(dictionary.meaning(word))
    print()

  if cmd == "trendbrowser" and installed_trendbrowser:
    trendbrowser_running = True
    print()
    print("------------")
    print("Trendbrowser")
    print("------------")
    print("Trending (select an option):")
    print("1) Fortnite Battle Royale")
    print("2) Logan Paul vs KSI")
    print("3) Dark web")
    print("4) HOS")
    print("5) J-DOS")
    print("-------------------------")
    print("6) Exit")
    print()
    
    while trendbrowser_running:
      trendbrowser_option = input("Option: ")

      if trendbrowser_option == "1":
        print()
        print("Fortnite Battle Royale is an online multiplayer battle royale game where you have to roam around a map, searching for guns / weapons. 100 players maximum are in a game. Last person standing wins. A storm is closing into the map as the game progresses. The storm is deadly and takes off a certain amount of health every second. The storm damage increases throughout the game.")
        print()
      elif trendbrowser_option == "2":
        print()
        print("KSI vs. Logan Paul is a two-part white-collar amateur boxing match between two YouTubers, KSI and Logan Paul, who are British and American, respectively. The first of the two parts was held on 25 August 2018 at 8:30 PM BST in the Manchester Arena, Manchester, England, and was streamed on YouTube's pay-per-view platform. The fight has been labeled the largest event in YouTube history and the largest ever amateur boxing fight. The fight ended in a majority draw, with two judges scoring it 57–57 and the other 58–57 in favour of KSI. The second fight is reportedly set to take place in February 2019 at an undetermined United States venue, provided neither KSI nor Logan Paul opt out. However, KSI has requested for the second fight to be postponed until May 2019.")
        print()
      elif trendbrowser_option == "3":
        print()
        print("Do you want to make your operating system more powerful than before? Are you looking to download a unofficial console capable of many things onto your OS? Are you looking to overclock the amount of storage your os has? Then you have come to the right place. Download our app named 'Dark Web Hub' using 'install dwhub'. it can bypass system security.")
        print()
      elif trendbrowser_option == "4":
        print()
        print("D-OS is a text based operating system made by Harvey H and modified by blank9485. published on repl.it. It has many features and extra apps available to download onto it, including a 2d terrain generator!")
        print()
      elif trendbrowser_option == "5":
        print()
        print("could load page. ERROR!")
        print()
      elif trendbrowser_option == "6":
        trendbrowser_running = False
        print()
      else:
        print()
        print("Invalid option!")
        print()

  if cmd == "dwhub" and installed_dwhub:
    print()
    print("------------")
    print("Dark Web Hub")
    print("------------")
    print("Select an option experimental:")
    print("1) Overclock storage")
    print("2) Custom console")
    print("3) Exit")
    print()
    dwhub_option = input("Option: ")

    if dwhub_option == "1":
      print()
      print("Warning: SETTING A HIGHER INPUT COULD BRICK YOUR DEVICE!.")
      print()
      print("-----------------")
      print("Overclock Options")
      print("-----------------")
      overclock_power = int(input("Power (1-5): "))
      if overclock_power > 0 and overclock_power < 6:
        print()
        print("Selected overclock power: " + str(overclock_power))
        print()
        overclock_start = input("Do you want to start the overclock? (Y/N): ")
        print()
        if overclock_start == "y" or overclock_start == "Y":
          if overclock_power == 1:
            print("Overclocking storage...")
            time.sleep(random.randint(3, 5))
            failed_number = random.randint(1, 6)
            if failed_number == 3:
              print ("UNABLE TO LOAD D-OS! YOUR DEVICE IS CORRUPTED! .")
              while True:
                input()
            else:
              print("Successfully overclocked storage to 120kb!")
              print()
              maximum_storage = 120
              storage = maximum_storage + storage - 95
          if overclock_power == 2:
            print("Overclocking storage...")
            time.sleep(random.randint(6, 10))
            failed_number = random.randint(2, 6)
            if failed_number == 3:
              print ("UNABLE TO LOAD D-OS! YOUR DEVICE IS CORRUPTED!.")
              while True:
                input()
            else:
              print("Successfully overclocked storage to 140kb!")
              print()
              maximum_storage = 140
              storage = maximum_storage + storage - 95
          if overclock_power == 3:
            print("Overclocking storage...")
            time.sleep(random.randint(10, 14))
            failed_number = random.randint(2, 5)
            if failed_number == 3:
              print("UNABLE TO LOAD D-OS! YOUR DEVICE IS CORRUPTED!")
              while True:
                input()
            else:
              print("Successfully overclocked storage to 160kb!")
              print()
              maximum_storage = 160
              storage = maximum_storage + storage - 95
          if overclock_power == 4:
            print("Overclocking storage...")
            time.sleep(random.randint(14, 18))
            failed_number = random.randint(1, 3)
            if failed_number == 2:
              print("UNABLE TO LOAD D-OS! YOUR DEVICE IS CORRUPTED!.")
              while True:
                input()
            else:
              print("Successfully overclocked storage to 200kb!")
              print()
              maximum_storage = 200
              storage = maximum_storage + storage - 95
          if overclock_power == 5:
            print("Overclocking storage...")
            time.sleep(random.randint(18, 22))
            failed_number = random.randint(1, 2)
            if failed_number == 2:
             print("UNABLE TO LOAD D-OS! YOUR DEVICE IS CORRUPTED!")
  
              
        else:
          print("Overclock cancelled.")
          print()
      else:
        print("Error: Overclock cancelled due to invalidinput.")
        print()
    if dwhub_option == "2":
      print()
      print("----------------")
      print("Dark Web Console")
      print("----------------")
      print("Use 'help' to view a list of available commands.")
      print()
      dwcmd = input("-> ")

      while dwcmd != "exit":
        dwcmd = input("-> ")

        if dwcmd == "help":
          print()
          print("---------")
          print("Help Menu")
          print("---------")
          print("help - Show this menu")
          print("list web insecure - List all insecure websites")
          print("webscrape <weblink> - List all databases in a website")
          print("webscrape -o <number> <weblink> - List all items in the selected database")
          print("webscrape -o <number> -a <number> <weblink> - List available info from a selected database")
          print("exit - Exit to the OS")
          print()

        if dwcmd == "list web insecure":
          print()
          print("-----------------")
          print("Insecure Websites")
          print("-----------------")
          print("fail!")
          print()

        if dwcmd == "webscrape http://goggle.com/?v=37653":
          print()
          print("Scraping website...")
          time.sleep(random.randint(7, 13))
          print()
          print("Fetched 3 results:")
          print("1) Credentials_Database")
          print("2) Ads")
          print("3) ???")
          print()

        if dwcmd == "webscrape -o 1 fail":
          print()
          print("Scraping DB...")
          time.sleep(random.randint(5, 7))
          print()
          print("Found 3 options:")
          print("1) lolerilol:password123")
          print("2) admin:admin675")
          print("3) owner:owner777")
          print()

        if dwcmd == "webscrape -o 2 fail":
          print()
          print("Scraping DB...")
          time.sleep(random.randint(5, 7))
          print()
          print("Found 4 options:")
          print("1) Brooklyn's Dog Toys & Treats")
          print("2) Goggle Search Engine")
          print("3) Sunrise Flight Simulator")
          print("4) Nanosoft Publisher")
          print()

        if dwcmd == "webscrape -o 2 -a 1 fail":
          print()
          print("Scraping selected option...")
          time.sleep(random.randint(5, 7))
          print()
          print("Found 1 Sublink:")
          print("1) fail")
          print()

        if dwcmd == "webscrape -o 2 - a 2 hle.m/?v=37653":
          print()
          print("Scraping selected option...")
          time.sleep(random.randint(5, 7))
          print()
          print("Found 1 Sublink:")
          print("1) fail")
          print()

        if dwcmd == "webscrape -o 2 -a 3 fail":
          print()
          print("Scraping selected option...")
          time.sleep(random.randint(5, 7))
          print()
          print("Found 1 Sublink:")
          print("1) ://1/adver")
          print()

        if dwcmd == "webscrape -o 2 -a 4 fail":
          print()
          print("Scraping selected option...")
          time.sleep(random.randint(5, 7))
          print()
          print("Unable to fetch sublinks (the link is invalid)")
          print()

      print()
    if dwhub_option == "3":
      print()

  if cmd == "clear":
    replit.clear()

  if cmd == "storage":
    print()
    print("Storage remaining: " + str(storage) + "kb/" + str(maximum_storage) + "kb")
    print()