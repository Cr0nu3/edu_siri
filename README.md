# [ Manual ]
1. [English](https://github.com/Cr0nu3/edu_siri/tree/main#Introduction-of-EDU_SIRI)
2. [Korean](https://github.com/Cr0nu3/edu_siri/tree/main#EDU_SIRI-소개)

## Introduction of EDU_SIRI
This program automatically summarizes and organizes video lectures. It is designed for lecture videos in English and is available for Windows operating systems. The program has the following features

1. Transcribe Instructor's voice into text.
2. Transcribe course materials into text.
3. Summarize lecture's content.

* Note : You can ignore "warning" message if program doesn't shut down.

## Before you use
1. Before running this code, you must download "https://alphacephei.com/vosk/models/vosk-recasepunc-en-0.22.zip", unzip it, and  put the directory in the same path as this README.md file. (After unzipping the file, rename it as "**recasepunc**")

## Manual in each options
* Video-Text Convert & Summary Mode (All) 
    1. Put videos you want to transcribe in "/video" directory.
    2. Set the directory name, the program will automatically create the directory and save the result file.
    3. The result of transcribing video speech is saved in 'speech_result.txt'
    4. The result of transcribing course material is saved in './course_material/ppt_content.txt'

* Video-Text Convert Mode (Except for Summary Mode)
    1. The desired video must be placed in the "/video" directory
    2. Set the directory name, the program will automatically create the directory and save the result file
    3. The result of transcribing video speech is saved in 'speech_result.txt'
    4. The result of transcribing course material is saved in './course_material/ppt_content.txt'

* Summary Mode
    * Note: You must enter the absolute path of the desired file.
    ex) C:\Users\GUEST\Desktop\edu_helper\speech_result.txt 

*****

## EDU_SIRI 소개
이 프로그램은 동영상 강의를 자동으로 요약, 정리해주는 프로그램입니다. 영어로 된 강의 동영상을 대상으로 만들었으며, 윈도우 운영체제에서 사용 가능합니다. 프로그램의 기능은 다음과 같습니다.

1. 강의자의 음성을 텍스트로 변환해주는 기능 
2. 강의 자료를 텍스트로 변환해주는 기능 
3. 수업 내용을 요약해주는 기능

* 주의 : 프로그램이 종료되지 않는 한, 'warning'이라 표시되는 메세지들은 무시해도 괜찮습니다.

## 사용 전 세팅 안내
1. 프로그램을 돌리기 전, https://alphacephei.com/vosk/models/vosk-recasepunc-en-0.22.zip 다운 필수 & README.md 파일과 같은 경로의 디렉토리 안에 넣어놔야 합니다. (다운받은 파일을 압축해제한 후, 디렉토리명은 recasepunc로 변경해주세요.)

## 옵션별 사용법
* Video-Text Convert & Summary Mode (All) 
    1. 변환하고자 하는 비디오를 "/video" 디렉토리에 넣어놔야 합니다
    2. 디렉토리 이름을 설정하면, 프로그램이 자동으로 디렉토리 생성 및 결과 파일을 저장합니다
    3. 비디오 음성을 텍스트로 변환한 결과는 'speech_result.txt'에 저장됩니다
    4. 강의 자료를 텍스트로 변환한 결과는 './course_material/ppt_content.txt'에 저장합니다

    ★ 주의 : 원하는 파일의 절대 경로를 넣어줘야 합니다.
    ex) C:\Users\홍길동\Desktop\edu_helper\speech_result.txt

* Video-Text Convert Mode (Except for Summary Mode)
    1. 원하는 비디오를 "/video" 디렉토리에 넣어놔야 합니다
    2. 디렉토리 이름을 설정하면, 프로그램이 자동으로 디렉토리 생성 및 결과 파일을 저장합니다
    3. 비디오 음성을 텍스트로 변환한 결과는 'speech_result.txt'에 저장됩니다
    4. 강의 자료를 텍스트로 변환한 결과는 './course_material/ppt_content.txt'에 저장합니다

* Summary Mode
    ★ 주의 : 원하는 파일의 절대 경로를 넣어줘야 합니다.
    ex) C:\Users\홍길동\Desktop\edu_helper\speech_result.txt