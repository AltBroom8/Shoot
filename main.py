import pyglet
from Bolita import Bolita
from Rectangulo import Rectangulo
from Texto import Texto


# Crea una instancia de la ventana
window = pyglet.window.Window(width=1050, height=740, caption="Jueguito que hice en js traducido a python")
batch = pyglet.graphics.Batch()

imagen1 = pyglet.image.load('Imagenes/cuadrado1.jpg')
imagen2 = pyglet.image.load('Imagenes/cuadrado2.jpeg')

jugador1 = imagen1.get_texture()
jugador2 = imagen2.get_texture()

disparo1 = None
boom1 = False
contvida2 = 5

disparo2 = None
boom2 = False
contvida1 = 5

final = False
ganador = None
j1posx = 240
j1posy = 350
j2posx = 760
j2posy = 350

# Haciendo las paredes
paredAbajo = Rectangulo(0, 100, 1050, 10, color=(255, 255, 255), batch=batch)
paredArriba = Rectangulo(0, 640, 1050, 10, color=(255, 255, 255), batch=batch)
paredIzquierda = Rectangulo(0, 100, 10, 540, color=(255, 255, 255), batch=batch)
paredDerecha = Rectangulo(1040, 100, 10, 540, color=(255, 255, 255), batch=batch)
paredCentral = Rectangulo(525, 100, 10, 540, color=(255, 255, 255), batch=batch)

# Haciendo las barras de vida

vida1 = Rectangulo(80, 20, 350, 60, color=(255, 229, 97), batch=batch)
vida2 = Rectangulo(620, 20, 350, 60, color=(255, 229, 97), batch=batch)

barritas1 = [Rectangulo(90, 30, 50, 40, color=(74, 255, 116), batch=batch),
             Rectangulo(160, 30, 50, 40, color=(74, 255, 116), batch=batch),
             Rectangulo(230, 30, 50, 40, color=(74, 255, 116), batch=batch),
             Rectangulo(300, 30, 50, 40, color=(74, 255, 116), batch=batch),
             Rectangulo(370, 30, 50, 40, color=(74, 255, 116), batch=batch)]

barritas2 = [Rectangulo(630, 30, 50, 40, color=(74, 255, 116), batch=batch),
             Rectangulo(700, 30, 50, 40, color=(74, 255, 116), batch=batch),
             Rectangulo(770, 30, 50, 40, color=(74, 255, 116), batch=batch),
             Rectangulo(840, 30, 50, 40, color=(74, 255, 116), batch=batch),
             Rectangulo(910, 30, 50, 40, color=(74, 255, 116), batch=batch)]
#Haciendo los textos

player1text = Texto('PLAYER 1',
                          font_name='Futura',
                          font_size=30,
                          x=180, y=680)
player2text = Texto('PLAYER 2',
                          font_name='Futura',
                          font_size=30,
                          x=700, y=680)

teclas_presionadas = {pyglet.window.key.W: False, pyglet.window.key.S: False, pyglet.window.key.A: False,
                      pyglet.window.key.D: False, pyglet.window.key.UP: False, pyglet.window.key.DOWN: False,
                      pyglet.window.key.LEFT: False, pyglet.window.key.RIGHT: False, pyglet.window.key.C: False,
                      pyglet.window.key.M: False,pyglet.window.key.R: False, pyglet.window.key.ESCAPE: False}

def actualizar(dt):
    global j1posx, j1posy,disparo1,boom1,barritas2,contvida2
    global j2posx, j2posy,disparo2,boom2,barritas1,contvida1
    global final,ganador
    if final is False:
        if (teclas_presionadas[pyglet.window.key.W]  and j1posy< 590):
            j1posy += 5  # Mueve hacia arriba
        if teclas_presionadas[pyglet.window.key.S] and j1posy > 110:
            j1posy -= 5  # Mueve hacia abajo
        if teclas_presionadas[pyglet.window.key.A] and j1posx > 10:
            j1posx -= 5  # Mueve hacia la izquierda
        if teclas_presionadas[pyglet.window.key.D] and j1posx < 475:
            j1posx += 5  # Mueve hacia la derecha
        if teclas_presionadas[pyglet.window.key.C] and boom1 is False:
            disparo1 = Bolita(j1posx+25, j1posy+25, 12, color=(255, 0, 0), batch=batch);
            boom1 = True
        if teclas_presionadas[pyglet.window.key.UP] and j2posy < 590:
            j2posy += 5  # Mueve hacia arriba
        if teclas_presionadas[pyglet.window.key.DOWN] and j2posy > 110:
            j2posy -= 5  # Mueve hacia abajo
        if teclas_presionadas[pyglet.window.key.LEFT] and j2posx > 535:
            j2posx -= 5  # Mueve hacia la izquierda
        if teclas_presionadas[pyglet.window.key.RIGHT] and j2posx < 990:
            j2posx += 5  # Mueve hacia la derecha
        if teclas_presionadas[pyglet.window.key.M] and boom2 is False:
            disparo2 = Bolita(j2posx + 25, j2posy + 25, 12, color=(0, 0, 255), batch=batch);
            boom2 = True

        if disparo1 is not None and disparo2 is not None:
            if (disparo1.x + disparo1.radius >= disparo2.x) and \
                    (disparo1.x <= disparo2.x + disparo2.radius) and \
                    (disparo1.y + disparo1.radius >= disparo2.y) and \
                    (disparo1.y <= disparo2.y + disparo2.radius):
                disparo1 = None
                disparo2 = None
                boom1 = False
                boom2 = False
        if disparo1 is not None:
            disparo1.x += 15
            if (disparo1.x + disparo1.radius >= j2posx) and \
                    (disparo1.x <= j2posx + 50) and \
                    (disparo1.y + disparo1.radius >= j2posy) and \
                    (disparo1.y <= j2posy + 50):

                if(contvida2>0):
                    barritas2.pop();
                contvida2 -= 1
                if contvida2 == 0:
                    final = True
                    ganador = 'Jugador 1'
                disparo1 = None
                boom1 = False
                disparo1 = None
            elif disparo1.x > 1080:
                disparo1 = None
                boom1 = False
        if disparo2 is not None:
            disparo2.x -= 15
            if (disparo2.x + disparo2.radius >= j1posx) and \
                    (disparo2.x <= j1posx + 50) and \
                    (disparo2.y + disparo2.radius >= j1posy) and \
                    (disparo2.y <= j1posy + 50):

                if(contvida1>0):
                    barritas1.pop();
                contvida1 -= 1
                if contvida1 == 0:
                    final = True
                    ganador = 'Jugador 2'
                disparo2 = None
                boom2 = False
                disparo2 = None
            elif disparo2.x < 0:
                disparo2 = None
                boom2 = False
    else:
        if teclas_presionadas[pyglet.window.key.R]:

            disparo1 = None
            boom1 = False
            disparo2 = None
            boom2 = False
            contvida1 = 5
            contvida2 = 5
            barritas1 = [Rectangulo(90, 30, 50, 40, color=(74, 255, 116), batch=batch),
                         Rectangulo(160, 30, 50, 40, color=(74, 255, 116), batch=batch),
                         Rectangulo(230, 30, 50, 40, color=(74, 255, 116), batch=batch),
                         Rectangulo(300, 30, 50, 40, color=(74, 255, 116), batch=batch),
                         Rectangulo(370, 30, 50, 40, color=(74, 255, 116), batch=batch)]

            barritas2 = [Rectangulo(630, 30, 50, 40, color=(74, 255, 116), batch=batch),
                         Rectangulo(700, 30, 50, 40, color=(74, 255, 116), batch=batch),
                         Rectangulo(770, 30, 50, 40, color=(74, 255, 116), batch=batch),
                         Rectangulo(840, 30, 50, 40, color=(74, 255, 116), batch=batch),
                         Rectangulo(910, 30, 50, 40, color=(74, 255, 116), batch=batch)]
            j1posx = 240
            j1posy = 350
            j2posx = 760
            j2posy = 350
            final = False
        if teclas_presionadas[pyglet.window.key.ESCAPE]:
            pyglet.app.exit()


pyglet.clock.schedule_interval(actualizar, 1/60.0)

@window.event
def on_key_press(symbol, modifiers):
    if symbol in teclas_presionadas:
        teclas_presionadas[symbol] = True

@window.event
def on_key_release(symbol, modifiers):
    if symbol in teclas_presionadas:
        teclas_presionadas[symbol] = False

@window.event
def on_draw():
    window.clear()
    if not final:
        batch.draw()
        player1text.draw()
        player2text.draw()
        jugador1.blit(j1posx,j1posy,width = 50,height =50)
        jugador2.blit(j2posx,j2posy, width=50, height=50)
    else:
        mensaje_ganador = pyglet.text.Label(f'¡{ganador} gana!', font_size=36, x=window.width // 2,
                                            y=window.height // 2, anchor_x='center', anchor_y='center')
        mensaje_ganador.draw()

        mensaje_secundario = pyglet.text.Label('Pulsa R para Reiniciar la partida o Esc para Salir', font_size=18, x=window.width // 2,
                                               y=window.height // 2 - 50, anchor_x='center', anchor_y='center')
        mensaje_secundario.draw()


# Ejecuta la ventana
pyglet.app.run()




