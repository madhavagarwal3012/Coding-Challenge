def process_list(input_list):
    if len(input_list) % 10 != 0:
        raise ValueError("Error: Input list length must be a multiple of 10.")

    processed_list = [input_list[i] for i in range(len(input_list)) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]

    return processed_list

try:
    input_list = [int(x) for x in input("Enter a list of integers separated by space: ").split()]
    processed_result = process_list(input_list)
    print("Processed List:", processed_result)
except ValueError as e:
    print(e)
