
# 1.Read a file
with open("input.txt", "r") as f1:
    data = f1.read()

with open("output.txt", "w") as f2:
    f2.write(data.upper())

print("File copied in uppercase successfully")



# 2.File handling
src = input("Enter source file: ")
dest = input("Enter destination file: ")

with open(src, "r") as f1, open(dest, "w") as f2:
    for line in f1:
        if not line.strip().startswith("#"):
            f2.write(line)

print("\n--- Source File Content ---")
with open(src, "r") as f:
    print(f.read())

print("\n--- Destination File Content ---")
with open(dest, "r") as f:
    print(f.read())