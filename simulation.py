import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown



def main():

    pygame.init()

    HEIGHT = 480
    WIDTH = 640


    screen = pygame.display.set_mode([800, 480])

    launch_button = Button(
        screen, 660, 400, 100, 40,
        text="Launch!", fontSize=30, radius=1, pressedColour=(150,0,0)
    )

    v_desc = TextBox(screen, 640, 70, 140, 30, fontSize=20, colour=(255,255,255), borderColour=(255,255,255), borderThickness=1, placeholderText="Voltage [10V-100V]")
    v_slider = Slider(screen, 650, 100, 120, 10, min=10, max=100, step=1)
    v_output = TextBox(screen, 680, 120, 60, 20, fontSize=20, borderColour=(20,20,20), borderThickness=1)

    b_desc = TextBox(screen, 640, 150, 140, 30, fontSize=20, colour=(255,255,255), borderColour=(255,255,255), borderThickness=1, placeholderText="Voltage [10V-100V]")
    b_slider = Slider(screen, 650, 180, 120, 10, min=1, max=100, step=1)
    b_output = TextBox(screen, 680, 200, 60, 20, fontSize=20, borderColour=(20,20,20), borderThickness=1)

    particle_dropdown = Dropdown(screen, 660, 250, 100, 40, name='Select particle',
                                 choices=["1p", "1p1n", "2p", "2p1n", "2p2n"])


    v_desc.disable()
    v_output.disable()
    b_desc.disable()
    b_output.disable()

    running = True

    while running:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, (255, 0, 0), (320, 240), 160)
        pygame.draw.circle(screen, (255, 255, 255), (320, 240), 158)
        v_desc.setText("Voltage [10V-100V]")
        v_output.setText(str(v_slider.getValue())[:5])
        b_desc.setText("Magnetic Field [1T-100T]")
        b_output.setText(str(b_slider.getValue())[:5])
        pygame_widgets.update(events)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()