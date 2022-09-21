    with open("C:/Parsing/artifact.txt", "r") as file:
        for line in file:
            if line in get:
                with open(title_element + '.txt', 'a') as f:
                    f.write(line + '\n')
