import pygame
import getNames
import getSong
import sys
import random

def main():
    screen = pygame.display.set_mode((600, 100))
    pygame.display.set_caption("Music Manager")
    playing = True
    play = pygame.Rect(400, 40, 25,25)
    skip = pygame.Rect(450, 40, 25, 25)
    prev = pygame.Rect(350, 40, 25,25)
    pygame.font.init()
    font = pygame.font.Font("BlissfulThinking.otf", 25)
    songs = getNames.getNames()
    random.shuffle(songs)
    on = 0
    pygame.mixer.init()
    clock = pygame.time.Clock()
    getSong.getSong(songs[on])
    sound = pygame.mixer.Sound("tmp") 
    channel = sound.play()
    get_next = True 
    
    playImg = pygame.image.load("play.png").convert()
    pauseImg = pygame.image.load("pause.png").convert()
    skipImg = pygame.image.load("skip.png").convert()
    prevImg = pygame.image.load("prev.png").convert()

    while True:
        clock.tick(60)
        screen.fill((255,255,255))
        if playing:
            screen.blit(pauseImg, (play.x, play.y))
        else:
            screen.blit(playImg, (play.x, play.y))
        screen.blit(skipImg, (skip.x, skip.y))
        screen.blit(prevImg, (prev.x, prev.y))
        
        screen.blit(font.render(str(songs[on]), -1, (0,0,0)), (10, 40))


        if playing:
            if not channel.get_busy():
                if not pygame.mixer.music.get_busy():
                    if on < len(songs):
                        on += 1
                    else:
                        on = 0
                    get_next = True
                    sound = pygame.mixer.Sound("tmp")
                    channel = sound.play()
        

        if get_next:
            if on < len(songs) - 1:
                o = on + 1
            else:
                o = 0
            getSong.getSong(songs[o])
            get_next = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if play.collidepoint(mouse):
                    if not playing:
                        channel.unpause()
                        playing = True
                    else:
                        channel.pause()
                        playing = False

                elif skip.collidepoint(mouse) and not get_next:
                    channel.pause()
                    if on < len(songs) - 1:
                        on += 1
                    else:
                        on = 0
                    getSong.getSong(songs[on])
                    sound = pygame.mixer.Sound("tmp")
                    channel = sound.play()

                elif prev.collidepoint(mouse):
                    channel.pause()
                    if on > 0:
                        on -= 1
                    else:
                        on = len(songs) - 1
                    getSong.getSong(songs[on])
                    sound = pygame.mixer.Sound("tmp")
                    channel = sound.play()

        pygame.display.update()


if __name__ == "__main__":
    main()
