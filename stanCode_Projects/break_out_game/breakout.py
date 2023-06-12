"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE

unsolved problems:
1. 超出底部邊界時，等待下一次點擊開始
2. 遊戲終止條件: 消滅所有磚塊
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 50  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    vx = graphics.get_ball_x_velocity()
    vy = graphics.get_ball_y_velocity()
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        # when ball is static (initial position)
        if vx == 0 and vy == 0:
            # get velocity
            vx = graphics.get_ball_x_velocity()
            vy = graphics.get_ball_y_velocity()
            print(vx, vy)
        graphics.ball.move(vx, vy)

        # set up boundaries
        if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
            vx = - vx
        if graphics.ball.y + graphics.ball.height > graphics.window.height:
            lives -= 1
            if lives != 0:
                graphics.create_ball()
            else:
                return

        # set up the 4 neighbor coordinates of the ball
        a = graphics.ball.x
        b = graphics.ball.y
        maybe_brick1 = graphics.window.get_object_at(a, b)
        maybe_brick2 = graphics.window.get_object_at(a, b + graphics.ball.height)
        maybe_brick3 = graphics.window.get_object_at(a + graphics.ball.width, b + graphics.ball.height)
        maybe_brick4 = graphics.window.get_object_at(a + graphics.ball.width, b)

        # collide on the top
        if maybe_brick1 and maybe_brick4 is not None:
            graphics.window.remove(maybe_brick1)
            graphics.window.remove(maybe_brick4)
            vy = - vy

        # collide at the bottom
        if maybe_brick2 and maybe_brick3 is not None:
            if b + graphics.ball.height <= graphics.window.height/2:
                graphics.window.remove(maybe_brick2)
                vy = - vy
            else:
                vy = - vy

        # collide at left side and right side
        if maybe_brick1 and maybe_brick2 is not None:
            graphics.window.remove(maybe_brick1)
            graphics.window.remove(maybe_brick2)
            vx = -vx
        if maybe_brick3 and maybe_brick4 is not None:
            graphics.window.remove(maybe_brick3)
            graphics.window.remove(maybe_brick4)
            vx = -vx


if __name__ == '__main__':
    main()
