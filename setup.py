import os


def changeYml(token):


    a_file = open("config.yml", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[0] = f"token: \"{token}\"\n"

    a_file = open("config.yml", "w")
    a_file.writelines(list_of_lines)
    a_file.close()

def initBot():

    os.system("pip install -r requirements.txt")
    os.system("python lichess-bot.py -u")



def main():
    token = input("Token :   ")
    changeYml(token)
    initBot()


main()



