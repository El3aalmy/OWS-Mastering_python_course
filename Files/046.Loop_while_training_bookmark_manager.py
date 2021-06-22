# -------------------------------------
# ------ Loop => While training -------
# ------ Simple bookmark manage -------
# -------------------------------------

# Empty list to fill later 
MyWeb = []

# Maximum allowed websites 
MaximumWeb = 5

while MaximumWeb > 0 :

    # Input the new website     
    web = input("Website name without https:// ")

    # Add the new website to the list 
    MyWeb.append(f"https://{web.strip().lower()}")

    # Decrease one number from allowed websites 
    MaximumWeb -= 1     # MaximumWeb = MaximumWeb - 1

    # Print the add message 
    print(f"Website added, {MaximumWeb} places left")

    # Print the list 
    print(MyWeb)
    
else :

    print("Bookmark is full, you cannot add more")

# Check if the list is not empty 

if len(MyWeb) > 0 :

    # Sort the list 
    MyWeb.sort()

    index = 0

    print("Printing the list of websites")

    while index < len(MyWeb) :

        print(MyWeb[index])

        index += 1      # index = index + 1
