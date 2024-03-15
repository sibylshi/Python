import pandas
# student_dict = {
#     "Angela":56,
#     "James": 78,
#     "Lily":90,
# }
student_dict = {
    "student":["Angela","Alex","Lily"],
    "score":[56,78,90],
}

# student_data_frame = pandas.DataFrame(student_dict,index=[0])
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop in a dict
# for (key,value) in dict.items():
#     print((key,value))

# loop by column
for (key,value) in student_data_frame.items():
    print((key,value))

# loop by row
for (index,row) in student_data_frame.iterrows():
    print(row)
