import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        with open('config.txt', 'r') as f:
            items = [item.rstrip('\n\r') for item in f.readlines()]
            for item in items:
                if item.startswith('image_title'):
                    image_title = item.split(' ')[1]
                elif item.startswith('percentage_alpha_decrease'):
                    alpha_decrease = float(item.split(' ')[1])
                elif item.startswith('final_image_width'):
                    final_image_width = int(item.split(' ')[1])
                elif item.startswith('final_image_height'):
                    final_image_height = int(item.split(' ')[1])
                elif item.startswith('degree_increase'):
                    degree_increase = int(item.split(' ')[1])
                elif item.startswith('rotate_left'):
                    rotation_factor = {'True':1, 'False':-1}[item.split(' ')[1]]

        self.display = pygame.display.set_mode((final_image_width, final_image_height))
        pygame.display.set_caption('Thing')
        self.clock = pygame.time.Clock()

        self.image = pygame.image.load(image_title).convert()
        self.images = []
        alpha = 255
        for angle in range(0, 360, degree_increase):
            angle *= rotation_factor
            image = pygame.transform.rotate(pygame.transform.scale(self.image, (final_image_width, final_image_height)), angle)
            image.set_alpha(alpha)
            alpha = round(alpha * alpha_decrease)
            self.images.append(image)

        self.centre = (final_image_width//2, final_image_height//2)

    def main(self):
        done = False
        while not done:
            self.display.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    raise SystemExit

            for image in self.images:
                rect = image.get_rect()

                x = self.centre[0] - (rect.width // 2)
                y = self.centre[1] - (rect.height // 2)

                self.display.blit(image, (x, y))

            pygame.display.flip()
            pygame.image.save(self.display, 'final_image.png')

            done = True

            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.main()
