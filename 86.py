'''case insensitive search for an element.'''
hello = list(input("Enter the string : ").lower())
crazy = input("Enter the element here : ").lower()
for i in hello:
    if i == crazy:
        print(f"The element is found {i}")
        break 
else:
    print("The element is not found in the list")