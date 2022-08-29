

prior_output = None
user_variables = {}


def get_firstword(user_input):
    """ Takes user input as a string and returns the first word."""

    r = 0
    
    while r < len(user_input) and user_input[r] != " ":
        r += 1
    
    return user_input[0:r]

def write_to_screen(user_input):
    """ Takes a string of user input. Prints the requested string on the console. """

    r = 6
    string_to_print = None
    if r > len(user_input):
        print('\nYou have made a syntax error.\n')
    elif user_input[r] != '"':
        l = r
        while r < len(user_input) and user_input[r] != ' ':
            r += 1
        variable_input = user_input[l:r]
        if variable_input == "that":
            string_to_print = prior_output
        elif variable_input not in user_variables:
            print('\nYou have made a syntax error.\n')
        else:
            string_to_print = user_variables[variable_input]
    else:
        r += 1
        l = r
        while r < len(user_input) and user_input[r] != '"':
            r += 1
        string_to_print = user_input[l:r]
    
    if string_to_print:
        print(f"\n{string_to_print}\n")
        return string_to_print

def add_two_numbers(user_input):
    """ Adds two values according to a user input string. """

    l = 4
    r = 5

    while r < len(user_input) and user_input[r] != " ":
        r += 1
    
    if user_input[l:r] in user_variables:
        first_number = float(user_variables[user_input[l:r]])
    elif user_input[l:r] == "that":
        first_number = float(prior_output)
    else:
        first_number = float(user_input[l:r])

    if user_input[(r):(r + 5)] != " and ":
        print('\nYou have made a syntax error.\n')
    else:
        l = r + 5
        r = l + 1
        while r < len(user_input) and user_input[r] != ".":
            r += 1
        
        if user_input[l:r] in user_variables:
            second_number = float(user_variables[user_input[l:r]])
        elif user_input[l:r] == "that":
            second_number = float(prior_output)        
        else:
            second_number = float(user_input[l:r])

        sum = first_number + second_number
        print(f"\n{sum}\n")
        return sum

def multiply_two_numbers(user_input):
    """ Multiplies two values according to a user input string. """

    l = 9
    r = 10

    while r < len(user_input) and user_input[r] != " ":
        r += 1
    
    if user_input[l:r] in user_variables:
        first_number = float(user_variables[user_input[l:r]])
    elif user_input[l:r] == "that":
            first_number = float(prior_output)
    else:
        first_number = float(user_input[l:r])

    if user_input[(r):(r + 4)] != " by ":
        print('\nYou have made a syntax error.\n')
    else:
        l = r + 4
        r = l + 1
        while r < len(user_input) and user_input[r] != ".":
            r += 1
        
        if user_input[l:r] in user_variables:
            second_number = float(user_variables[user_input[l:r]])
        elif user_input[l:r] == "that":
            second_number = float(prior_output)
        else:
            second_number = float(user_input[l:r])

        product = first_number * second_number
        print(f"\n{product}\n")
        return product

def divide_two_numbers(user_input):
    """ Divides one value by another according to a user input string. """

    l = 7
    r = 8

    while r < len(user_input) and user_input[r] != " ":
        r += 1
    
    if user_input[l:r] in user_variables:
        first_number = float(user_variables[user_input[l:r]])
    elif user_input[l:r] == "that":
            first_number = float(prior_output)
    else:
        first_number = float(user_input[l:r])

    if user_input[(r):(r + 4)] != " by ":
        print('\nYou have made a syntax error.\n')
    else:
        l = r + 4
        r = l + 1
        while r < len(user_input) and user_input[r] != ".":
            r += 1
        
        if user_input[l:r] in user_variables:
            second_number = float(user_variables[user_input[l:r]])
        elif user_input[l:r] == "that":
            second_number = float(prior_output)
        else:
            second_number = float(user_input[l:r])

        quotient = first_number / second_number
        print(f"\n{quotient}\n")
        return quotient

def store_variable(user_input):
    ''' Stores a value in a variable according to a user input string. '''

    l = 6
    r = 7

    if user_input[l] == '"':
        while r < len(user_input) and user_input[r] != '"':
            r += 1
        value_to_store = user_input[l + 1 : r]
        r += 1

    else:
        while r < len(user_input) and user_input[r] != ' ':
            r += 1
        value_to_store = user_input[l:r]
    
    r += 1

    if user_input[r : r + 16] != "as the variable ":
        print('\nYou have made a syntax error.\n')
    
    else:
        l = r + 16
        r = l + 1
        while r < len(user_input) and user_input[r] != ".":
            r += 1

        variable_name = user_input[l:r]

        if value_to_store == "that":
            value_to_store = prior_output
        
        user_variables[variable_name] = value_to_store
        
        print(f"\nThe value {value_to_store} is stored as the variable {variable_name}.\n")



def main():
    global prior_output
    global user_variables

    print("\nWelcome to the Ordinary Languge interpreter!\n")
    exit_interpreter = False
    while exit_interpreter == False:
        user_input = input("> ")
        firstword = get_firstword(user_input)

        if firstword == "Write":
            prior_output = write_to_screen(user_input)

        elif firstword == "Add":
            prior_output = add_two_numbers(user_input)

        elif firstword == "Store":
            store_variable(user_input)

        elif firstword == "Multiply":
            prior_output = multiply_two_numbers(user_input)

        elif firstword == "Divide":
            prior_output = divide_two_numbers(user_input)
        
        elif firstword.upper() == "EXIT" or firstword.upper() == "QUIT":
            exit_interpreter = True
        
        else:
            print(f'"{user_input}" is incorrect phrasing. Please try again. Type "Exit" to exit.')

if __name__ == "__main__":
    main()