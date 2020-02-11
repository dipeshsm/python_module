def open_file(file_location):
    word_count = 0
    with open(file_location, 'r') as file:
        for line in file:
            word_count = word_count + len(line.split())
        return word_count
