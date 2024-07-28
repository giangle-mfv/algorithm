in order to finish a game, a player has to complete N missions. The mission are the numbered from 0 to N-1. the K-th mission has an integer D[K] assigned representing its difficulty level.
During a day, you can perform in the specified order, in other words, a mission can be undertaken only if all of the mission preceding it have already been completed.
the difference between the difficulty levels of any two missions performed on the same day should not be greated than an integer X
Write the function def  solution (D, X)
that, given an array D of N integer and an integer X, return the minimum numbers of days required to complete all of the missions in the game.
examples:
D = [5,8,2,7] and X = 3, your function should return 3
D = [2,5,9,2,1,4] and X = 4, function should return 3
D = [1,12,10,4,5,2] and X = 2. function should return 4