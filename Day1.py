file_path = 'Day1Input.txt'  # Replace 'your_file.txt' with the actual file path

with open(file_path, 'r') as file:
    sum = 0
    # Iterate over each line in the file
    for line in file:

        # Process the line (in this example, print it)
        string_digits = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
        possible_num = []   

        for str, dig in string_digits.items():
            line = line.replace(str, dig)

        for let in line:
            if let.isdigit():
                firstNum = let
                break

        for let in reversed(line):
            if let.isdigit():
                secondNum = let
                break
        
        sum += int(firstNum + secondNum)


    print(sum)
