# togyz-qumalaq-agent
Training an agent to play the game Togyzqumalaq

## Rules of the game
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

## Python Classes

### 0. State
Methods:
- `init()`
- `get_state()` -
  `return {
     #initial state
     "otaular": [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
     "tuzdyq": [-1, -1],
     "qazandar": [0, 0]
  }`

  list _"otaular"_: range(0 - 8) indexes - for _"bastauysh"_ player and range(9 - 17) indexes - for _"qostauysh"_ player

  list _"tuzdyq"_: 0 - index for _"bastauysh"_ player and 1 index - for _"qostauysh"_ player
  
  list _"qazandar"_: 0 - for _"bastauysh"_ player and 1 - for _"qostauysh"_ player

### 1. Environment
   Methods: 
   
- `init()`
- `reset()` - reset the game, i.e initial state of the environment 
- `step(current_state, action)` - return `(reward, new_state, new_action)`
- `render(current_state)` - plot the state of the environment
   
### 2. Policy

Methods: 

- `init()`
- `get_action(current_state)` - return `action`

### 3. Action
Methods: 
- `init()`
- `make_action(current_state, action)`
