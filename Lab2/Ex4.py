import numpy as np

def compose(musicalNotes, Moves, Start):
    print(musicalNotes[Start], end=" "),
    for move in Moves:
        print(musicalNotes[(Start + move) % musicalNotes.size], end=" ")
        Start = Start + move
    print(end="\n\n")


musicalNotes = np.array(["do", "re", "mi", "fa", "sol"])
compose(musicalNotes, [1, -3, 4, 2], 2)