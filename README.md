# RL Lab 1 - Tic Tac Toe Environment

M.Tech Data Science - Reinforcement Learning Lab
Name: <Akula Jashwanth Kumar>
Roll No: <BL.SC.P2DSC25003>

## What this project is

This is Lab 1 for RL. The task was to build an RL **environment**
(not train an agent) using tic tac toe as example, since that's what
was used in class to explain the basic terms:

- Agent
- Environment
- State
- Action
- Reward
- Next State
- Policy
- Value Function
- Episode
- Discount factor

So this project just builds the tic tac toe game as an environment
that follows the usual step()/reset() style used in RL, and then
`main.py` runs a couple of demo games using simple hand written rules
(not actual learning) just so we can see the loop working.

## Files

- `tictactoe_env.py` - the environment itself (the board + game rules)
- `main.py` - runs some demo games and prints what's happening at each step
- `README.md` - this file
- `requirements.txt` - nothing extra needed, just python

## How the board works

Board is a list of 9 numbers:

```
0 1 2
3 4 5
6 7 8
```

- 0 = empty
- 1 = X (agent)
- -1 = O (opponent)

## Mapping to RL terms

| Term | In this project |
|---|---|
| Agent | player X, decided by `simple_policy()` |
| Environment | `TicTacToeEnv` class |
| State | `self.board` |
| Action | number 0-8, which cell to play |
| Reward | +1 win, -1 loss, 0 draw/ongoing, -10 for illegal move |
| Next state | board after `step()` runs |
| Policy | `simple_policy()` and `random_policy()` in main.py |
| Value function | `guess_state_value()` - just a made up score, not learned |
| Episode | one full game, reset() to done=True |
| Discount factor | `gamma` in main.py, used to calculate the return at the end |

## Reward table

| what happened | reward |
|---|---|
| agent wins | +1 |
| agent loses | -1 |
| draw | 0 |
| normal move, game not over | 0 |
| illegal move (cell already used) | -10 |

Reward is basically 0 the whole game until the last move, that's why
we calculate a "discounted return" at the end using gamma, to show
how a reward from the last step relates back to the earlier moves.

## Episode

One episode = one game. Starts from `reset()` (empty board) and ends
when `done = True`, which happens when:
- someone wins
- board is full (draw)
- someone tries an illegal move

## How to run

```
pip install -r requirements.txt
python main.py
```

It'll print 3 games, showing each step (who played where, reward,
whether game ended) plus a summary at the end of each game.

## Sample output

```
Step 1 - Agent (X) played cell 4
reward: 0  done: False  info: {'result': 'ongoing'}
- | - | -
---------
- | X | -
---------
- | - | -
...
Game 1 finished
rewards during game: [0, 0, 0, 0, 0, 0, 1]
discounted return (gamma=0.9): 0.5314
rough value of final board: 5
result: win
```

(numbers/moves change a bit each run since opponent moves randomly)

## Notes

- `guess_state_value()` is NOT a real learned value function, I just
  wrote a simple scoring rule to show what "value of a state" means.
  Real value functions get learned through algorithms like
  Q-learning which we'll probably do in a later lab.
- Didn't add extra files since the assignment is only about building
  the environment, not the agent/training part.
