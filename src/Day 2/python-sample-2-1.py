# import python
"""
Python boot camp day 2

This code is to give you an approximate idea of how a extremely basic python game could look like.
We will be using pygame for this. We will try to build a simple block collision game.

We need a player, and randomly occurring enemies which come at the player.

to run this file, you will first need to install pygame on your machine. this is quite simple.

On your computer open command prompt/ terminal. Once it opens up, please type
python3 -m pip install pygame

if this command does not work, please try
python -m pip install pygame

This should install pygame module on your machine for python to use.

Note: If both of these fail, there is some problem with your python installation. Please check our python-setup guide under the setup folder.
"""

# import pygame to use the display and other necessary functions to render and move the elements around.
import pygame

import random

# the max screen width in pixels
SCREEN_WIDTH = 1000
# the max screen height in pixels
SCREEN_HEIGHT = 600


class Enemy(pygame.sprite.Sprite):
    """
    This enemy class essentially represents a template of how an enemy should behave, move and be displayed like.
    """

    def __init__(self):
        # the following lines of code in this __init__ function basically tell pygame how the enemy should look like
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((50, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(50, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        # speed at which the enemy will move
        self.speed = random.randint(5, 10)

    def update(self):
        # this following statement tells pygame to move the enemy left by 5 units and not move it in any way on the y axis.
        self.rect.move_ip(-self.speed, 0)
        # this line checks if the enemy is past the game boundary. if yes, kill the enemy and remove it from the screen
        if self.rect.right < 0:
            self.kill()


class Player(pygame.sprite.Sprite):
    """
    This player class essentially represents a template of how the player should behave, move and be displayed like.
    """

    def __init__(self):
        # as we saw with the Enemy class, we define how a player should look like and where should it be displayed
        super(Player, self).__init__()
        self.surf = pygame.Surface((80, 30))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(50, 10)
        )

    def update(self, pressed_keys):
        # since the player moves based on user input, we write some code to move the player up and down when you press some keys
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)

        # as was with the enemy, we check if the player has reached the window boundary. if yes, we need to make sure that
        # the player stays inside of these boundaries. the following code keeps the player from going outside.
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# initialize the pygame module and check if it was done correctly.
pygame.init()
if pygame.get_init() == False:
    raise RuntimeError("pygame modules not initialized")

# Create a surface for our game. This actually creates the window and gives us a surface to put things on
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# we always have one player in the game.
player = Player()

# we define an empty collection of enemies. we will add some enemies to this later.
enemies = pygame.sprite.Group()

# we define a list of all the players and enemies we want to draw on the screen. we will add our player for now, and we will add
# all the enemies later
all_entities = pygame.sprite.Group()
all_entities.add(player)

# We need some way to add enemies to our game. We can do this in a number of ways, but for now, we can just add enemies
# at a fixed interval of every 0.5 seconds (500ms).
ADD_ENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY_EVENT, 500)

# set the game loop to run
running = True

while running:  # run the game

    # update the entire display with the latest positions of the objects on the screen
    pygame.display.update()

    # make the surface black
    display_surface.fill((0, 0, 0))

    # find what events have occurred while the game is running...
    # this is responsible for capturing events like game window closed, mouse clicks, button clicks etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADD_ENEMY_EVENT:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_entities.add(new_enemy)

    # draw all the entities on the screen
    for entity in all_entities:
        display_surface.blit(entity.surf, entity.rect)

    # get a list of keys pressed and update the player position accordinly
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # also update the enemies so they can be in motion
    enemies.update()

    # check if any of the enemies have collided with the player. if yes, stop and kill the game.
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False
