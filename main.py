import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in file.iterrows()}

user_input = input("Type a word to get the NATO alphabet: ")
out_list = []
for letter in user_input:
    out_list.append(nato_dict[letter.upper()])
print(out_list)
