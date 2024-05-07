# togyz-qumalaq-agent

**Title**: *Applications of Curriculum Learning and Self-Play of Reinforcement Learning Techniques for Competitive Environments in Kazakh National Games*

**Author**: Dinara Zhussupova

**Scientific mentor**: Elena Kantonistova

Training an agent to play the game Togyzqumalaq https://en.wikipedia.org/wiki/Toguz_korgol


## Plan

|# | Point                                        | Date                  | Description                                                                                                        | Results                                  |
|--|----------------------------------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------|
|1 | Exploring a library to create an environment | 01/04/2024-05/04/2024 | Learn how to write PettingZoo AEC type env https://pettingzoo.farama.org/api/aec/#about-aec                        | Jupyter notebook                         |
|2 | Learning the game, rules and strategies      | 06/04/2024-10/04/2024 | Writing a multi-agent environment for the game                                                                     | Jupyter notebook                         |
|3 | Exploring a library to train agents          | 11/04/2024-15/04/2024 | Learn about training agents for multi-agent environment https://tianshou.org/en/stable/01_tutorials/04_tictactoe.html | Jupyter notebook                         |
|4 | Train agents                                 | 16/04/2024-21/04/2024 | Train DQN agents to play the game                                                                                  | Jupyter notebook, policy models of agents|
|5 | Implement web app to play with humans        | 22/04/2024-15/05/2024 | Write web service via Flask framework                                                                              | Docker container                         |


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

## Self-play training

Tianshou https://tianshou.org/en/stable/index.html#

## Recording some frames: playing two trained DQN agents

Recording some frames: playing two trained DQN agents https://drive.google.com/file/d/1hcGc5CWTM308dK3-yl4sixhslXmm31ZR/view?usp=drive_link (spoiler: Bastaushy will win :monkey:)

Recording a game with a stronger agent *models/policy_dqn_256x512x512x256_2.pth* https://drive.google.com/file/d/1Aw_BRzBt-32vHekFi-mt6ZptQclQy9GR/view?usp=sharing

## Running guide
Python version >= 3.11

```
pip install -r requirements.txt
```

```
python app/app.py
```

