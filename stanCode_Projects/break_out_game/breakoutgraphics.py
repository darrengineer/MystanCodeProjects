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

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball

SWITCH_ON = False


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing  # self. => added by me
        self.window_height = brick_offset + 3 * (
                brick_rows * (brick_height + brick_spacing) - brick_spacing)  # self. => added by me
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)  # self. => added by me

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(self.window_width - paddle_width) / 2,
                        y=(self.window_height - paddle_height) - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        # self.window.add(self.ball, x=self.window_width / 2 - ball_radius, y=self.window_height / 2 - ball_radius)
        self.create_ball()

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.ball_move)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=(brick_width + brick_spacing) * i,
                              y=(brick_height + brick_spacing) * j)
                brick.filled = True
                if j == 0 or j == 1:
                    brick.fill_color = 'red'
                if j == 2 or j == 3:
                    brick.fill_color = 'orange'
                if j == 4 or j == 5:
                    brick.fill_color = 'yellow'
                if j == 6 or j == 7:
                    brick.fill_color = 'green'
                if j == 8 or j == 9:
                    brick.fill_color = 'blue'
                self.window.add(brick)

    def create_ball(self, ball_radius=BALL_RADIUS):
        self.window.add(self.ball, x=self.window_width / 2 - ball_radius, y=self.window_height / 2 - ball_radius)

    def paddle_move(self, mouse, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET):
        if paddle_width / 2 < mouse.x < self.window_width - paddle_width / 2:
            self.paddle.y = (self.window_height - paddle_height) - paddle_offset
            self.paddle.x = mouse.x - paddle_width / 2
            self.window.add(self.paddle)

    def ball_move(self, event):
        self.set_ball_velocity()

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_ball_x_velocity(self):
        return self.__dx

    def get_ball_y_velocity(self):
        return self.__dy
