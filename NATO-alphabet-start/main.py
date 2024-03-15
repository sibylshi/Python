# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}



import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

#is_continue = True

# while is_continue:
#     user_input = input("What is your name?").upper()
#     try:
#         list = [nato_dict[letter] for letter in user_input]
#     except KeyError:
#         print("You should enter a word made of letters")
#
#     else:
#         print(list)
#         is_continue = False


def generate_letter():
    user_input = input("What is your name?").upper()
    try:
        list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("You should enter a word made of letters")
        generate_letter()

    else:
        print(list)

generate_letter()




# for letter in user_input.upper():
#     for letter in user_input.upper():
#         obj = [value for (name, value) in nato_dict.items() if letter == name ]
#     list.append(obj)




# for (name,value) in nato_dict.items():
#     list = [value for letter in user_input.upper() if letter == name]

    # for letter in user_input.upper():
    #     if letter == name:
    #         print(value)
