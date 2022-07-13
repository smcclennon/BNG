# Blues Name Generator
# github.com/smcclennon

# Easily find the value of English letters to find their adjacent blues version
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Define the ridiculous blues initials
# 'Fat' = value 0 = letter a
# 'Buddy' = value 1 = letter b
# 'Sticky' = value 2 = letter c
firstBlues = ['Fat', 'Buddy', 'Sticky', 'Old', 'Texas','Hollerin''','Ugly','Brown','Happy','Boney','Curly','Pretty','Jailhouse','Peg Leg','Red','Sleepy','Bald','Skinny','Blind','Big','Yella','Toothless','Screamin''','Fat Boy','Washboard','Steel-eye']

middleBlues = ['Bones', 'Money', 'Harp','Legs','Eyes','Lemon','Killer','Hips','Lips','Fingers','Boy','Liver','Gumbo','Foot','Mama','Back','Duke','Dog','Bad Boy','Baby','Chicken','Pickles','Sugar','Willy','Tooth','Smoke']

lastBlues = ['Jackson', 'McGee', 'Hopkins','Dupree','Green','Brown','Jones','Rivers','Malone','Washington','Smith','Parker','Lee','Thompkins','King','Bradley','Hawkins','Jefferson','Davis','Franklin','White','Jenkins','Bailey','Johnson','Blue','Allison']


# Handle command line arguments
# Example:
# python bluesNameGenerator.py John Smith Doe
import sys
arguments = sys.argv[1:]  # Get the command line arguments ['arg1', 'arg2', 'arg3']
# If the command line arguments exist and are invalid
if arguments != [] and len(arguments) < 2:
    print(f'Invalid number of arguments specified ({len(arguments)} instead of 2-3)')
    quit()

if arguments == []:
    print('Please enter your real name (press enter to skip)')
    arguments.append(input('First name: '))
    arguments.append(input('Middle name: '))
    arguments.append(input('Last name: '))
    print('\nYour blues name is', end=' ')


# Convert the arguments to lowercase (for comparing to the 'alphabet' list)
arguments = [argument.lower() for argument in arguments]

# Logic to determine if a middle or last name has been provided
first = arguments[0]
if len(arguments) >= 3:
    middle = arguments[1]
    last = arguments[2]
elif len(arguments) == 2:
    middle = ''
    last = arguments[1]


try:
    # Add blues names that exist
    name = ''
    if first:
        name += f'{firstBlues[alphabet.index(first[0])]} '
    if middle:
        name += f'{middleBlues[alphabet.index(middle[0])]} '
    if last: name += lastBlues[alphabet.index(last[0])]

    # Print your blues name!
    print(name)

except ValueError as e:
    print(f'Invalid character specified. Only use English letters ({e})')