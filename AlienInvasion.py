import sys
import pygame
from settings import Settings

class AlienInvasion:
  
  def __init__(self):
      pygame.init()
      self.setting = Settings()

      self.screen = pygame.display.set_mode(
          (self.settings.screen_w,self.settings.screen_h)
          )
      pygame.display.set_caption(self.settings.name)

      self.bg = pygame.image.load(self.settings.bg_file)
      self.bg = pygame.transform.scale(self.bg, 
          (self.settings.screen_w, self.settings_h)
          )

      self.running = True
      self.clock = pygame.time.Clock()

  def run_game(self):
      while self.running:
          for event in pygame.event.git():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()

          pygame.display.flip()
          self.clock.tick(self.settings.FPS)

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()
