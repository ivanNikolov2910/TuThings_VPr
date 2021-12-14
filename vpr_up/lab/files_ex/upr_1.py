import constants.pr_constants as pr_const

RESOURCES_PATH = pr_const.RESOURCES_PATH

# read and print with for - txt
file_name = 'text.txt'
file = open(str(RESOURCES_PATH + file_name), 'r')
for i in file:
    print(i, end='')

# create bin file "document.bin", open and write "this is good" to ascii and close

file_bin = open(str(RESOURCES_PATH + 'document.bin'), 'wb')
file_bin.write("this is good".encode("ascii"))
file_bin.close()

file_bin = open(str(RESOURCES_PATH + 'document.bin'), 'rb')
print("\n\n")
print(file_bin.read())
file_bin.close()
