import numpy as np


def request_key(n: int) -> list[list[float]]:
    key = [[0.0 for aux in range(n)] for aux in range(n)]
    for row in range(n):
        for column in range(n):
            key[row][column] = float(input(f"key{row+1},{column+1} = "))
    return key


def calculate_invertible(matrix: list) -> list[list[float]]: 
    inverse_matrix = np.linalg.inv(matrix)
    inverse_matrix = inverse_matrix.tolist()
    return inverse_matrix


def convert_message_to_dec(message: str) -> list[int]: 
    converted_message = []
    for char in message:
        num = ord(char)
        converted_message.append(num)
    return converted_message


def message_setup(message: list[int], n: int) -> list[list[int]]:
    sublists = []
    sublist = []
    for i in message:
        if len(sublist) >= n:
            sublists.append(sublist)
            sublist = []
        sublist.append(i)
    sublists.append(sublist)
    return sublists


def multiply_matrices(invertible: list[list[float]], message: list[list[int]]) -> list[list[int]]:
    result = []
    for m in message:
        for row in range(len(invertible)):
            sum = 0
            for column in range(len(invertible[row])):
                a = invertible[row][column] * m[column]
                sum += a
            result.append(int(sum))
    return result


def convert_dec(message) -> str:
    message = [chr(num) for num in message]
    return "".join(message)


def main():    # pragma: no cover
    n = int(input("Please, type the order of the matrix (key): "))

    encoder_key = request_key(n)
    decoder_key = calculate_invertible(encoder_key)
    
    message = input("Type encrypted message: ")
    
    converted_to_dec_message = convert_message_to_dec(message)
    converted_to_dec_message = message_setup(converted_to_dec_message, n)
    decrypted_message_in_dec = multiply_matrices(decoder_key, converted_to_dec_message)
    decrypted_message_in_str = convert_dec(decrypted_message_in_dec)
    print("The message is: ", decrypted_message_in_str)


if __name__ == "__main__":    # pragma: no cover
    main()
