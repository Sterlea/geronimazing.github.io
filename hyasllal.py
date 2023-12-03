# geronimazing.github.io
print("How hard will a hilichurl hit you?")

de=int(input("How much DEF (in total) do you have? "))
print("You have ",de," DEF in total.")
hilile = int(input('What is the level of the hilichurl? '))
if hilile <= 90:
    print("The hilichurl is level ", hilile)
elif hilile > 90:
    print("Your hilichurl level is too high... but...")
dmg= ((hilile*13.584)-(de//(de+5*hilile+500)))
print("A hilichurl will cause you to take approx. ",dmg," damage.")
