import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.toggle import Toggle
import numpy as np
from cyclotron_calculation import calculate_path

def add(x, y):
    print(x+y)

BASE_HEIGHT = 960
BASE_WIDTH = 1280
BASE_CIRCLE_SIZE = BASE_WIDTH / 2

def main():

    pygame.init()

    screen = pygame.display.set_mode([BASE_WIDTH+160, BASE_HEIGHT])

    iterator = 0

    particle_position_x, particle_position_y = ([0],[0])

    q = 1
    m = 1
    v = 100
    b = 2.0
    negation_q = False
    #particle_position_x, particle_position_y = calculate_path(3,2,100,2.0)

    def launch():
        nonlocal particle_position_x
        nonlocal particle_position_y
        nonlocal iterator
        iterator = 0
        if negation_q:
            particle_position_x, particle_position_y = calculate_path(q*-1,m,v,b)
        else:
            particle_position_x, particle_position_y = calculate_path(q,m,v,b)

    v_desc = TextBox(screen, BASE_WIDTH, 70, 140, 30, fontSize=20, colour=(255,255,255), borderColour=(255,255,255), borderThickness=1)
    v_slider = Slider(screen, BASE_WIDTH+10, 100, 120, 10, min=1, max=500, step=1, initial=100)
    v_output = TextBox(screen, BASE_WIDTH+30, 120, 60, 20, fontSize=20, borderColour=(20,20,20), borderThickness=1)

    b_desc = TextBox(screen, BASE_WIDTH, 150, 140, 30, fontSize=20, colour=(255,255,255), borderColour=(255,255,255), borderThickness=1)
    b_slider = Slider(screen, BASE_WIDTH+10, 180, 120, 10, min=0.0, max=10, step=0.1, initial=2.0)
    b_output = TextBox(screen, BASE_WIDTH+30, 200, 60, 20, fontSize=20, borderColour=(20,20,20), borderThickness=1)

    m_desc = TextBox(screen, BASE_WIDTH, 230, 140, 30, fontSize=20, colour=(255,255,255), borderColour=(255,255,255), borderThickness=1)
    m_slider = Slider(screen, BASE_WIDTH+10, 260, 120, 10, min=1, max=100, step=1, initial=1)
    m_output = TextBox(screen, BASE_WIDTH+30, 280, 60, 20, fontSize=20, borderColour=(20,20,20), borderThickness=1)

    q_desc = TextBox(screen, BASE_WIDTH, 310, 140, 30, fontSize=20, colour=(255,255,255), borderColour=(255,255,255), borderThickness=1)
    q_slider = Slider(screen, BASE_WIDTH+10, 340, 120, 10, min=1, max=100, step=1, initial=1)
    q_output = TextBox(screen, BASE_WIDTH+30, 360, 60, 20, fontSize=20, borderColour=(20,20,20), borderThickness=1)

    negative_q_desc = TextBox(screen, BASE_WIDTH, 390, 140, 30, fontSize=20, colour=(255,255,255), borderColour=(255,255,255), borderThickness=1)
    negative_q_toggle = Toggle(screen, BASE_WIDTH+50, 420, 30, 10)

    launch_button = Button(
        screen, BASE_WIDTH+20, 450, 100, 40,
        text="Launch!", fontSize=30, radius=1, pressedColour=(150,0,0),
        onRelease=launch
    )

    v_desc.disable()
    v_output.disable()
    b_desc.disable()
    b_output.disable()
    m_desc.disable()
    m_output.disable()
    q_desc.disable()
    q_output.disable()
    negative_q_desc.disable()

    running = True

    semicircle_rect = pygame.Rect(BASE_WIDTH/4, BASE_HEIGHT/6, BASE_CIRCLE_SIZE, BASE_CIRCLE_SIZE)
    
    while running:
        print(iterator)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        q = q_slider.getValue()
        m = m_slider.getValue()
        v = v_slider.getValue()
        b = b_slider.getValue()
        negation_q = negative_q_toggle.getValue()

        screen.fill((255, 255, 255))

        left_color = (0,0,255)
        right_color = (255,0,0)
        if(particle_position_x[iterator] < 0):
            left_color = (255,0,0)
            right_color = (0,0,255)

        pygame.draw.arc(screen, left_color, semicircle_rect, np.radians(90), np.radians(270), 2)
        pygame.draw.arc(screen, right_color, semicircle_rect, np.radians(270), np.radians(90), 2)
        for i in range(iterator):
            pygame.draw.circle(screen, (0,255,0), (BASE_WIDTH/2+BASE_WIDTH*5*particle_position_x[i],BASE_HEIGHT/2+BASE_WIDTH*5*particle_position_y[i]), 1)
        v_desc.setText("Voltage [1V-500V]")
        v_output.setText(str(v_slider.getValue())[:5])
        b_desc.setText("Magnetic Field [0T-10T]")
        b_output.setText(str(b_slider.getValue())[:3])
        m_desc.setText("Mass [1-100 proton mass]")
        m_output.setText(str(m_slider.getValue())[:3])
        q_desc.setText("Charge [1-100 proton mass]")
        q_output.setText(str(q_slider.getValue())[:3])
        negative_q_desc.setText("Negative charge")

        if iterator < len(particle_position_x)-1:
            iterator += 1

        pygame_widgets.update(events)
        pygame.display.update()

        

    pygame.quit()

if __name__ == '__main__':
    main()