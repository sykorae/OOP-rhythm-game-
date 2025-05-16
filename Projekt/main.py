import pygame as pg, sys
from scene import Scene
from menu import MenuScene
from config import *
from game import GameScene


def main():
    pg.mixer.init()
    pg.init()
    clock = pg.time.Clock()
    screen: pg.Surface = pg.display.set_mode((SCREEN_W, SCREEN_H)) 
    pg.display.set_caption(CAPTION)

    scenes: dict[SceneType, Scene] = {
        'menu': MenuScene(screen),
        #'stgs': SettingsScene(screen),
        'game': GameScene(screen),
    }

    scene: Scene = scenes['menu']
    scene.start()
    scene.draw()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == SCENEEVENT:
                print(f"Switching scene to: {event.scene_type}")

                if event.scene_type == 'game':
                    scene = GameScene(screen)
                    scene.start()

                elif event.scene_type == 'opts':
                    pass  

            elif event.type in scene.process:
                scene.process[event.type](event)
            
        scene._draw()
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == '__main__':
    main()




