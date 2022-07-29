import winsound
import sys
print("\t\t\t Sound 0.3")
quit = True
while True:
    try:
        Frequency = 0
        Timer = 0
        print(f"Choose Frequrency: ")
        Frequency = int(input())
        print(f"Choose time: 's'")
        Timer = str(input())
        Timer1 = Timer + "000"
        Timert = int(Timer1)
        winsound.Beep(Frequency, Timert)

    except ValueError:
        print("You entered a non-correct, or too small/large number")
    except KeyboardInterrupt:
        break
    quit = input("Exit?: 'y - yes, n - no' ")
    if quit == "y":
        sys.exit("Bye!")
    else:
        continue


