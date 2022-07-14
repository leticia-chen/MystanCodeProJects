"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.graphics.gimage import GImage
from campy.gui.events.timer import pause

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 5    # Initial vertical speed for the ball
MAX_X_SPEED = 3        # Maximum initial horizontal speed for the ball
DELAY = 150
DELAY1 = 10
SPEED_UP = 0.3


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width)/2, y=self.window.height-paddle_offset-self.paddle.height)

        # Create the ball
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        self.total_bricks = 0
        self.max_bricks = 0

        # create 100 bricks
        for i in range(brick_rows):                                         # In rows count
            brick_y = brick_offset + (brick_height + brick_spacing) * i     # y coordinate, from top to bottom
            # color = 'red'
            if i <= 1:                                                      # The first 2 rows - top
                color = 'firebrick'
            elif i <= 3:                                                    # The 3,4 rows
                color = 'tomato'
            elif i <= 5:                                                    # The 5.6 rows
                color = 'orange'
            elif i <= 7:                                                    # The 7,8 rows
                color = 'seagreen'
            else:                                                           # The 9,10 rows
                color = 'cadetblue'
            for j in range(brick_cols):                                     # In columns count
                brick_x = (brick_width + brick_spacing) * j                 # x coordinate, from left to right side
                self.brick = GRect(brick_width, brick_height)               # give each brick size
                self.brick.filled = True
                self.brick.fill_color = color
                self.brick.color = color
                self.window.add(self.brick, x=brick_x, y=brick_y)
                self.total_bricks += 1
            if self.max_bricks <= self.total_bricks:
                self.max_bricks = self.total_bricks

        # Give initial velocity to ball before default value, they are strict private
        self.__dx = 0
        self.__dy = 0

        # To reset ball position and direction before start game
        self.reset_ball()
        self.set_ball_velocity()

        self.start_game = False                                 # Switch to start game
        onmouseclicked(self.start)                              # Click mouse to start game
        onmousemoved(self.move_paddle)                          # To move paddle by mouse

        self.score = 0                                          # To show score information
        self.score_label = GLabel('Score = ' + str(self.score))
        self.score_label.font = '-15'
        self.window.add(self.score_label, x=0, y=self.window.height)

    def remove_bricks(self):
        """
        While ball hit brick, brick will be removed, there are 4 points of ball to determine hitting
        This is Methods function
        """
        # If ball hit on the score label, score label will not be removed
        for b_x in range(int(self.ball.x), int(self.ball.x+self.ball.width+1), self.ball.width):    # (start, end, step)
            for b_y in range(int(self.ball.y), int(self.ball.y+self.ball.height+1), self.ball.height):
                maybe_bricks = self.window.get_object_at(b_x, b_y)                            # May hit object on 4 points
                if maybe_bricks is not None and maybe_bricks is not self.score_label:
                    if maybe_bricks is self.paddle:                                           # Ball hit paddle
                        if self.__dy > 0:                                                     # Ball rebound to up
                            self.__dy = -self.__dy                                            # Ball keep moving to up

                    else:
                        self.window.remove(maybe_bricks)                                      # Hitting on brick and be removed
                        self.__dy = -self.__dy
                        self.total_bricks -= 1
                        self.score += 1
                        self.score_label.text = 'Score = ' + str(self.score)
                        self.__dy += SPEED_UP
                        self.__dx += SPEED_UP

    def reset_ball(self):
        """
        Before start game, have to reset ball position, initial direction
        Methods function
        """
        self.set_ball_position()
        self.window.add(self.ball)

    def move_paddle(self, mouse):
        """
        Move paddle´s direction with mouse moving, moving only horizonte
        param (event): MouseEvent
        """
        self.paddle.x = mouse.x                                     # Mouse move = paddle move, only left and right
        if self.paddle.x <= 0:                                      # Paddle cannot surpass window left side
            self.paddle.x = 0
        if self.paddle.x+self.paddle.width >=\
                self.window.width:                                  # Paddle cannot surpass window right side
            self.paddle.x = self.window.width-self.paddle.width

    def set_ball_position(self):
        """
        To set ball position by random before game starts
        x coordinate: inside of window, left and right side
        y coordinate: below all bricks and upon paddle
        """
        self.ball.x = random.randint(0, self.window.width-self.ball.width)
        self.ball.y = random.randint(BRICK_OFFSET+(BRICK_HEIGHT+BRICK_SPACING)*BRICK_ROWS-BRICK_SPACING,
                                     self.window.height-PADDLE_OFFSET-PADDLE_HEIGHT-self.ball.height)

    def set_ball_velocity(self):
        """
        To set ball velocity by random before game starts
        """
        self.__dx = random.randint(3, MAX_X_SPEED)
        self.__dy = random.randint(INITIAL_Y_SPEED, 7)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def reset_velocity(self):
        """

        """
        self.__dx += SPEED_UP
        self.__dy += SPEED_UP

    def get_dx(self):
        """
        Horizonte speed getter, for user can use it
        """
        return self.__dx

    def get_dy(self):
        """
        Vertical speed getter, for user can use it
        """
        return self.__dy

    def set_dx(self):
        """
        Horizonte speed setter, for user can change its direction
        """
        self.__dx = -self.__dx

    def set_dy(self):
        """
        Vertical speed setter, for user can change its direction
        """
        self.__dy = -self.__dy

    # Switch to start game
    def start(self, mouse):
        """
        This is like a switch to start game when clicks mouse
        param mouse: MouseEvents
        """
        self.start_game = True

    def winner(self):
        """
        While game over, if score is more than 60, player win the game, will be crowned
        """
        self.window.remove(self.brick)          # remove remaining bricks
        self.window.remove(self.paddle)         # remove paddle
        self.window.remove(self.ball)           # remove ball

        background = GRect(self.window.width, self.window.height-self.score_label.height-10)
        background.color = 'white'
        background.filled = True
        background.fill_color = 'white'
        self.window.add(background)

        face = GImage('happy.png')
        self.window.add(face, x=(self.window.width-face.width)/2,
                        y=(self.window.height-PADDLE_OFFSET-self.paddle.height-face.height)/2)
        crown = GImage('crown1.png')
        self.window.add(crown, x=(self.window.width-crown.width)/2, y=5)

        # Crown will be added, from top of window to top of face
        vx = 0
        for i in range(0, 14, 1):
            vy = i
            pause(DELAY)
            crown.move(vx, vy)

        rect = GRect(self.window.width, 84)
        rect.color = 'purple'
        rect.filled = True
        rect.fill_color = 'purple'
        self.window.add(rect, x=(self.window.width - rect.width) / 2,
                        y=(self.window.height - (face.y + face.height)) * 2)

        you_win = GImage('you win1.JPG')
        self.window.add(you_win, x=0, y=(self.window.height-(face.y+face.height))*2)

        # Will show YOU WIN news ticker below face area
        vy = 0
        vx = 3
        count = 0
        while count < 10:
            if you_win.x > self.window.width:
                self.window.add(you_win, x=0, y=(self.window.height-(face.y+face.height))*2)
                count += 1
            you_win.move(vx, vy)
            pause(DELAY1)
        self.window.add(you_win, x=(self.window.width-you_win.width)/2, y=(self.window.height - (face.y + face.height)) * 2)






