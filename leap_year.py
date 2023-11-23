year = int(input("Enter year: "))
if year <= 0 :
  print("Invalid year.")
else :
  if year % 4 == 0 or year % 400 == 0 :
    if year % 100 == 0 and year % 400 != 0 :
      print("%d is not a leap year." % year)
    else :
      print("%d is a leap year." % year)
  else :
    print("%d is not a leap year." % year)