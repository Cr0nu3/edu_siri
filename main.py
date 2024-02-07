from function import *
import re
from description import *
import shutil

reg = r'^[ㄱ-힣a-zA-Z0-9_\s]+[.][a-z]'
reg1 = r'^[ㄱ-힣a-zA-Z0-9_\-\s]+[.][a-z0-9]'
reg2 = r'^[ㄱ-힣a-zA-Z0-9_\-\s]+'

# Program Start 
start()

#while True:
print("===================================================================")
print("[!] Please Choose Options You want")
print(""" 
[+] 1. How to use? \n\
[+] 2. Video - Text Convert & Summary Mode (All) \n\
[+] 3. Video - Text Convert Mode (except summary mode)\n\
[+] 4. Summary Mode \n\
[+] 5. Exit\
    """)
mode = str(input("[>] ").strip())

if(mode == "1"):
    description() 
elif(mode == "2"):
    # Text Convert & Motion capture & Summary
    first_mode_description()

    input_file = str(input('Input video file name that you want to convert. e.g) hello.mp4 \n[>]'))
    valid = re.search(reg1, input_file)

    if not valid:
        error("Invalid input filename!")  

    input_file_path = os.getcwd()+"\\video\\" + input_file

    if(check_validity(input_file_path)):
        error("File that you choose doesn't exists. Please check if file you want exists in 'video' directory")
    
    dir = str(input('Input directory name that you want to create and save. e.g) hello \n[>]'))
    valid_dir = re.search(reg2, dir)

    if not valid:
        error("Invalid input directory name!")

    dir_path = os.getcwd() + "\\" + dir
    speech_summary = os.getcwd() + "\\speech_result.txt"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    # Video -> Text
    video_to_text(input_file) 
    # motion change detection
    motion_change_detection(input_file, dir_path)
    # get text from difference between two images
    file_listing(dir_path)
    
    generate_summary(speech_summary, "speech_summary.txt" ,'a')
    shutil.rmtree(dir_path)

    
elif(mode == "3"):
    # Text Convert & Motion Capture
    second_mode_description()
    
    input_file = str(input('Input video file name that you want to convert. e.g) hello.mp4 \n[>]'))
    valid = re.search(reg1, input_file)

    if not valid:
        error("Invalid input filename!")  
    input_file_path = os.getcwd()+"\\video\\" + input_file
    if(check_validity(input_file_path)):
        error("File that you choose doesn't exists. Please check if file you want exists in 'video' directory")
    
    dir = str(input('Input directory name that you want to create and save. e.g) hello \n[>]'))
    valid_dir = re.search(reg2, dir)

    if not valid:
        error("Invalid input directory name!")

    dir_path = os.getcwd() + "\\" + dir

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    # Video -> Text
    video_to_text(input_file) 
    # motion change detection
    motion_change_detection(input_file, dir_path)
    # get text from difference between two images
    file_listing(dir_path)
    shutil.rmtree(dir_path)

elif(mode == "4"): 
    # Summary Mode
    third_mode_description()
    input_file = str(input('Input file path that you want to summarize : \n[>]'))
    input_file = input_file.replace('\\', '\\\\')

    if(check_validity(input_file)):
        error("File that you choose doesn't exists. Please check your file path")
        #continue

    output_file = str(input('Output filename that you want. e.g) hello.txt\n[>]'))
    valid = re.search(reg, output_file)

    if not valid:
        error("Invalid output filename!")

    generate_summary(input_file, output_file, 'w')

elif(mode == "5"):
    print("\n+=====================================+")
    print("|             Good Bye!               |")
    print("+=====================================+")
    #break
else:
    print("\n+=========================================+")
    print("| !! Error !!  : You choose wrong options  |")
    print("+==========================================+\n")