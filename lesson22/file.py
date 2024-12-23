import os
# r = read
# a = append
# w = write
# x = create

# Read - error if file does not exist

# print(os.getcwd())
# /home/samuelbsr/python_tutorial/lesson22/
f = open("names.txt")
# print(f.read())
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it des not exist

f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file

# avoid an error if it doesnt't exist

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)