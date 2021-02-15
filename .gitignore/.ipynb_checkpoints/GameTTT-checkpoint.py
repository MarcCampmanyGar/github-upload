{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What size game of tic tac toe?  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  0  1  2\n",
      "0 \n",
      "1 \n",
      "2 \n",
      "Current player: 1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What column do you want to play? (0, 1 or 2):  1\n",
      "What row do you want to play? (0, 1 or 2):  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  0  1  2\n",
      "0 \n",
      "1 \n",
      "2 \n",
      "Current player: 2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What column do you want to play? (0, 1 or 2):  2\n",
      "What row do you want to play? (0, 1 or 2):  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  0  1  2\n",
      "0 \n",
      "1 \n",
      "2 \n",
      "Current player: 1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What column do you want to play? (0, 1 or 2):  1\n",
      "What row do you want to play? (0, 1 or 2):  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  0  1  2\n",
      "0 \n",
      "1 \n",
      "2 \n",
      "Current player: 2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What column do you want to play? (0, 1 or 2):  01\n",
      "What row do you want to play? (0, 1 or 2):  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  0  1  2\n",
      "0 \n",
      "1 \n",
      "2 \n",
      "Current player: 1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What column do you want to play? (0, 1 or 2):  1\n",
      "What row do you want to play? (0, 1 or 2):  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "position ocuppied already, try again\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What column do you want to play? (0, 1 or 2):  1\n",
      "What row do you want to play? (0, 1 or 2):  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "position ocuppied already, try again\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What column do you want to play? (0, 1 or 2):  2\n",
      "What row do you want to play? (0, 1 or 2):  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: make sure  you input column/row as 0, 1 or 2 list index out of range\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What column do you want to play? (0, 1 or 2):  1\n",
      "What row do you want to play? (0, 1 or 2):  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "position ocuppied already, try again\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What column do you want to play? (0, 1 or 2):  2\n",
      "What row do you want to play? (0, 1 or 2):  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  0  1  2\n",
      "0 \n",
      "1 \n",
      "2 \n",
      "Current player: 2\n"
     ]
    }
   ],
   "source": [
    "import itertools\n",
    "from colorama import Fore,  Back,  Style, init\n",
    "init()\n",
    "\n",
    "def win(current_game):\n",
    "    \n",
    "    def all_same(l):\n",
    "        if l.count(l[0]) == len(l) and l[0] != 0:\n",
    "            return True\n",
    "        else:\n",
    "            return False\n",
    "        \n",
    "    #horitzontal\n",
    "    for row in game:\n",
    "        if all_same(row):\n",
    "            print (f\"Player {row[0]} is the winner horizontally (-)!\")\n",
    "            return True\n",
    "\n",
    "    #vertical\n",
    "    for col in range(len(game)):\n",
    "        check = []\n",
    "        for row in  game:\n",
    "            check.append(row[col])\n",
    "        if all_same(check):\n",
    "            print (f\"Player {check[0]} is the winner vertically (|)!\")\n",
    "            return True\n",
    "\n",
    "    #Diagonal\n",
    "    diags = []\n",
    "    for col, row in enumerate(reversed(range(len(game)))):\n",
    "        diags.append(game[row][col])\n",
    "    if all_same(diags):\n",
    "        print (f\"Player {diags[0]} is the winner diagonally (/)!\")\n",
    "        return True\n",
    "\n",
    "    diags = []\n",
    "    for ix in range(len(game)):\n",
    "        diags.append(game[ix][ix])\n",
    "    if all_same(diags):\n",
    "        print (f\"Player {diags[0]} is the winner diagonally (\\\\)!\")    \n",
    "        return True\n",
    "    \n",
    "    return False\n",
    "            \n",
    "def game_board(game_map, player=0, row=0, column=0, just_display=False):\n",
    "    try:\n",
    "        if game_map[row][column] != 0:\n",
    "            print(\"position ocuppied already, try again\")\n",
    "            return game_map, False\n",
    "        print(\"  \"+\"  \".join([str(i) for i in range(len(game_map))]))\n",
    "        if not just_display:\n",
    "            game_map[row][column] = player\n",
    "            \n",
    "        for count,row in enumerate(game_map):\n",
    "            #print(count,row)\n",
    "            colored_row = \"\"\n",
    "            for item in row:\n",
    "                if item == \"0\":\n",
    "                    colored_row += \"   \"\n",
    "                elif item == \"1\":\n",
    "                    colored_row += Fore.GREEN + \" X \" + Style.RESET_ALL\n",
    "                elif item == \"2\":\n",
    "                    colored_row += Fore.MAGENTA + \" O \" + Style.RESET_ALL\n",
    "            print(count, colored_row)\n",
    "                    \n",
    "            \n",
    "        return game_map, True\n",
    "    \n",
    "    except IndexError as e:\n",
    "        print ( \"Error: make sure  you input column/row as 0, 1 or 2\", e)\n",
    "        return game_map, False\n",
    "    \n",
    "    except Exception as e:\n",
    "        print(\"Something went terribly wrong\", e)\n",
    "        return game_map, False\n",
    "        \n",
    "play = True\n",
    "players =  [1, 2]\n",
    "while play:\n",
    "    game_size = int(input(\"What size game of tic tac toe? \"))\n",
    "    game = [[0 for i in range(game_size)] for i in range(game_size)]\n",
    "        \n",
    "    game_won = False\n",
    "    game, _ = game_board(game, just_display=True)\n",
    "    player_choice = itertools.cycle([1,2])\n",
    "    while not game_won:\n",
    "        current_player = next(player_choice)\n",
    "        print (f\"Current player: {current_player}\")\n",
    "        played = False\n",
    "        \n",
    "        while not played:\n",
    "            column_choice = int(input(\"What column do you want to play? (0, 1 or 2): \"))\n",
    "            row_choice = int(input(\"What row do you want to play? (0, 1 or 2): \"))\n",
    "            game, played = game_board(game, current_player, row_choice, column_choice)\n",
    "            \n",
    "        if win(game):\n",
    "            game_won =  True\n",
    "            again = input(\"Game is over. Would you like to play again? (y/n): \")\n",
    "            if again.lower() == \"y\":\n",
    "                print(\"Restarting\")\n",
    "            elif again.lower() == \"n\":\n",
    "                print(\"Byeee\")\n",
    "                play = False\n",
    "            else:\n",
    "                print(\"not a valid answer\")\n",
    "                play = False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
