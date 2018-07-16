
check_error = 1


def check_valid_input(square_side_length):
    """
    Check the input number and valid it to be only positive odd number.

    :param  int square_side_length: The magic square side length (input number from the user).
    :return: The method will return (0) if the input is valid and will return (1) if the input is invalid.
    :rtype: int.
    """
    if square_side_length.isnumeric() and not (int(square_side_length) % 2 == 0 or int(square_side_length) <= 0):
        return 0
    else:
        return 1


def magic_total_constant(square_side_length):
    """
    Return the magic square total constant number which is the summation of: a single (row or col or diagonal).

    :param  int square_side_length: The magic square side length (input number from the user).
    :return: The magic square constant number.
    :rtype: int.
    """
    return square_side_length * (square_side_length**2 + 1) / 2


def print_magic_square(square_side_length, magic_square_arr):
    """
    Print a legibly magic square.

    :param int square_side_length: The magic square side length (input number from the user).
    :param array(int) magic_square_arr: The magic square array with the number.
    :return: There is no return value.
    :rtype: There is no return type.
    """
    for row in magic_square_arr:
        for element in row:
            # Note: the equation below is used to calculate the spaces after each printed number
            # the spaces fit inversely with the length of each number(number of digits)
            # so there will not be any wrap.
            print("| ", str(element), end=(2 * (len(str(square_side_length ** 2))) - len(str(element))) * " ")
        print(' |', '\n')


def build_magic_square(square_side_length, magic_square_arr):
    """
    Build the magic square array with the numbers and store it inside an array.

    :param int square_side_length: The magic square side length (input number from the user).
    :param array(int) magic_square_arr: The magic square array with the number.
    :return: There is no return value.
    :rtype: There is no return type.
    """
    current_col = square_side_length - 1
    current_row = square_side_length // 2
    current_number = 1

    while current_number <= square_side_length ** 2:
        magic_square_arr[current_row][current_col] = current_number
        current_number = current_number + 1
        new_row = (current_row - 1) % square_side_length
        new_col = (current_col + 1) % square_side_length

        if magic_square_arr[new_row][new_col]:
            current_col = current_col - 1
        else:
            current_col = new_col
            current_row = new_row


def verify_magic_square(square_side_length, magic_square_arr):
    """
    Verify that the magic square is indeed valid.

    :param int square_side_length: The magic square side length (input number from the user).
    :param array(int) magic_square_arr: The magic square array with the number.
    :return: The method will return (1) if the magic square is valid and (0) if the magic square is not valid.
    :rtype: int.
    """
    diagonal_sum = 0
    reverse_diagonal_sum = 0

    for diagonal_position in range(square_side_length):
        col_sum = 0
        row_sum = 0

        for row_and_col_iterator in range(square_side_length):
            row_sum = row_sum + magic_square_arr[diagonal_position][row_and_col_iterator]
            col_sum = col_sum + magic_square_arr[row_and_col_iterator][diagonal_position]
            if (row_and_col_iterator + diagonal_position) == (square_side_length - 1):
                reverse_diagonal_sum = reverse_diagonal_sum + magic_square_arr[diagonal_position][row_and_col_iterator]

        if row_sum != magic_square_constant or col_sum != magic_square_constant:
            print("The magic square is not valid.")
            return 0

        diagonal_sum = diagonal_sum + magic_square_arr[diagonal_position][diagonal_position]

    if diagonal_sum != magic_square_constant or reverse_diagonal_sum != magic_square_constant:
        print("The magic square is not valid.")
        return 0
    else:
        return 1


while check_error:
    # input from user: should be only +ve odd number.
    input_number = input("Please enter the number (No chars)(odd and positive only):\n")
    check_error = check_valid_input(input_number)
    if not check_error:
        input_number = int(input_number)


magic_square = [[0 for row in range(input_number)] for col in range(input_number)]

magic_square_constant = magic_total_constant(input_number)

build_magic_square(input_number, magic_square)

print_magic_square(input_number, magic_square)

valid_magic_square = verify_magic_square(input_number, magic_square)

if valid_magic_square:
    print("correct")

