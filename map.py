from main_block import *
import border_block, crate, random
class Map:

    def __init__(self):
        self.blocks = []
        self.make_map()


    def update(self, objects):
        for b in self.blocks:
            b.update(objects)

    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)


    def make_map(self):
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1 or (c % 2 == 0 and r % 2 == 0):
                    self.blocks.append(border_block.Border_block(c * BLOCK_SIZE, r * BLOCK_SIZE))
                    self.blocks.append(border_block.Border_block(c * BLOCK_SIZE, r * BLOCK_SIZE))

        ammount = random.randint(round((ROWS * COLS) * 0.50), round((ROWS * COLS) * 0.60))
        print(ammount)

        while ammount > 0:
            x = random.randint(0, COLS)
            y = random.randint(0, ROWS)

            if (x % 2 != 0 or y % 2 != 0) and x != 0 and x != COLS - 1 and y != 0 and y != ROWS -1:
                self.blocks.append(crate.Crate(x * BLOCK_SIZE, y * BLOCK_SIZE))
                ammount += -1
