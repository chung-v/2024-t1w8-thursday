def convert_to_integer(value):
    try:
        result = int(value)
        print(f'Conversion Successful! Result: {result}')
    except ValueError:
        print('Conversion Failed. Please enter a valid integer.')
    finally: # Optional, but makes the code more organised and readable
        print("Closing any open resources.")

# Usesr input
user_input = input ("Enter a number to convert to integer: ")

# Conver the number
convert_to_integer(user_input)