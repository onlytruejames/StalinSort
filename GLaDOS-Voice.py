import time as t
from pygame import mixer
import pygame
import eng_to_ipa as ipa
def say(ipaChar):
    l = fr"C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\\{ipaChar}"
    mixer.init()
    if ipaChar=="e":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\e.ogg")
    elif ipaChar=="æ":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\æ.ogg")
    elif ipaChar=="ā":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\ā.ogg")
    elif ipaChar=="ē":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\ē.ogg")
    elif ipaChar=="ī":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\ī.ogg")
    elif ipaChar=="ō":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\ō.ogg")
    elif ipaChar=="ū":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\ū.ogg")
    elif ipaChar=="ɒ":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\ɒ.ogg")
    elif ipaChar=="ə":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\ə.ogg")
    elif ipaChar=="ʊ":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\ʊ.ogg")
    elif ipaChar=="ʌ":
        sound = pygame.mixer.Sound("C:\Users\marce\Downloads\gladosvoiceJamesAndShadow\sounds\ʌ.ogg")
    sound = pygame.mixer.Sound(l)
    
while True:
    try:
        x = ipa.convert(input("Input word to be GLaDified\n"))
    except:
        print("Something went wrong")
        x = False
    if x:
        for word in x:
            word=word.replace("ɪə","ë").replace("eə","ä").replace("eɪ","å").replace("ɔɪ","ø").replace("aɪ","ï").replace("əʊ","ö").replace("aʊ","ü").replace("ɜ:","ē").replace("ɑ:","ā").replace("i:","ī").replace("ɔ:","ō").replace("u:","ū")
            for letter in list(word):
                if not letter=="'":
                    say(letter)
            t.sleep(0.3)
