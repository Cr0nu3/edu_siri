import os

def start():
    print("""
===========================================================================
███████╗██████╗░██╗░░░██╗  ██╗░░██╗███████╗██╗░░░░░██████╗░███████╗██████╗░
██╔════╝██╔══██╗██║░░░██║  ██║░░██║██╔════╝██║░░░░░██╔══██╗██╔════╝██╔══██╗
█████╗░░██║░░██║██║░░░██║  ███████║█████╗░░██║░░░░░██████╔╝█████╗░░██████╔╝
██╔══╝░░██║░░██║██║░░░██║  ██╔══██║██╔══╝░░██║░░░░░██╔═══╝░██╔══╝░░██╔══██╗
███████╗██████╔╝╚██████╔╝  ██║░░██║███████╗███████╗██║░░░░░███████╗██║░░██║
╚══════╝╚═════╝░░╚═════╝░  ╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
===========================================================================
""")

def description():
    print("\n ======================      Description of this Program      ===========================")
    print("[+] Edu_Helper is a program that extracts and summarizes the contents of a video lecture in text.")
    print("Manual :")
    print("[✓] Video - Text Convert & Summarizing Mode : The program extracts the speaker's voice and course material from the video you enter and converts it to text.")
    print("[✓] Video - Text Convert Mode : Only extracts and summarize text the content of video you input (No Summarization)")
    print("[✓] Summarizing Mode : Only summarizing aritcles you input.\n")

def first_mode_description():
    print("\nYou choose Video - Text Convert & Summarizing Mode (All).\n\
! Important ! : Before using this mode, you must check if file you want exists in '/video' directory. \n\
! Important ! : You should input directory name (Program will automatically create a directory with name you entered) \n\
! Important ! : The result content of converting speaker's voice into text is saved in 'speech_result.txt'\n\
! Important ! : The result content of course materials is saved in './course_material/ppt_content.txt'\
! Important ! : You must input absolute file path e.g) C:\\Users\\[USERNAME]\\Desktop\\test\\test.txt \n\
")

def second_mode_description():
    print("\nYou choose Video - Text Convert Mode.\n\
! Important ! : Before using this mode, you must check if file you want exists in '/video' directory. \n\
! Important ! : You should input directory name (Program will automatically create a directory with name you entered) \n\
! Important ! : The result content of converting speaker's voice into text is saved in 'speech_result.txt'\n\
! Important ! : The result content of course materials is saved in './course_material/ppt_content.txt'\n")

def third_mode_description():
    print("\nYou choose Summarizing Mode. A result file will be saved at './summary/' directory.\n\
! Important ! : You must input absolute file path e.g) C:\\Users\\[USERNAME]\\Desktop\\test\\test.txt \n\
! Important ! : Please check twice whether you give a correct path of file you want.\n")

def error(content):
    print("\n+===============================================================+")
    print("| !! Error !! : {%s} |".format(content))
    print("+================================================================+\n")

def check_validity(filename):
    if(os.path.isfile(filename) != True):
        return True
    return False
