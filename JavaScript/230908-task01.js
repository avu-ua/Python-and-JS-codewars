// Task 1 - 08/09/2023 - Yulia 
// https://www.codewars.com/kata/564e1d90c41a8423230000bc/javascript

// ---------------------- DESCRIPTION ----------------------

// Knight vs King

// On the chess board rows, denoted by numbers, are called ranks, and columns, denoted by a letter, are called files).

// You put a Knight and a King in the board.

// Complete the method that tell us which one can capture the other one.

// You are provided with two object array; each contains an integer (the rank, first item) and a string/char (the file, second item) to show the position of the pieces in the chess board.

// Return:

// "Knight" if the knight is putting the king in check,
// "King" if the king is attacking the knight
// "None" if none of the above occur
// Example:

// knight = [7, "B"], king = [6, "C"]  ---> "King"

// ===============  Slava ===============
function knightVsKing(knightPosition, kingPosition) {
    const kingAttacksRelative = [[1,-1], [1,0], [1,1], [0,-1], [0,1], [-1,-1], [-1,0], [-1,1]]
    const knightAttacksRelative = [[1,-2], [2,-1], [2,1], [1,2], [-1,2], [-2,1], [-2,-1], [-1,-2]]

    for (const cellRelative of kingAttacksRelative) {
        const cellAbsolute = [kingPosition[0] + cellRelative[0], kingPosition[1].charCodeAt(0) + cellRelative[1]]
        if (cellAbsolute[0] === knightPosition[0] && cellAbsolute[1] === knightPosition[1].charCodeAt(0)) return "King"
    }

    for (const cellRelative of knightAttacksRelative) {
        cellAbsolute = [knightPosition[0] + cellRelative[0], knightPosition[1].charCodeAt(0) + cellRelative[1]]
        if (cellAbsolute[0] === kingPosition[0] && cellAbsolute[1] === kingPosition[1].charCodeAt(0)) return "Knight"
    }
    return "None"
}