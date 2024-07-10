def main():
    number_list = load_numbers_from_file("numbers.txt")
    val = 0
    for i in range (len(number_list)):
        val += number_list[i]

    Final = val / len(number_list)

    print("Average: ", Final)    
    


def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers


if __name__ == '__main__':
    main()
