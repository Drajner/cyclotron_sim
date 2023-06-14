import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.toggle import Toggle
import numpy as np
from cyclotron_calculation import calculate_path

BASE_HEIGHT = 960
BASE_WIDTH = 1280
BASE_CIRCLE_SIZE = BASE_WIDTH / 2


class CyclotronSimulator:

    def __init__(self):
        self.text_boxes = None
        self.launch_button = None
        self.ui_elements = None
        self.particle_position = None
        self.iterator = None
        pygame.init()
        self.screen = pygame.display.set_mode([BASE_WIDTH + 160, BASE_HEIGHT])
        self.init_ui_elements()

    def init_ui_elements(self):
        self.ui_elements = {
            'v': Slider(self.screen, BASE_WIDTH - 50, 100, 120, 10, min=1, max=500, step=1, initial=100),
            'b': Slider(self.screen, BASE_WIDTH - 50, 180, 120, 10, min=0.0, max=10, step=0.1, initial=2.0),
            'm': Slider(self.screen, BASE_WIDTH - 50, 260, 120, 10, min=1, max=100, step=1, initial=1),
            'q': Slider(self.screen, BASE_WIDTH - 50, 340, 120, 10, min=1, max=100, step=1, initial=1),
            'negative_q': Toggle(self.screen, BASE_WIDTH - 10, 420, 30, 10)
        }

        self.launch_button = Button(
            self.screen, BASE_WIDTH - 40, 470, 100, 40, text="Launch!", fontSize=30,
            radius=1, pressedColour=(150, 0, 0), onRelease=self.launch
        )

        self.text_boxes = {
            'v': TextBox(self.screen, BASE_WIDTH - 80, 70, 140, 30, fontSize=20, colour=(255, 255, 255),
                         borderColour=(255, 255, 255), borderThickness=1),
            'b': TextBox(self.screen, BASE_WIDTH - 80, 150, 140, 30, fontSize=20, colour=(255, 255, 255),
                         borderColour=(255, 255, 255), borderThickness=1),
            'm': TextBox(self.screen, BASE_WIDTH - 80, 230, 140, 30, fontSize=20, colour=(255, 255, 255),
                         borderColour=(255, 255, 255), borderThickness=1),
            'q': TextBox(self.screen, BASE_WIDTH - 80, 310, 140, 30, fontSize=20, colour=(255, 255, 255),
                         borderColour=(255, 255, 255), borderThickness=1),
            'negative_q': TextBox(self.screen, BASE_WIDTH - 40, 390, 140, 30, fontSize=20, colour=(255, 255, 255),
                                  borderColour=(255, 255, 255), borderThickness=1),
        }

    def launch(self):
        self.particle_position = calculate_path(
            self.ui_elements['q'].getValue() * (-1 if self.ui_elements['negative_q'].getValue() else 1),
            self.ui_elements['m'].getValue(),
            self.ui_elements['v'].getValue(),
            self.ui_elements['b'].getValue())
        self.iterator = 0

    def start(self):
        self.particle_position = ([0], [0])
        self.iterator = 0
        semicircle_rect = pygame.Rect(BASE_WIDTH / 4, BASE_HEIGHT / 6, BASE_CIRCLE_SIZE, BASE_CIRCLE_SIZE)

        running = True

        while running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return

            self.screen.fill((255, 255, 255))

            left_color, right_color = (0, 0, 255), (255, 0, 0)
            if self.particle_position[0][self.iterator] < 0:
                left_color, right_color = right_color, left_color

            pygame.draw.arc(self.screen, left_color, semicircle_rect, np.radians(90), np.radians(270), 2)
            pygame.draw.arc(self.screen, right_color, semicircle_rect, np.radians(270), np.radians(90), 2)
            for i in range(self.iterator):
                pygame.draw.circle(self.screen, (0, 255, 0),
                                   (BASE_WIDTH / 2 + BASE_WIDTH * 5 * self.particle_position[0][i],
                                    BASE_HEIGHT / 2 + BASE_WIDTH * 5 * self.particle_position[1][i]), 1)

            self.text_boxes['v'].setText(f"Voltage [1V-500V]: {self.ui_elements['v'].getValue():.2f}V")
            self.text_boxes['b'].setText(f"Magnetic Field [0T-10T]: {self.ui_elements['b'].getValue():.2f}T")
            self.text_boxes['m'].setText(f"Mass [1-100 proton mass]: {self.ui_elements['m'].getValue():.2f}")
            self.text_boxes['q'].setText(f"Charge [1-100 proton mass]: {self.ui_elements['q'].getValue():.2f}")
            self.text_boxes['negative_q'].setText(
                "Negative charge" if self.ui_elements['negative_q'].getValue() else "Positive charge")

            if self.iterator < len(self.particle_position[0]) - 1:
                self.iterator += 1

            pygame_widgets.update(events)
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    simulator = CyclotronSimulator()
    simulator.start()
