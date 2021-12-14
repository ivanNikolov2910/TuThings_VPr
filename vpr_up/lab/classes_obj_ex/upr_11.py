# method(name) -> чете файл и връща srt
import constants.pr_constants as pr_constants

RESOURCES_PATH = pr_constants.RESOURCES_PATH


def get_data(fail_name: str):
    file_path = RESOURCES_PATH + fail_name
    return open(file_path).read()


try:
    string = 'upr_11.txt'  # input("Enter file name:")
    print(get_data(string))
except(FileNotFoundError):
    print("incorrect file name")
else:
    print('END!!')
