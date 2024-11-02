import pygame
import random


def main():
    pygame.init()

    # Настройка экрана игры
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Простая Змейка")

    BLOCK_SIZE = 20 # Размер 1 блока змейки
    speed = 10 # Скорость змейки
    FPS = 8 #количество кадров в секунду

    # Загрузка изображения для змейки
    snake_image = pygame.image.load("snake.png").convert_alpha()
    snake_image = pygame.transform.scale(snake_image, (BLOCK_SIZE, BLOCK_SIZE))

    # Координаты змейки и еды
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (BLOCK_SIZE, 0)

    # Создание нескольких единиц еды
    food_count = 5
    food = [(random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
             random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE) for _ in range(food_count)]

    # Основной цикл игры (управление змейкой при помощи клавиатуры)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                    direction = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                    direction = (BLOCK_SIZE, 0)
                elif event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                    direction = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                    direction = (0, BLOCK_SIZE)

        # Обновление положения змейки
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # Проверка на еду
        if snake[0] in food:
            food.remove(snake[0])
            food.append((random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                         random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE))
        else:
            snake.pop()

        # Проверка на столкновение с границами или самой собой
        if (new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake[1:]):
            running = False
            print("Игра окончена. Змейка врезалась!")

        # Отрисовка
        screen.fill((255, 255, 255))
        for segment in snake:
            screen.blit(snake_image, segment)
        for f in food:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(f[0], f[1], BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

