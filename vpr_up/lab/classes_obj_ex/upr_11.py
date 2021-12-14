# method(name) -> чете файл и връща srt

def get_data(fail_name: str):

    file_path = "D:\\Programs\\PyCharm Community Edition 2021.2.2\\Projects\\TuThings\\resources\\" + fail_name
    return open(file_path).read()

try:
    string = 'upr_11.tt'  # input("Enter file name:")
    print(get_data(string))
except(FileNotFoundError):
    print("incorrect file name")
else:
    print('END!!')
