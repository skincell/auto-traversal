# auto-traversal


Update: This project is defunct. I found this solution shortly before I stopped working on it for an api design, which I should be using as a first step. https://github.com/SerpentAI/SerpentAI
Once I saw how mature this project was then I decided my project wasn't needed. But I won't really know until I try out their API for my use case. Thanks for coming in and looking at this project, but you should look at Serpent AI and read up and find the community which it spun off of for further research on your project. Thanks

## Description
Auto-movement which can be hopefully strapped to games.


## Installation
To set up the environment, all you need to do is run:
pip install -r requirements.txt

This requires that the user has a version of python with pip installed.


## Purpose
The purpose of this software is to add auto-traversal to games that do not already have it.

## My Personal Motivation
* Develop a software package that I can use for game development later on. (The idea is that I would include this as part of a game)
* Make boring parts of the game auto done
* Eventually would like to add an AI to a part of it.

## Brainstormed components to make this work
* Interface devices with game
* graph traversal component - This will be broken as we go along
* mapping of commands to interface and graph traversal component


# TODO look up feedback options -> visual and otherwise for games
## Feedback options (On hold == because we will make an assumption that user only gives commands that work for movement)
* visual feedback
- robotics libraries - AI libraries that do feedback perception
