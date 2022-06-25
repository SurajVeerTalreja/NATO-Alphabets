import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_phonetic_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dictonary = {row.letter: row.code for (index, row) in nato_phonetic_alphabet_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
correct_word = False
while not correct_word:
    word = input("Enter a word  ").upper()
    try:
        list_of_phonetic_codes = [nato_phonetic_alphabet_dictonary[letter] for letter in word]
    except KeyError:
        print("Sorry only Alphabets are accepted.")
    else:
        print(list_of_phonetic_codes)
        correct_word = True
