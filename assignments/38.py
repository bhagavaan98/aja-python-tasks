'''Show the below menu to the user until and until user select quit and display corresponding os message 
Menu: 
1. windows 
2. Linux 
3. Mac 
4. quit 
''' 

while True:
    Options = int(input("Select anyone option\n1.Windows\n2.Linux\n3.Mac\n4.Quit\n"))

    if Options == 1:
        print("menu\n1.Windows\n2.Linux\n3.Mac\n4.Quit\n")
    elif Options == 2:
        print("menu\n1.Windows\n2.Linux\n3.Mac\n4.Quit\n")
    elif Options == 3:
        print("menu\n1.Windows\n2.Linux\n3.Mac\n4.Quit\n")
    elif Options == 4:
        print("Quit")
        break
    else:
        print("Select anything from given Option")
        