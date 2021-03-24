
# def recipe(*item):
#   '''idk if we need a docstring for this'''
#   print(f'The items for the recipe are {item[0]} and {item[1]}!')

# recipe('eggs', 'flour', 'sugar', 'milk', 'the blood sweat and tears of AOT fans')
  # try in case they dont use an integer



class color:
   cyan = '\033[96m'
   bold = '\033[1m'
   end = '\033[0m'

def metreYard():
  try:
    x = float(input('Type a number you want to convert'))
  except ValueError:
    print('Please put in a valid number')
    x = float(input('Type a number you want to convert'))
  finally:
    print(round((x * 1.094), 3))

def kilogramPound():
  try:
    x = float(input('Type a number you want to convert'))
  except ValueError:
    print('Please put in a valid number')
    x = float(input('Type a number you want to convert'))
  finally:
    print(round((x * 2.205), 3))

def celsiusFahrenheit():
  try:
    x = float(input('Type a number you want to convert'))
  except ValueError:
    print('Please put in a valid number')
    x = float(input('Type a number you want to convert'))
  finally:
    print(round((x * 9/5) + 32, 3))

def kilometreMile():
  try:
    x = float(input('Type a number you want to convert'))
  except ValueError:
    print('Please put in a valid number')
    x = float(input('Type a number you want to convert'))
  finally:
    print(round((x / 1.609)), 3)

def menu():
  print(color.cyan + '┍━━━━━━━━༻¨:·. ✧ .·:¨༺ ━━━━━━━┑' + color.end)
  print(color.bold + 'Menu'.center(30) + color.end)
  print(color.cyan + '└━━━━━━━━༻¨:·. ✧ .·:¨༺ ━━━━━━━┘' + color.end)
  print('1. Meters to Yards')
  print('2. Kilograms to Pounds')
  print('3. Celsius to Fahrenheit')
  print('4. Kilometres/Hour to Miles/Hour')
  print('5. Exit')
  print(color.cyan + '└━━━━━━━━༻¨:·. ✧ .·:¨༺ ━━━━━━━━┘' + color.end)
  y = float(input('(∩｀-´)⊃━ ☆ﾟ.*･｡ﾟ Enter your choice [1-5]: '))
  if y == 1:
    metreYard()
  elif y == 2:
    kilogramPound()
  elif y == 3:
    celsiusFahrenheit()
  elif y == 4:
    kilometreMile()
  elif y == 5:
    print('Exited')
  else:
    print('That is not an option, please pick a valid option next time')

menu()