# neopets-shapeshifter
Resources for solving Neopets' shapeshifter puzzles

```
(special thanks to divvy for replying to my email about kvho -I'm hosting
it here without permission just in case its lost to time)
.
├── kvho_ss
│   ├── myshape.pl
│   ├── readme.md
│   └── ss.c
└── README.md

1 directory, 4 files
```

Level notes:
https://www.jellyneo.net/?go=shapeshifter

```
At at the very least, an extra check that could perhaps save some time. I
need to put in a test to see how often the check would fire. Maybe it
never does… maybe it happens a lot.

 If you took the total area of all pieces and from that subtracted the
 difference of the initial board from the pristine board, you would have
 the product of the total number of “flips” — pieces that go past
 the goal piece back to the first piece and then eventually back to the
 goal piece again — times the depth of the board. So divinde by the
 depth to get the total number of flips.

So, the optimization, is to keep a running count of how many flips have
been performed. If a potential move would put it over the limit —
it’s a bad move and will not lead to a solvable board. Combined with
my original pruner (area of remaining pieces minus the difference of
the board must be greater than or equal to zero and a multiple of the
board depth), this may make the current generation of boards solvable
in a reasonable amount of time.

(This can be eyeballed by saying that N has to be the same or smaller
than its parent. That is easy and doesn’t require a new ‘C’ routine
or having to return a tuple from place()… omg… if this works… my
pen-and-paper test says it can… so exciting. But I’ve been excited
by duds before 😦 )

I can’t see how these puzzles could, realistically, ger much
harder. I’m beginning to think the top scorers are solving them by hand;
maybe they are just that intuitive.

-- shapeshifter 2007-05-30 at 18:40
```

# Performance Notes

| level | khvo speed | python speed |
|-------|------------|--------------|
| 26    |            |              |
| 27    | 880 us     | 17m 9s       |
| 28    |            |              |

# Blog posts:

- https://shummie.wordpress.com/2009/08/04/shapeshifting/
- https://shewhoshapes.wordpress.com/2007/08/02/more-on-kvhos-ss-shapeshifter-solver/
- https://shewhoshapes.wordpress.com/2007/08/04/kvho-wins-what-next/

# Other solvers:

Neopets Shapeshifter:
- http://web.eecs.utk.edu/~jplank/plank/classes/cs140/Labs/Lab9/
- https://github.com/dzou/ShapeShifterSolver
- https://clraik.com/forum/downloads.php?do=file&id=105
- https://github.com/diceroll123/shapeshiftersolver

Lights Out:
- Archive of Interesting Code - Keith Schwarz https://www.keithschwarz.com/interesting/code/?dir=lights-out

# Mathematics:
https://www.jaapsch.net/puzzles/lomath.htm

- The Game of Lights Out - Rebecca S. Meyer https://dc.ewu.edu/theses/167/
- The Lights Out Game on Directed Graphs - Elise Dettling, Darren Parker https://arxiv.org/pdf/2306.06017.pdf
- NUMBER OF SOLUTIONS TO THE LIGTHS OUT GAME - VICENTE MUNOZ (http://www.mat.ucm.es/~vmunozve/lights-out.pdf)
- Modified Lights Out on Generalized Petersen Graphs - Jacob K Porter (Poster, AMS JMM 2023)
- Barile, Margherita. "Lights Out Puzzle." From MathWorld--A Wolfram Web Resource, created by Eric W. Weisstein. https://mathworld.wolfram.com/LightsOutPuzzle.html
- Lights Out: Solutions Using Linear Algebra - Matthew A. Madsen http://cau.ac.kr/~mhhgtx/courses/LinearAlgebra/references/MadsenLightsOut.pdf
- Lights Out on graphs - Abraham Berman, Franziska Borer, Norbert Hungerbühler 10.1007/s00591-021-00297-5

# ChatGPT 3.5
- I have added a chat gpt 3.5 log as a text file

