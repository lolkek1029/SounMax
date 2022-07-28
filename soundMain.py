import winsound
from time import sleep
program = "Sound 0.2"
print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t {program}")
print("""
Hey!
This program create sound
I`m learn python,and this program test!)
""")
sleep(3)
Frequency = 0
Timer = 0
chooseSound = input("Choose Frequency: 'Small, Medium, High': ")
time = [1000, 3000, 5000, 8000, 10000]
if chooseSound == "Small":
    Frequency = 1000
    Timer = 2500
    winsound.Beep(Frequency, Timer)
elif chooseSound == "Medium":
    Frequency = 2500
    Timer = 2500
    winsound.Beep(Frequency, Timer)
else:
    Frequency = 5000
    Timer = 2500
    winsound.Beep(Frequency,Timer)