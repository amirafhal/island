print("""
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████

""")
print("Welcome to my island!")
print("There are two doors in front of you. 🟥 a red door and 🟦 a blue door")
door = input("Which door do you want to open? ")
if door.lower() == "blue":
  print("""Oops! You chose the crocodile door.
Game over! 🐊🐊🐊
  """)
elif door.lower() == "red":
  print("""Great! now you entered a room.
you found three boxes: ➊ white, ➋ black, ➌ green""")
  d = input("Which box do you open? ")
  if d.lower() == "white":
    print("Oops! You opened a box filled with snakes 🐍🐍🐍")
  elif d.lower() == "green":
    print("Congratulations! You found the treasure! 💰💰💰")
    print("🎉🎉🎉🎉🎉👏👏👏👏👏👏👏👏👏👏👏👏👏👏🎊🎊🎊🎊🎊")
  elif d.lower() == "black":
    print("Oops! You opened a box filled with spiders 🕷️🕷️🕷️")
  else:
    print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")
else:
  print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")
