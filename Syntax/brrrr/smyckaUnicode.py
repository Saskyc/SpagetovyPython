index = 0
string = ""
for i in range(40000):
    
    string += f"{i} {chr(i)} "
    index += 1
    if index == 10:
        string += "\n"
        index = 0
print(string)

import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Full path to file in same directory
file_path = os.path.join(script_dir, "myfile.txt")

# Now write the string
with open(file_path, "w", encoding="utf-8") as f:
    f.write(string)

print(f"Finished writing {file_path}") 
