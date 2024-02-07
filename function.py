import moviepy.editor as mp 
import os
import cv2 as cv
from skimage.metrics import structural_similarity as compare_ss
from pytesseract import image_to_string 
import configparser
from PIL import Image
import numpy as np
import  time
import nltk
from nltk.corpus import stopwords
import re
from nltk.tokenize import sent_tokenize
from collections import Counter
import pandas as pd
import heapq
from description import error
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
import json
import subprocess

#######################  Video 음성 Text로 변환 기능 Part   ##################################
# Video_to_text 파일 완료
def video_to_text(video_name):
    # Set path of video and speech file
    base_path = os.getcwd()
    video_path = base_path + "\\video\\" + str(video_name)
    speech_file = str(video_name).split('.')[0]
    speech_file = speech_file + ".wav"
    speech_path = base_path + "\\speech\\" + str(speech_file)

    # Convert Video to sound file
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(speech_path)

    FRAME_RATE = 16000
    CHANNELS = 1

    try:
        model = Model(model_name='vosk-model-small-en-us-0.15')
        rec = KaldiRecognizer(model, FRAME_RATE)
        rec.SetWords(True)
        print("\n\n#############    Now, I'm on my work.. It takes a few minutes.  #####################")
        print("##################      It's okay to ignore warnings!      ##########################")
        print("####  If the program is still stuck after enough time has passed, press Enter.  #####")
        speech = AudioSegment.from_mp3(speech_path)
        speech = speech.set_channels(CHANNELS)
        speech = speech.set_frame_rate(FRAME_RATE)

        rec.AcceptWaveform(speech.raw_data)
        result = rec.Result()
        text = json.loads(result)['text']
        cased = subprocess.check_output('python recasepunc/recasepunc.py predict recasepunc/checkpoint', shell=True, text=True, input=text)
        cased = cased.replace(" ' ", "'").replace(" ? ", "? ").replace(" ! ", "! ")
        with open('speech_result.txt',mode ='a') as file: 
            file.write("\n==============================================\n")
            file.write("Content: \n") 
            file.write(str(cased)) 
            print("+===========================================+")
            print("| Converting is done! (Video Sound -> Text) |")
            print("+===========================================+")
    
    except Exception as e:
        error("Error occurred during converting video sound to text! The file is probably an unsupported format")

#######################    PPT 내용 텍스트로 변환하는 기능 Part    ####################################

def comparePic(path, image1, image2) -> str:
    image1_path = path + "/" + image1
    image2_path = path + "/" + image2

    pre = cv.imread(image1_path)
    post = cv.imread(image2_path)
    result = pre.copy()

    grayPre = cv.cvtColor(pre, cv.COLOR_BGR2GRAY)
    grayPost = cv.cvtColor(post, cv.COLOR_BGR2GRAY)

    (Similarity, diff) = compare_ss(grayPre, grayPost, full=True)
    diff = (diff * 255).astype('uint8')

    if(Similarity < 0.95):
        PicToText(post)

# 글자 인식을 위한 함수 1
def ocrToStr(fullPath, lang='eng'):
    img = Image.fromarray(fullPath)
    #추출(이미지파일, 추출언어, 옵션)
    #preserve_interword_spaces : 단어 간격 옵션을 조절하면서 추출 정확도를 확인한다.
    #psm(페이지 세그먼트 모드 : 이미지 영역안에서 텍스트 추출 범위 모드)
    #psm 모드 : https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage
    outText = image_to_string(img, lang=lang, config='--psm 1 -c preserve_interword_spaces=1')
    strToText(outText)

def strToText(outText):
    with open('./course_material/ppt_content.txt', 'a', encoding='utf-8') as f:
        f.write(outText)
        f.write("==========================================================\n")

# 글자 인식하는 main 함수
def PicToText(path)->str:
    # Config Parser 초기화 & Config File 읽기
    config = configparser.ConfigParser()
    config.read(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'env' + os.sep + 'property.ini')

    ocrToStr(path, 'eng')

def file_listing(path)->str:
    files = os.listdir(path)

    for i in range(1, len(files)):
        comparePic(path, files[i-1], files[i])
    print("\n+=====================================+")
    print("| Organizing class materials is Done! |")
    print("+=====================================+")

##################        글 요약 기능 Part         ###################
# refer : https://blog.devgenius.io/extractive-text-summarizing-with-python-9834dad6a020
def generate_summary(path, output_filename, mode):
    nltk.download('punkt')
    nltk.download("stopwords", quiet=True)

    file = open(path, "r", encoding='UTF-8')
    core_text = file.read().split('===========================================================================')[-1]

    # Removing Square Brackets and Extra Spaces
    core_text = re.sub(r'\[[0-9]*\]', ' ', core_text)
    core_text = re.sub(r'\s+', ' ', core_text)

    # Removing special characters and digits
    formatted_text = re.sub('[^a-zA-Z]', ' ', core_text )
    formatted_text = re.sub(r'\s+', ' ', formatted_text)

    sentence_list = nltk.sent_tokenize(core_text)
    stopwords_english = stopwords.words("english")

    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_text):
        if word not in stopwords_english:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent):
            if(word in word_frequencies.keys() and len(sent.split(' ')) > 50):
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(8, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    path = "./summary/" + output_filename
    try:
        with open(path, mode=mode, encoding='UTF-8') as file:
            file.write('Summarized Content: \n')
            file.write(str(summary))
            file.write("\n========================================================\n")
        print("+======================+")
        print("|   Summary Complete   |")
        print("+======================+")
    except Exception as e:
        error("Error occured during summarizing text!")     
##################     모션 캡쳐 기능 (PPT의 변화 있을 시, 캡쳐)       ###################
def motion_change_detection(video_name, dir_name) -> str:
    base_path = os.getcwd()
    video_name = base_path + "\\video\\" + str(video_name)
    cap = cv.VideoCapture(video_name)

    # 옵션 설명 http://layer0.authentise.com/segment-background-using-computer-vision.html
    fgbg = cv.createBackgroundSubtractorMOG2(history=500, varThreshold=500, detectShadows=0)
    # 지정된 시간마자 찍기 위한 세팅
    start_time = int(time.time())
    # 파일 이름 세팅
    i = 0

    try:
        while(1):
            instant_time = int(time.time())
            # 동영상의 현재 프레임 수(POS_FRAMES)와 총 프레임 수(FrAME_COUNT)를 가져온다.
            # 현재 프레임 수 == 동영상 총 프레임 수 -> 종료
            if(cap.get(cv.CAP_PROP_POS_FRAMES) == cap.get(cv.CAP_PROP_FRAME_COUNT)):
                break
            ret, frame = cap.read()

            width = frame.shape[1]
            height = frame.shape[0]
            frame = cv.resize(frame, (int(width*0.8), int(height*0.8))) # 보여질 영상 크기

            fgmask = fgbg.apply(frame) # 배경 제거
            nlabels, lables, stats, centroids = cv.connectedComponentsWithStats(fgmask)

            for index, centroid in enumerate(centroids):
                if stats[index][0] == 0 and stats[index][1] == 0:
                    continue
                if np.any(np.isnan(centroid)):
                    continue

                x, y, width, height, area = stats[index]
                centerX, centerY = int(centroid[0]), int(centroid[1])

                # 영상의 움직임 범위 = area
                if(area > 400):
                    if(instant_time > start_time+2):
                        cv.imwrite("%s/%s.png" % (dir_name,  i), frame)
                        start_time = instant_time
                        i += 1
            cv.imshow('mask', fgmask)
            cv.imshow('frame', frame)

            k = cv.waitKey(30) & 0xff
            if k == 27:
                break
        #cap.release()
        print("\n+==================================+")
        print("| Detecting motion change is done! |")
        print("+==================================+")
        #cap.destoryAllWindows()

    except OSError:
        error("Failed to save file in directory that you want. Please check permission of directory or check filename")