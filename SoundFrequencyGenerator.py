from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

"""если работа на linux или macos, то нужно импортировать библиотеки pygame и numpy, вместо winsound,
                   предварительно установив их через консоль CMD
                   pip install pygame
                   pip install numpy"""
import winsound

"""инициализация pygame и его модуля для работы со звуком"""
# import pygame
# import numpy as np
# pygame.init()
# pygame.mixer.init()

class FirstApp(App):
    def build(self):
        main_layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        self.solution = Label(font_size = 60)
        main_layout.add_widget(self.solution)

        button = [['-', '+'], ['50 Гц', '100 Гц', '500 Гц', '1000 Гц'],
                  ['Start']]

        for lay in button:
            vr = BoxLayout()
            for name in lay:
                button = Button(text = name,
                                pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                                background_color = [0.9, 0.9, 0, 1],
                                font_size = 45)

                if name == 'Start':
                    button.bind(on_press = self.start_solution)
                else:
                    button.bind(on_press = self.on_solution)

                vr.add_widget(button)

            main_layout.add_widget(vr)

        self.solution.text = '50 Гц'
        return main_layout

    def start_solution(self, instance):
        if self.solution.text and self.solution.text != "Error: Incorrect frequency":
            try:
                winsound.Beep(int(self.solution.text.split()[0]), 2000)
            except:
                self.solution.text = "Error: Incorrect frequency"
        else:
            self.solution.text = "Error: Incorrect frequency"

    """для linux и macos заменить на данный метод: """

    # def start_solution(self, instance):
    #     if self.solution.text \
    #             and self.solution.text != "Error: Incorrect frequency":
    #         try:
    #             frequency = int(self.solution.text.split()[0])
    #             duration = 2
    #             num_samples = int(88200 * duration)
    #             time_array = np.arange(num_samples) / 88200
    #             samples = (np.sin(2 * np.pi * frequency * time_array) * 32767).astype(np.int16)
    #             sound = pygame.mixer.Sound(samples)
    #             sound.play()
    #         except:
    #             self.solution.text = "Error: Incorrect frequency"
    #     else:
    #         self.solution.text = "Error: Incorrect frequency"

    def on_solution(self, instance):
        if instance.text == "50 Гц":
            self.solution.text = "50 Гц"
        elif instance.text == "100 Гц":
            self.solution.text = "100 Гц"
        elif instance.text == "500 Гц":
            self.solution.text = "500 Гц"
        elif instance.text == "1000 Гц":
            self.solution.text = "1000 Гц"
        elif instance.text == "+":
            try:
                if self.solution.text != "Error: Incorrect frequency":
                    self.solution.text = str(int(self.solution.text.split()[0]) + 1) + " Гц"
                else:
                    self.solution.text = "1" + " Гц"
            except:
                self.solution.text = "50 Гц"
        elif instance.text == "-":
            try:
                if self.solution.text != "Error: Incorrect frequency":
                    self.solution.text = str(int(self.solution.text.split()[0]) - 1) + " Гц"
            except:
                self.solution.text = "50 Гц"
        if self.solution.text != "Error: Incorrect frequency":
            if int(self.solution.text.split()[0]) <= 0:
                self.solution.text = "Error: Incorrect frequency"


if __name__ == '__main__':
    FirstApp().run()