from globals import *
from snake import *
from food import *

class Screen: 
    def draw(self, window):
        pygame.draw.rect(window, NAVY, (0, 0, WIDTH, HEIGHT))
        pygame.draw.rect(window, WHITE, (0, 2*TILE_SIZE, WIDTH-1, HEIGHT-2*TILE_SIZE-1), 2)
        for row in range(TILE_COUNT):
            curr_x = 2
            if row % 2 == 1:
                curr_x = TILE_SIZE + 2 
            curr_y = 2*TILE_SIZE + 2 + TILE_SIZE*row
            for col in range(TILE_COUNT//2):
                pygame.draw.rect(window, LIGHT_NAVY, (curr_x, curr_y, TILE_SIZE, TILE_SIZE))
                curr_x += 2*TILE_SIZE 

def game():
    run = True
    clock = pygame.time.Clock()
    screen = Screen()
    start_x = 2
    start_y = 2 * (TILE_SIZE+1)
    snake = Snake(start_x, start_y)
    food = Food(start_x, start_y+1)
    food.init_coords()
    score = 0
    score_font = pygame.font.SysFont("comicsans", TILE_SIZE * 2)
    over = False

    def redraw_window():
        # Draw Background
        screen.draw(WINDOW)
        score_label = score_font.render(f"Score: {score}", 1, (WHITE))
        WINDOW.blit(score_label, (TILE_SIZE*2//5, TILE_SIZE*2//5))
        if food.exists():
            food.draw(WINDOW)
        else:
            # Gets the next food position that is not on the snake
            while not food.check_valid_placement(snake):
                food.set_coords()
            food.flip_exists()

        if not over:
            snake.draw(WINDOW)
        else:
            snake.drawPrev(WINDOW)
            pygame.draw.rect(WINDOW, NAVY, (90,90,90,90))

        pygame.display.update()

    while(run):
        clock.tick(FPS)

        if snake.collision():
            over = True

        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_SPACE:
            #        snake.add_tile()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            snake.change_dir("left")
        elif keys[pygame.K_d]:
            snake.change_dir("right")
        elif keys[pygame.K_w]:
            snake.change_dir("up")
        elif keys[pygame.K_s]:
            snake.change_dir("down")

        if (food.get_coords() == snake.get_coords()):
            score += 1
            snake.add_tile()
            food.flip_exists()
        
        if not over:
            if snake.timer == snake.cool_down:
                snake.move()
                snake.timer = 0
            else:
                snake.timer += 1