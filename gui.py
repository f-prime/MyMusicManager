import pygame
import getNames
import getSong
import sys

def main():
    screen = pygame.display.set_mode((600, 100))
    pygame.display.set_caption("Music Manager")
    playing = False
    play = pygame.Rect(400, 40, 25,25)
    skip = pygame.Rect(450, 40, 25, 25)
    prev = pygame.Rect(350, 40, 25,25)
    pygame.font.init()
    font = pygame.font.Font("BlissfulThinking.otf", 25)
    songs = getNames.getNames()
    song = None
    on = 0
    pygame.mixer.init()

    while True:
        screen.fill((255,255,255))
        if playing:
            pygame.draw.rect(screen, (255, 0, 0), play)
        else:
            pygame.draw.rect(screen, (0, 0, 255), play)
        
        pygame.draw.rect(screen, (0, 255, 0), skip)
        pygame.draw.rect(screen, (0, 255, 0), prev)

        if song:
            screen.blit(font.render(song, -1, (0,0,0)), (10, 40))


        if playing:
            if not song:
                song = songs[on]
                
                pygame.mixer.music.load(getSong.getSong(song))
                pygame.mixer.music.play(-1, 0.0)
                
            elif not pygame.mixer.music.get_busy():
                song = None
                if on < len(songs):
                    on += 1
                else:
                    on = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if play.collidepoint(mouse):
                    if not playing:
                        pygame.mixer.music.unpause()
                        playing = True
                    else:
                        pygame.mixer.music.pause()
                        playing = False

                elif skip.collidepoint(mouse):
                    if on < len(songs) - 1:
                        on += 1
                    else:
                        on = 0
                    song = None

                elif prev.collidepoint(mouse):
                    if on > 0:
                        on -= 1
                    else:
                        on = len(songs) - 1
                    song = None

        pygame.display.update()


if __name__ == "__main__":
    main()
