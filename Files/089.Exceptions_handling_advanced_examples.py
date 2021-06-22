# -----------------------------------
# --     Exceptions handling       --
# -- Try | Except | Else | Finally --
# --      Advanced examples        --
# -----------------------------------

the_file = None 
number_of_tries = 5

while number_of_tries > 0 :

    try :

        print("Enter the file name with absolute path")

        print(f"You have {number_of_tries} tries left")

        print(r"Example: C:\Users\hasan\Google Drive\1.Projects\Mastering_python_course\Files\file_name")

        file_name_with_path = input("File name => ").strip()

        the_file = open(file_name_with_path, "r")

        print(the_file.read())

        break

    except FileNotFoundError :

        print("File not found, make sure the file name is valid")

        number_of_tries -= 1 

    except :

        print("Error happens")
    
    finally :

        if the_file is not None :

            the_file.close()

            print("File closed.")

else :

    print("All tries is done")
