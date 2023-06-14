import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
import numpy as np
from cyclotron_calculation import calculate_path

BASE_HEIGHT = 960
BASE_WIDTH = 1280
BASE_CIRCLE_SIZE = BASE_WIDTH / 2

def main():

    pygame.init()

    screen = pygame.display.set_mode([BASE_WIDTH+160, BASE_HEIGHT])

    

    v_desc = TextBox(screen, BASE_WIDTH, 70, 140, 30, fontSize=20, colour=(255,255,255), borderColour=(255,255,255), borderThickness=1)
    v_slider = Slider(screen, BASE_WIDTH+10, 100, 120, 10, min=1, max=500, step=1)
    v_output = TextBox(screen, BASE_WIDTH+30, 120, 60, 20, fontSize=20, borderColour=(20,20,20), borderThickness=1)

    b_desc = TextBox(screen, BASE_WIDTH, 150, 140, 30, fontSize=20, colour=(255,255,255), borderColour=(255,255,255), borderThickness=1)
    b_slider = Slider(screen, BASE_WIDTH+10, 180, 120, 10, min=0.0, max=10, step=0.1)
    b_output = TextBox(screen, BASE_WIDTH+30, 200, 60, 20, fontSize=20, borderColour=(20,20,20), borderThickness=1)

    particle_dropdown = Dropdown(screen, BASE_WIDTH+20, 250, 100, 40, name='Select particle',
                                 choices=["1p", "1p1n", "2p", "2p1n", "2p2n"])


    launch_button = Button(
        screen, BASE_WIDTH+20, 400, 100, 40,
        text="Launch!", fontSize=30, radius=1, pressedColour=(150,0,0)
    )

    v_desc.disable()
    v_output.disable()
    b_desc.disable()
    b_output.disable()

    running = True

    semicircle_rect = pygame.Rect(BASE_WIDTH/4, BASE_HEIGHT/6, BASE_CIRCLE_SIZE, BASE_CIRCLE_SIZE)
    
    pposx, pposy = calculate_path(1,1,100,2.0)

    iterator = 0

    

    while running:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        screen.fill((0, 0, 0))

        left_color = (0,0,255)
        right_color = (255,0,0)
        if(pposx[iterator] < 0):
            left_color = (255,0,0)
            right_color = (0,0,255)

        pygame.draw.arc(screen, left_color, semicircle_rect, np.radians(90), np.radians(270), 2)
        pygame.draw.arc(screen, right_color, semicircle_rect, np.radians(270), np.radians(90), 2)
        for i in range(iterator):
            pygame.draw.circle(screen, (0,255,0), (BASE_WIDTH/2+BASE_WIDTH*5*pposx[i],BASE_HEIGHT/2+BASE_WIDTH*5*pposy[i]), 1)
        v_desc.setText("Voltage [1V-500V]")
        v_output.setText(str(v_slider.getValue())[:5])
        b_desc.setText("Magnetic Field [0T-10T]")
        b_output.setText(str(b_slider.getValue())[:5])
        pygame_widgets.update(events)
        pygame.display.update()

        if iterator < len(pposx)-1:
            iterator += 1
        

    pygame.quit()

if __name__ == '__main__':
    main()