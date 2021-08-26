# lockdown
<center>
![lockdown](https://github.com/trashvin/lockdown_game_witty/blob/main/docfiles/game_screen.png)
</center>

lockdown is a simple arcade game based on a popular retro game 'breakout'. this is an output from witty academy sessions for game app development using python and pygame. the topics and lessons can be found on this [link](https://trashvin.github.io/python-gamedev-2021/).

# the story

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

# the rules

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

# developer notes

## platform

python 3.8+ and pygame

## how to's

### how to add modify the level layout

- level layouts are located in src/assets/files/. the files are text files with the 'ldk' extension.
- the contents of the file is a matrix representing either a covid virus or a brick.
```
covid viruses
1 - alpha variant
2 - beta variant
3 - delta variant
4 - lamda variant

bricks
11 - regular brick
12 - power brick

level file content example
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
1,1,1,4,1,1,1,1,2,1,1,1,1,3,1
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
```

#### how to add a level

- to add a new level, create a level layout file and save it in src/assets/files/. use the following format for the filename :
  format : level_<level>.ldk
  e.g.   : level_1.ldk
- modify constants.py and set the value of MAX_LEVEL to the new level count.

