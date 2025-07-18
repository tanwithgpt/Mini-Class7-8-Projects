import time
import pygame
pygame.init()
pygame.mixer.init()
et = pygame.mixer.Sound("C:/Users/MY PC/PycharmProjects/PythonProject/Healthy Programmar/eye_tracker.mp3")
dw = pygame.mixer.Sound("C:/Users/MY PC/PycharmProjects/PythonProject/Healthy Programmar/drinking_water.mp3")
per = pygame.mixer.Sound("C:/Users/MY PC/PycharmProjects/PythonProject/Healthy Programmar/per.mp3")
log = open("Logfile.txt","a+")
def dwater():
    global dw
    time.sleep(1*60*60)
    print("Drink water(437 ml)")
    if not et.get_busy() or not per.get_busy():
        dw.play()
        dw.set_volume(.10)
        hd = input("Have you drank?(Enter Y)").upper()
        if hd == "Y":
            rt = time.time()
            log.write(f"Drank water at:{rt}\n")
            pygame.mixer.stop()
def deye():
    global et
    time.sleep(30*60)
    if not dw.get_busy() or not per.get_busy():

        print("Do eyes excercise")
        et.play()
        et.set_volume(.10)
        he = input("Have you done eye exercise?(Enter Y)").upper()
        if he == "Y":
            rt = time.time()
            log.write(f"Eye exercise at:{rt}\n")
            pygame.mixer.stop()
def pex():
    global per
    time.sleep(45*60)
    if not dw.get_busy() or not et.get_busy():
        per.play()
        per.set_volume(.10)
        hpe = input("Have you done physical exercise?(Enter Y)").upper()
        if hpe == "Y":
            rt = time.time()
            log.write(f"Physical exercise at:{rt}\n")
            pygame.mixer.stop()

while True:
    pex()
    dwater()
    deye()




