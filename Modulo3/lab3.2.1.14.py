blocks = int(input("Enter the number of blocks: "))

height = 0

while ((height < blocks) and (blocks > 1)):
    blocks = blocks - height
    height = height + 1

print("The height of the pyramid:", height)