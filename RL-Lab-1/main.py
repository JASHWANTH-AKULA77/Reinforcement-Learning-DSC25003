# This script just runs a few games using the environment we built in tictactoe_env.py
# so we can see the RL loop happening (state, action, reward, next state)
import random
from tictactoe_env import TicTacToeEnv


def random_policy(valid_moves):
    # just pick a random valid move
    return random.choice(valid_moves)


def simple_policy(board, valid_moves):
    # basic strategy: win if you can, else block opponent, else take
    # the middle, else just go random
    # (this is roughly the rule mentioned in the class notes)

    lines = TicTacToeEnv.win_lines

    def find_winning_spot(player):
        for (a, b, c) in lines:
            vals = [board[a], board[b], board[c]]
            cells = [a, b, c]
            if vals.count(player) == 2 and vals.count(0) == 1:
                return cells[vals.index(0)]
        return None

    # try to win
    spot = find_winning_spot(1)
    if spot is not None:
        return spot

    # try to block opponent
    spot = find_winning_spot(-1)
    if spot is not None:
        return spot

    # take center
    if 4 in valid_moves:
        return 4

    return random.choice(valid_moves)


def guess_state_value(board):
    # just a rough made-up score to show what "value function" means
    # not learned, just counting near-wins / near-losses
    score = 0
    for (a, b, c) in TicTacToeEnv.win_lines:
        vals = [board[a], board[b], board[c]]
        if vals.count(1) == 2 and vals.count(0) == 1:
            score += 5
        elif vals.count(-1) == 2 and vals.count(0) == 1:
            score -= 5
    return score


def play_one_game(env, game_num, gamma=0.9):
    print("=" * 50)
    print("GAME", game_num)
    print("=" * 50)

    state = env.reset()
    env.render()

    step_num = 0
    reward_list = []

    while True:
        moves = env.get_valid_actions()

        if env.turn == 1:
            action = simple_policy(state, moves)
            who = "Agent (X)"
        else:
            action = random_policy(moves)
            who = "Opponent (O)"

        state, reward, done, info = env.step(action)
        step_num += 1
        reward_list.append(reward)

        print("Step", step_num, "-", who, "played cell", action)
        print("reward:", reward, " done:", done, " info:", info)
        env.render()

        if done:
            break

    # calculate discounted return, just to show what gamma does
    total = 0
    for i in range(len(reward_list)):
        total += (gamma ** i) * reward_list[i]

    print("Game", game_num, "finished")
    print("rewards during game:", reward_list)
    print("discounted return (gamma=" + str(gamma) + "):", round(total, 4))
    print("rough value of final board:", guess_state_value(state))
    print("result:", info.get("result"))
    print()


def main():
    num_games = 3
    gamma = 0.9

    env = TicTacToeEnv()

    for g in range(1, num_games + 1):
        play_one_game(env, g, gamma)


if __name__ == "__main__":
    main()
