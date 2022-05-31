from PIL import Image

import pygame
import pygame.font
import pygame.mixer

pygame.init()

DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

print(DISPLAYSURF.get_size())

size = width, height = DISPLAYSURF.get_size()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

# Objetos graficos
# img_path = "img/gnomo1.gif"
# img_path = "img/bola.gif"
img_path = "img/gifs-de-boneco-pensando-4.gif"
img_parede_path = "img/parede_madeira_1.jpg"
chao_path = "img/chao_paralelepipedo.jpg"
cachorro_path = "img/animated-dog-image-0049.gif"

path_to_image = img_path
FORMAT = "RGBA"

def pil_to_game(img):
    data = img.tobytes("raw", FORMAT)
    return pygame.image.fromstring(data, img.size, FORMAT)

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert(FORMAT)

def init():
    return pygame.display.set_mode(size)

def exit():
    pygame.quit()

# def draw_text(texto='Olá mundo', fontsize=12, posx=0, posy=0, width=100, height=150):
#     font = pygame.font.Font('freesambold.ttf', fontsize)
#     pygame.draw.rect(screen, (255, 255, 255), (posx, posy, width, height))
#     text = font.render = (texto, True, (0, 0, 0))
#     return text


def draw_text(texto="Game Start!", coords = ( DISPLAYSURF.get_width()/2, DISPLAYSURF.get_height()/8), size=60):
    myfont = pygame.font.SysFont('Comic Sans MS', size)
    textsurface = myfont.render(texto, True, (255, 255, 255))
    screen.blit(textsurface, coords)


def carregar_som(som):
    som = pygame.mixer.Sound(som)
    som.set_volume(1)
    som.play(-1)

def escrever_arquivo():
    with open('data.dat', 'w+') as f:
        f.writelines([
                      'Este boneco está passeando com seu carrocho',
                      'aproveitando para ler um livro',
                      'ele deve ter cuidado pois está caminhando sem olhar para o chão'
        ])

def ler_arquivo():
    data = ""
    with open('data.dat', 'r') as f:
           data += f.read()

    return data

def main(screen):

    pygame.mixer.init()

    # gravar aquivos para posterior leitura
    escrever_arquivo()

    gif_img = Image.open(path_to_image)
    cachorro = Image.open(cachorro_path)

    carregar_som("sons/forest1.wav")
    parede = pygame.image.load(img_parede_path)

    #ceu = pygame.image.load("img/universo_estrelado.gif")
    ceu = Image.open("img/universo_estrelado.gif")

   # chao
    chao = pygame.image.load(chao_path)

    if not getattr(gif_img, "is_animated", False):
        print(f"Imagem em {path_to_image} não é um gif animado")
        return

    current_frame = 0

    i = 0
    passos = 0

    while True:
        frame = pil_to_game(get_gif_frame(gif_img, current_frame))
        frame_ceu = pil_to_game(get_gif_frame(ceu, current_frame))
        frame_cachorro = pil_to_game(get_gif_frame(cachorro, current_frame))

        screen.fill((0, 0, 0))

        screen.blit(frame_ceu, (0, 0))
        screen.blit(parede, (0, 300))
        #screen.blit(chao, (0, 300))
        screen.blit(frame_cachorro, (0 +i -5, DISPLAYSURF.get_height() - 200))

        screen.blit(frame, (0 + i, DISPLAYSURF.get_height() - 400))

        # Escrever na tela
        draw_text("Inicio do Jogo")
        passos += 12

        draw_text("Passos do boneco: " + str(passos), coords=(DISPLAYSURF.get_height() -200, DISPLAYSURF.get_width()/9))
        draw_text("Carregamento de texto,  som e imagens - Prof. Wanderlei Silva do Carmo ", coords=(DISPLAYSURF.get_height() - 200, DISPLAYSURF.get_width() / 6), size=24)


        #Escrever texto em um retangulo na tela
        draw_text(ler_arquivo(), coords=(100, 300, 300, 60), size=18)



        i += 12

        if i > DISPLAYSURF.get_width() -100:
            i = -100
        # current_frame = (current_frame +1) % gif_img.n_frames
        current_frame = (current_frame + 1) % cachorro.n_frames

        pygame.display.flip()

        clock.tick(12)
        # pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    try:
        screen = init()
        main(screen)
    finally:
        exit()