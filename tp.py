import pygame
import screeninfo

# 初始化 pygame
pygame.init()

# 获取副屏信息（假设副屏为第二个屏幕）
screen = screeninfo.get_monitors()[1]
screen_width, screen_height = screen.width, screen.height

# 创建全屏窗口并设置位置为副屏
#window = pygame.display.set_mode((0, 0), pygame.NOFRAME)
#window = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE,0,1) # 设置窗口在第二块显示器上显示，display_index = 1

window = pygame.display.set_mode((screen_width, screen_height),  pygame.NOFRAME,0,1) # 设置窗口在第二块显示器上显示，display_index = 1

pygame.display.set_caption("Display on Secondary Screen")

# 加载图片
image = pygame.image.load("c:\\R-C.jpg")
sz = image.get_size()

#显示版本
score = '0.0.1'
window.fill((0,0,0))
font = pygame.font.Font(None, 50)
score_text = font.render(f"VER: {score}  == {sz}, Screen: {screen_width} x {screen_height}", 1, (255,0,0))
window.blit(score_text, (20, 20))
pygame.display.flip()

#显示图片    
window.blit(image, (screen_width//2 - sz[0]//2, screen_height//2 - sz[1]//2))
pygame.display.flip()
    
# 显示图片
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()