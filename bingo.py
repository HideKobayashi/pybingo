import random

DEFAULT_NUM_BALLS = 75

class Bingo:
    def __init__(self, max_N = DEFAULT_NUM_BALLS):
        self.max_N = max_N
        self.balls = list(range(1, self.max_N + 1))
        self.out_balls = []
    
    def pop(self):
        print('ボールを取り出す')
        pick_num = random.randint(0, len(self.balls) - 1)
        out_ball = self.balls.pop(pick_num)
        self.out_balls.append(out_ball)
        return out_ball

    def show_status(self):
        print("中のボール", self.balls)
        print("外のボール", self.out_balls)

def run_bingo(num_balls = DEFAULT_NUM_BALLS):
    b = Bingo(num_balls)
    b.show_status()
    while True:
        choice = input("Enter を押してください。やめるなら 'q' を入力")
        if choice == 'q':
            break
        if len(b.balls) == 0:
            print("中が空になりました。")
            break
        b.pop()
        b.show_status()


if __name__ == "__main__":
    run_bingo(num_balls=5)
