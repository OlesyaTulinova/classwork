import os
import sys

import pygame
import requests


def idk(def_coords, def_spn):
    response = None
    map_request = "https://static-maps.yandex.ru/1.x/?ll=" + def_coords + '&spn=' + def_spn + '&l=map'
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    screen.blit(pygame.image.load(map_file), (0, 0))


cords = input()
spn = input()


pygame.init()
screen = pygame.display.set_mode((600, 450))
idk(cords, spn)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            flag = False
            if event.key == pygame.K_PAGEDOWN:
                spn = str(float(spn.split(',')[0]) - float(spn.split(',')[0]) / 10) + ',' + \
                      str(float(spn.split(',')[1]) - float(spn.split(',')[1]) / 10)
                flag = True
            elif event.key == pygame.K_PAGEUP:
                spn = str(float(spn.split(',')[0]) + float(spn.split(',')[0]) / 10) + ',' + \
                      str(float(spn.split(',')[1]) - float(spn.split(',')[1]) / 10)
                flag = True
            elif event.key == pygame.K_LEFT:
                cords = str(float(cords.split(',')[0]) - float(cords.split(',')[0]) / 10) + ',' + cords.split(',')[1]
                flag = True
            elif event.key == pygame.K_RIGHT:
                cords = str(float(cords.split(',')[0]) + float(cords.split(',')[0]) / 10) + ',' + cords.split(',')[1]
                flag = True
            elif event.key == pygame.K_DOWN:
                cords = cords.split(',')[0] + ',' + str(float(cords.split(',')[1]) + float(cords.split(',')[1]) / 10)
                flag = True
            elif event.key == pygame.K_UP:
                cords = cords.split(',')[0] + ',' + str(float(cords.split(',')[1]) - float(cords.split(',')[1]) / 10)
                flag = True
            if flag:
                idk(cords, spn)
        pygame.display.flip()
