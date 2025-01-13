#Adrian



#Functions
print("Who Your Superhero Character?")
print("Answer the questions to know find out who your Superhero Character is.")
ans = input("Marvel(M) or DC(D)")
if ans == "M":
    ans = input("Woman Power(WP) or Man Power(MP)?")
    if ans == "WP":
        ans = input("Caring(C) or Sneaky(S)?")
        if ans == "C":
            print("Your Superhero Character is Scarlet Witch")
        else:
            print("Your Superhero Character is Black Widow")
    if ans == "MP":
        ans = input("Smart(S) or Strength (ST)?")
        if ans == "S":
            print("Your Superhero Character is Ironman")
        else:
            print("Your Superhero Character is Thor")
if ans == "D":
    ans = input("Woman Power(WP) or Man Power(MP)?")
    if ans == "WP":
        ans = input("Leader(L) or Fierce(F)?")
        if ans == "L":
            print("Your Superhero Character is WonderWoman")
        else:
            print("Your Superhero Character is Supergirl")
    if ans == "MP":
        ans = input("Mysetrious(M) or Hope(H)?")
        if ans == "M":
            print("Your Superhero Character is Batman")
        else:
            print("Your Superhero Character is Superman")
#Main
