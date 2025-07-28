"""
Base attacked by aliens

1D linear base of given length is attacked by aliens
Their attack destroys a segment of length 1: [start, start+1]
Write the attack and is_game_over functions
Make them both work in O(1)
"""

import math

class Base:
    def __init__(self, base_length:int):
        assert type(base_length) == int
        self.base_length = base_length
        self.safe = [[x, x+1] for x in range(base_length)]
        self.remaining_length = base_length
        print(self.remaining_length, self.safe)

    def attack(self, start:float):
        """Aliens attack the base at location 'start' and destroy all the way to 'start'+1 """
        if start < 0 or start >= self.base_length:
            return
        idx = math.floor(start) # index of the segment where the attack starts

        # move the end of the first segment
        m = min(self.safe[idx][1], start)
        self.remaining_length -= self.safe[idx][1] - m # remove the length of the base destroyed
        self.safe[idx][1] = m

        # move the beginning of the next segment
        if idx < self.base_length-1:
            m = max(self.safe[idx+1][0], start+1)
            self.remaining_length -= m - self.safe[idx+1][0]
            self.safe[idx+1][0] = m
        print(f"After attack at {start}  ", self.remaining_length, self.safe)

    def is_game_over(self) -> bool:
        return self.remaining_length <= 0
    

b = Base(3)
b.attack(0)
b.attack(1)
assert not b.is_game_over()
b.attack(2)
assert b.is_game_over()

b = Base(3)
b.attack(-0.5)
b.attack(0.5)
b.attack(2.5)
b.attack(2.4)


        