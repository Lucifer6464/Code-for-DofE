import pygame
import neat
import pickle
import time
import random
import os

WIDTH = 750
HEIGHT = 900
WHITE = (255, 255, 255)

PADDLE = pygame.transform.scale2x(pygame.image.load('imgs/paddle.png'))
BALL = pygame.transform.scale2x(pygame.image.load('imgs/ball.png'))
pygame.font.init()
STAT_FONT = pygame.font.Font('retro.ttf', 100)
LARGE_FONT = pygame.font.Font('retro.ttf', 120)

replay_winner = False
gen = 0
player_score = 0
AI_score = 0
game_over = False


# pygame.mixer.init()
# pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play(-1)


class PaddlePlayer:
    IMG = PADDLE

    def __init__(self, x, y):
        self.speed = 15
        self.x = x
        self.y = y
        self.img = self.IMG
        self.rect = self.img.get_rect()
        self.hitbox = (self.x - 5, self.y, 18, 150)

    def draw(self, sc):
        pass
        # sc.blit(PADDLE, (self.x, self.y))  # <---------------------
        # pygame.draw.rect(sc, (255, 0, 0), self.hitbox, 2)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 10:
            self.y -= self.speed
            self.hitbox = (self.x - 5, self.y, 18, 150)
        if keys[pygame.K_DOWN] and self.y < WIDTH - (self.img.get_height() // 14):
            self.y += self.speed
            self.hitbox = (self.x - 5, self.y, 18, 150)


class PaddleNEATAI:
    IMG = PADDLE

    def __init__(self, x, y):
        self.speed = 15
        self.x = x
        self.y = y
        self.img = self.IMG
        self.rect = self.img.get_rect()
        self.hitbox = (self.x + 1, self.y, 18, 150)

    def draw(self, sc):
        sc.blit(PADDLE, (self.x, self.y))
        # pygame.draw.rect(sc, (255, 0, 0), self.hitbox, 2)

    def move_up(self):
        self.y -= self.speed
        self.hitbox = (self.x + 1, self.y, 18, 150)

    def move_down(self):
        self.y += self.speed
        self.hitbox = (self.x + 1, self.y, 18, 150)


class PaddleAI:
    IMG = PADDLE

    def __init__(self, x, y):
        self.speed = 15
        self.x = x
        self.y = y
        self.img = self.IMG
        self.rect = self.img.get_rect()
        self.hitbox = (self.x + 1, self.y, 18, 150)

    def draw(self, sc):
        pass
        sc.blit(PADDLE, (self.x, self.y))  # <-----------------
        # pygame.draw.rect(sc, (255, 0, 0), self.hitbox, 2)

    def move_up(self):
        self.y -= self.speed
        self.hitbox = (self.x + 1, self.y, 18, 150)

    def move_down(self):
        self.y += self.speed
        self.hitbox = (self.x + 1, self.y, 18, 150)


class Ball:
    IMG = BALL

    def __init__(self, x, y):
        self.speed = 15
        self.angle = random.randrange(-12, 12)
        self.x = x
        self.y = y
        self.img = self.IMG
        self.rect = self.img.get_rect()
        self.hitbox = (self.x, self.y, 16, 16)

    def draw(self, sc):
        sc.blit(BALL, (self.x, self.y))
        # pygame.draw.rect(sc, (255, 0, 0), self.hitbox, 2)

    def move(self):
        global game_over
        global player_score
        global AI_score
        if self.x < 0:
            game_over = True
            player_score += 1
        if self.x > WIDTH:
            game_over = True  # <------------------
            AI_score += 1  # <--------------------------
            # self.collision()  # <-----------------
        if self.y < 0:
            self.angle *= -1
            if self.speed < 0:
                self.speed -= 0.5
            else:
                self.speed += 0.5
        if self.y > HEIGHT:
            self.angle *= -1
            if self.speed < 0:
                self.speed -= 0.5
            else:
                self.speed += 0.5
        self.y -= self.angle
        self.x -= self.speed
        self.hitbox = (self.x, self.y, 16, 16)

    def collision(self):
        # illusion of velocity and bounce using random to see how the AI responds
        self.speed *= -1
        self.angle += random.randrange(2, 5)
        if self.speed < 0:
            self.speed -= 0.5
        else:
            self.speed += 0.5
        value = random.randrange(1, 5)
        if value == 1:
            self.angle *= -1


def draw_window(sc, paddle_player, paddle_AI, ball, paddles):
    clock = pygame.time.Clock()
    sc.fill((0, 0, 0))
    paddle_player.draw(sc)
    paddle_AI.draw(sc)
    ball.draw(sc)
    for line in range(10):
        pygame.draw.rect(sc, WHITE, (WIDTH // 2, 0 + line * 95, 18, 50))
    for paddle in paddles:
        paddle.draw(sc)
    score_left = STAT_FONT.render(str(AI_score), 1, WHITE)
    sc.blit(score_left, (WIDTH // 2 - 150, 20))
    score_right = STAT_FONT.render(str(player_score), 1, WHITE)
    sc.blit(score_right, (WIDTH // 2 + 90, 20))
    pygame.display.update()
    clock.tick(30)  # 11111111111111111111111111111 (30 or 144 or 0)


def main(genomes, config):
    global gen
    global game_over
    global player_score
    global AI_score
    nets = []
    ge = []
    paddles = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        paddles.append(PaddleNEATAI(25, (HEIGHT // 2) - (PADDLE.get_height() // 2)))
        g.fitness = 0
        ge.append(g)

    ball = Ball(WIDTH // 2, HEIGHT // 2)
    paddle_player = PaddlePlayer(WIDTH - (PADDLE.get_width() * 2), (HEIGHT // 2) - (PADDLE.get_height() // 2))
    paddle_AI = PaddleAI(WIDTH - (PADDLE.get_width() * 2), (HEIGHT // 2) - (PADDLE.get_height() // 2))
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_s]:
            break
        if ball.y > paddle_AI.y and ball.y - paddle_AI.y < 15:
            pass
        elif ball.y > paddle_AI.y and paddle_AI.y < HEIGHT - 148:
            paddle_AI.move_down()
        elif ball.y < paddle_AI.y and paddle_AI.y > 0:
            paddle_AI.move_up()
        if len(paddles) > 0:
            pass
        else:
            if not replay_winner:
                player_score = 0
                AI_score = 0
            break
        for x, paddle in enumerate(paddles):
            output = nets[x].activate((paddle.y, abs(paddle.y - ball.y), abs(paddle.x - paddle.y)))
            if output[0] > 0.5 and paddle.y > -5:
                paddle.move_up()
            elif output[0] < 0.5 and paddle.y < HEIGHT - 120:
                paddle.move_down()
            if ball.x < 10:
                ge[x].fitness -= 6
            if ball.y - ball.img.get_height() / 2 < \
                    paddle.hitbox[1] + paddle.hitbox[3] and ball.y + ball.img.get_height() / 2 > \
                    paddle.hitbox[1]:
                if ball.x + ball.img.get_width() / 2 > \
                        paddle.hitbox[0] and ball.x - ball.img.get_width() / 2 < paddle.hitbox[0] + \
                        paddle.hitbox[2]:
                    ge[x].fitness += 3
                    ball.x += 7
                    # AI_score += 1  # <-------------------
                    ball.collision()

                if not replay_winner:
                    if player_score > 0:
                        if ge[x].fitness < player_score * 20:
                            ge[x].fitness -= 0.3
                            paddles.pop(x)
                            nets.pop(x)
                            ge.pop(x)
                    elif player_score > 4:
                        if ge[x].fitness < player_score * 30:
                            ge[x].fitness -= 0.4
                            paddles.pop(x)
                            nets.pop(x)
                            ge.pop(x)
                    elif player_score > 10:
                        if ge[x].fitness < player_score * 60:
                            ge[x].fitness -= 0.5
                            paddles.pop(x)
                            nets.pop(x)
                            ge.pop(x)
                    elif player_score > 20:
                        if ge[x].fitness < player_score * 150:
                            paddles.pop(x)
                            nets.pop(x)
                            ge.pop(x)
                    if game_over:
                        ball = Ball(WIDTH // 2, HEIGHT // 2)

            # if ball.y - ball.img.get_height() / 2 < paddle_player.hitbox[1] + paddle_player.hitbox[
            #     3] and ball.y + ball.img.get_height() / 2 > paddle_player.hitbox[1]:
            #     if ball.x + ball.img.get_width() / 2 > paddle_player.hitbox[0] and ball.x - ball.img.get_width() / 2 < \
            #             paddle_player.hitbox[0] + paddle_player.hitbox[2]:
            #         ball.x -= 7
            #         ball.collision()
            if ball.y - ball.img.get_height() / 2 < paddle_AI.hitbox[1] + paddle_AI.hitbox[
                3] and ball.y + ball.img.get_height() / 2 > paddle_AI.hitbox[1]:
                if ball.x + ball.img.get_width() / 2 > paddle_AI.hitbox[0] and ball.x - ball.img.get_width() / 2 < \
                        paddle_AI.hitbox[0] + paddle_AI.hitbox[2]:
                    ball.x -= 7
                    ball.collision()

        paddle_player.move()
        ball.move()
        if game_over:
            ball.speed = 15
            ball = Ball(WIDTH // 2, HEIGHT // 2)
            if replay_winner:
                paddle_player = PaddlePlayer(WIDTH - (PADDLE.get_width() * 2),
                                             (HEIGHT // 2) - (PADDLE.get_height() // 2))
                paddle_AI = PaddleAI(WIDTH - (PADDLE.get_width() * 2), (HEIGHT // 2) - (PADDLE.get_height() // 2))
                paddle.y = HEIGHT // 2
        # if not replay_winner:
        #     if AI_score > 100:
        #         break

        game_over = False
        draw_window(sc, paddle_player, paddle_AI, ball, paddles)
        if player_score == 1000000000000:  # 1111111111111111111111111 (10 or 100000000)
            time.sleep(1)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    exit()
                sc.fill((0, 0, 0))
                win = LARGE_FONT.render('YOU WIN', 1, WHITE)
                sc.blit(win, (70, HEIGHT // 2 - 100))
                pygame.display.update()

        if AI_score == 10000000000000:  # 1111111111111111111111111 (10 or 100000000)
            time.sleep(1)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    exit()
                sc.fill((0, 0, 0))
                lose = LARGE_FONT.render('YOU LOSE', 1, WHITE)
                sc.blit(lose, (30, HEIGHT // 2 - 100))
                pygame.display.update()


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    try:
        def replay_genome(genome_path="winner.pkl"):
            global replay_winner
            replay_winner = True
            # unpickle saved winner
            with open(genome_path, "rb") as f:
                genome = pickle.load(f)

            # convert loaded genome into required data structure
            genomes = [(1, genome)]

            # call game with only the loaded genome
            main(genomes, config)

        while True:
            replay_genome()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                exit()

    except:
        global replay_winner
        if replay_winner:
            exit()
        # population
        p = neat.Population(config)

        # printed statistics of each gen
        p.add_reporter(neat.StdOutReporter(True))
        p.add_reporter(neat.StatisticsReporter())

        winner = p.run(main, 30)
        with open("testing.pkl", "wb") as f:
            pickle.dump(winner, f)
            f.close()


if __name__ == '__main__':
    # we have the path set up so that it can be ran from anywhere in the computer and not only in the same directory
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
