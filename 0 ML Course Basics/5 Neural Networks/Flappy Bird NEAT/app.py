import pygame
import neat
import pickle
import os
import random

# images and fonts
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load('imgs/bird1.png')),
             pygame.transform.scale2x(pygame.image.load('imgs/bird2.png')),
             pygame.transform.scale2x(pygame.image.load('imgs/bird3.png'))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load('imgs/pipe.png'))
BASE_IMG = pygame.transform.scale2x(pygame.image.load('imgs/base.png'))
BG_IMG = pygame.transform.scale2x(pygame.image.load('imgs/bg.png'))

pygame.font.init()
STAT_FONT = pygame.font.SysFont('comicsans', 50)

# screen size
WIDTH = 500
HEIGHT = 800

# neural network global variables
gen = 0
replay_winner = False

# music
pygame.mixer.init()
pygame.mixer.music.load('theme.mp3')
pygame.mixer.music.play(-1)


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROT = 25
    ROT_VEL = 20
    ANIM_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        # calculate velocity after each tick. Will move up until the output becomes positive and then it moves down
        # the pattern continues until it becomes positive and starts falling
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2
        # this prevents the velocity from going too down too quickly
        if d >= 16:
            d = 16
        # if we are moving up, move up a bit more for it to be a bit more smooth
        if d < 0:
            d -= 2

        # changes y pos depending on displacement
        self.y = self.y + d

        # if we are moving up or we are above the position that we jumped from
        if d < 0 or self.y < self.height + 50:
            # if we are going up and are not tilted then tilt 25 degrees
            if self.tilt < self.MAX_ROT:
                self.tilt = self.MAX_ROT
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    # animation
    def draw(self, sc):
        self.img_count += 1

        if self.img_count < self.ANIM_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIM_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIM_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIM_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIM_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # this is so when it dives it doesn't flap
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIM_TIME * 2

        blitRotateCenter(sc, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


def blitRotateCenter(sc, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    sc.blit(rotated_image, new_rect.topleft)


class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, sc):
        sc.blit(self.PIPE_TOP, (self.x, self.top))
        sc.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    # mask (the collision mechanism we are using, figures out which pixels in a box are actually relevant because
    # by default, all the ones in the background are transparent because they are not what we have put the box around
    # it then takes a list of these pixels top to bottom and checks if the list of relevant pixels collide
    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True

        return False


class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, sc):
        sc.blit(self.IMG, (self.x1, self.y))
        sc.blit(self.IMG, (self.x2, self.y))


def draw_window(sc, birds, pipes, base, score, gen):
    clock = pygame.time.Clock()
    sc.blit(BG_IMG, (0, 0))
    for pipe in pipes:
        pipe.draw(sc)
    if replay_winner:
        text = STAT_FONT.render(str(score), 1, (255, 255, 255))
        sc.blit(text, (WIDTH - 10 - text.get_width(), 10))
    else:
        text = STAT_FONT.render('Score ' + str(score), 1, (255, 255, 255))
        sc.blit(text, (WIDTH - 10 - text.get_width(), 10))

        text = STAT_FONT.render('Gen ' + str(gen), 1, (255, 255, 255))
        sc.blit(text, (10, 10))

    base.draw(sc)
    for bird in birds:
        bird.draw(sc)
    pygame.display.update()
    clock.tick(30)


def main(genomes, config):
    global gen
    gen += 1
    nets = []
    ge = []
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)

    base = Base(730)
    pipes = [Pipe(600)]
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        pipe_ind = 0
        if len(birds) > 0:
            # if we have passed a pipe then change the pipe we are looking at to the one in front
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            break

        for x, bird in enumerate(birds):
            bird.move()
            # encourages bird to stay alive
            ge[x].fitness += 0.1

            # looks at the distance between the bird x, y and pipe x,y and then determines whether it should jump
            # if it is close the the pipe
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].
                                                                                         bottom)))
            if output[0] > 0.5:
                bird.jump()

        # bird.move()
        add_pipe = False
        remove = []
        base.move()
        for pipe in pipes:
            for x, bird in enumerate(birds):
                # this encourages it to go between the pipe because if it doesn't then its fitness will go down
                if pipe.collide(bird):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                # if the bird's x coordinate goes past the pipes x coordinate add another pipe to the pipe list
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove.append(pipe)
            pipe.move()

        if add_pipe:
            score += 1
            # increases their fitness if they go through the pipe
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(600))

        for r in remove:
            pipes.remove(r)

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        if score > 50 and not replay_winner:
            break

        draw_window(sc, birds, pipes, base, score, gen)


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    try:
        h
        def replay_genome(config_path, genome_path="winner.pkl"):
            global replay_winner
            replay_winner = True
            # Unpickle saved winner
            with open(genome_path, "rb") as f:
                genome = pickle.load(f)

            # Convert loaded genome into required data structure
            genomes = [(1, genome)]

            # Call game with only the loaded genome
            main(genomes, config)

        while True:
            replay_genome(config_path)
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

        # 50 generations max, calls main function and runs it 50 times
        winner = p.run(main, 50)
        with open("winner.pkl", "wb") as f:
            pickle.dump(winner, f)
            f.close()


if __name__ == '__main__':
    # we have the path set up so that it can be ran from anywhere in the computer and not only in the same directory
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
