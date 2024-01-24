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


with open ("DOB.txt", "r+") as f:
        print('\33[1m'"Name"'\33[0m')
        for line in f:
                words = line.split()             # Split words in each line
                first_two_words = words[:2]      # Take first 2 words(names)
                print(first_two_words)           # Print names
                name.extend(first_two_words)     # Add names to container

        print("")

with open ("DOB.txt", "r+") as f:
        print('\33[1m'"Birthdate"'\33[0m')
        for line in f:
                words = line.split()             # Split words in each line
                birthdate = words[2:5]           # Take last 3 characters 
                print(birthdate)                 # Print DOB
                dob.extend(birthdate)            # Add DOB to container
                
            


                

