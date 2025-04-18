# togyz-qumalaq-agent

Source Python code for the paper *Applying Self-Play Reinforcement Learning to Kazakh National Board Games: A Case Study on Togyzkumalak*

**Author**: Dinara Zhussupova

Source code for training an agent to play the game Togyzkumalak https://en.wikipedia.org/wiki/Toguz_korgol


## Rules of the game in Kazakh
Youtube videos - 
1. https://www.youtube.com/watch?v=IwD_8vqU2k0&t=205s
2. https://www.youtube.com/watch?v=BqThWE5PClw
3. https://www.youtube.com/watch?v=2tTcwhZA5m8
4. https://www.youtube.com/watch?v=tFbVBoPihP0
5. https://www.youtube.com/watch?v=KdJAIrOl1Qk
6. https://www.youtube.com/watch?v=N81DI7ASCaU
7. https://www.youtube.com/watch?v=aOy0pQj2F80
8. https://www.youtube.com/watch?v=0uGeorKId8I
9. https://www.youtube.com/watch?v=F7hoRafIzu4
10. https://www.youtube.com/watch?v=rMG9OQGqZoA
11. https://www.youtube.com/watch?v=O0hTAWevNco
12. https://www.youtube.com/watch?v=_eHs1UHVwMA
13. https://www.youtube.com/watch?v=k2DdvZ-9Fdk
14. https://www.youtube.com/watch?v=794pbqS_xCk
15. https://www.youtube.com/watch?v=569eH-2m-mw
16. https://www.youtube.com/watch?v=CALCK1HkflQ
17. https://www.youtube.com/watch?v=JImCVuuabJg
18. https://www.youtube.com/watch?v=JmPVm3d5BH4
19. https://www.youtube.com/watch?v=itcJGCira1g
20. https://www.youtube.com/watch?v=MT-00UMozTA
21. https://www.youtube.com/watch?v=K268_4llf78
22. https://www.youtube.com/watch?v=1IWfghT-3HQ
23. https://www.youtube.com/watch?v=JvyOozHjxII

## Game apps
- https://www.iggamecenter.com/ru/info/maintoguz - 2 players
- https://www.playok.com/ru/togyzkumalak/ - 2 players
- https://play.google.com/store/apps/details?id=kz.enu&hl=kk - 1,2 players

## Environment 
PettingZoo https://pettingzoo.farama.org/

## Running guide
Python version >= 3.11

Create virtual env
```
python -m venv 9qumalaq
```

Activate virtual env
```
source 9qumalaq/bin/activate
```

Install packages
```
pip install -r requirements.txt
```
## Self-play training (DQN)

Tianshou https://tianshou.org/en/stable/index.html#

### Recording some frames: playing two trained DQN agents

![Alt Text](https://github.com/zhus-dika/togyz-qumalaq-agent/blob/main/data/6vs5.gif)

(spoiler: Qostaushy will win :monkey:)

### Run web app - play as Bastaushy with the DQN agent

```
python app/app.py
```

## Self-play training (MCTS Alpha Zero)

https://github.com/suragnair/alpha-zero-general

### Implementation game board for MCTS

The board for the game is implemented as in the Figure below

<img src="https://github.com/zhus-dika/togyz-qumalaq-agent/blob/main/data/9qumalaq_init_board_mcts.png" alt="drawing" width="450"/>

When Tuzdyk is captured, the cell is marked with a symbol representing the corresponding player. For example, in Figure below

<img src="https://github.com/zhus-dika/togyz-qumalaq-agent/blob/main/data/9qumalaq_tuzdyk_board_mcts.png" alt="drawing" width="450"/>

### Run tests for the environment

```
python model_based_approach/tests/test_env.py

python model_based_approach/tests/test_natural_env.py
```

### Run the game with random players for testing asserts in main codes

```
python model_based_approach/tests/test_game.py
```

### Train agents

```
python model_based_approach/main.py
```

### Play vs trained MCTS agent

```
python model_based_approach/pit.py
```
## Experiments

https://docs.google.com/spreadsheets/d/12MiySvyxko9UPw_rFsr3w9lILuD7jYY2vgqoScxDRZQ/edit?usp=sharing
