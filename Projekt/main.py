import pygame as pg, sys, asyncio
from scene import Scene
from menu import MenuScene
from config import *
from assets import *
from game import GameScene


async def main():
    pg.mixer.init()
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((SCREEN_W, SCREEN_H)) 
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
    loop = asyncio.get_event_loop()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == SCENEEVENT:
                print(f"Switching scene to: {event.scene_type}")

                if event.scene_type == 'game':
                    scene = GameScene(screen)
                    asyncio.run_coroutine_threadsafe(GameScene.play_music(1, 'Projekt/assets/music/test.mp3'), loop)

                elif event.scene_type == 'opts':
                    pass  

            elif event.type in scene.process:
                scene.process[event.type](event)
            
        scene.update()
        scene.draw()
        pg.display.flip()
        clock.tick(FPS)

        await asyncio.sleep(0.01)

    pg.quit()

if __name__ == '__main__':
    asyncio.run(main())




