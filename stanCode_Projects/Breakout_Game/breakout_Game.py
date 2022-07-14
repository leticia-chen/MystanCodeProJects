"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    """
    This is a breakout bricks game, player has three times to win the game.
    """
    breakout = BreakoutGraphics()

    # Can play 3 times, use counter: count
    count = 0
    while count < NUM_LIVES:
        pause(FRAME_RATE)
        if breakout.total_bricks == 0:                          # If breakout all bricks, you win
            break
        # Start to play game
        if breakout.start_game:
            breakout.ball.move(breakout.get_dx(), breakout.get_dy())

            # Paddle did not catch ball
            if breakout.ball.y + breakout.ball.height >= breakout.window.height:
                count += 1
                breakout.start_game = False                      # one run overed
                breakout.reset_ball()

            # The ball run to hit left, right or top edge
            if breakout.ball.x <= 0 or breakout.ball.x+breakout.ball.width >= breakout.window.width:
                breakout.set_dx()
            if breakout.ball.y <= 0:
                breakout.set_dy()

            breakout.remove_bricks()

    # If you win, will be crowned
    if breakout.score >= 60:
        breakout.winner()


if __name__ == '__main__':
    main()
