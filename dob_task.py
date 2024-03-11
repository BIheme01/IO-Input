"""
Start

MY APPROACH

# Create container for name
# Create container for DOB
# Open and read DOB text file
# Add names to name container
# Add birthdate to DOB container
# Print names and birthdates as 2 separate lists

End

"""
name = []
dob = []

file = open("io-input/dob.txt", "r+")
print('\33[1m'"Name"'\33[0m')
for line in file:
    words = line.split()             # Split words in each line
    first_two_words = words[:2]      # Take first 2 words(names)
    #Turn list of names to string 
    first_two_words = (" ").join(first_two_words)    
    print(first_two_words)           # Print names
    name.extend(first_two_words)     # Add names to container

print("")
# Reset the read position to the beginning of the file
file.seek(0)
print('\33[1m'"Birthdate"'\33[0m')
for line in file:
    words = line.split()                # Split words in each line
    birth_date = words[2:5]             # Take last 3 characters
    birth_date = (" ").join(birth_date)          
    print(birth_date)                   # Print DOB
    dob.extend(birth_date)              # Add DOB to container
                
file.close()

                

