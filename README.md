# HackNC 2023 Submission: Quame of Life
## Description
This is a game inspired by Conway's game of life, but using the time-dependent Schrodinger equation to simulate quantum dynamics. Players can choose between the sandbox mode, where they have unlimited squares and can build whatever shapes they want, and the challenge mode, where they can take on levels where they battle red quantum squares with blue quantum squares.
## Usage
Using python 3.12, run the MainMenu.py script, as it is the central script that connects everything else. Through the main menu, you can access the Sandbox mode, the Challenge mode, as well as change the grid size.

### Dependencies
The packages you will need to download in order to run this are as follows:

- numpy
- tkinter
- tkvideo

## Saving / Loading Configurations
The Sandbox mode gives you the ability to save and load configurations that you create. When you save a configuration, it saves the data for the blue squares, but when you load one, it loads them into the red squares, allowing you to create your own challenge levels, or take on challenge levels without the block limits.

### Notes
When loading, make sure the grid size for the file you're trying to load is the same as the grid size that you have set. Otherwise, it will distort the shapes and load incorrectly.
