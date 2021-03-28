with open("file1.txt") as file_1:
    f1_list = file_1.readlines()
    f1 = [int(num.strip("\n")) for num in f1_list]

with open("file2.txt") as file_2:
    f2_list = file_2.readlines()
    f2 = [int(num.strip("\n")) for num in f2_list]

result = list(set(f1) & set(f2))

# Write your code above 👆

print(result)


