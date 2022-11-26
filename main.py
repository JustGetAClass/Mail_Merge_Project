with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # we can use name_file.splitlines() so that we don't have to strip the spaces(/n)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        new_name = name.strip()
        new_letter = letter_content.replace("[name]", new_name)
        with open(f"./Output/ReadyToSend/letter_to_{new_name}.txt", mode="w") as final_letters:
            final_letters.write(new_letter)
