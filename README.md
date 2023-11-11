function makeMove(state, player, opponent) {
    const playerOccupiedCell = player;
    const opponentOccupiedCell = opponent;
    const blankCell = 0;

    // Function to check if there are four consecutive cells of the same player in any direction
    function isWinningMove(row, col, dr, dc, targetPlayer) {
        const checkCell = (r, c) => state[r] && state[r][c] === targetPlayer;

        for (let i = 0; i < 4; i++) {
            const r = row + i * dr;
            const c = col + i * dc;
            if (!checkCell(r, c)) {
                return false;
            }
        }
        return true;
    }

    // Function to check if a move is valid in the given column
    function isValidMove(row, col) {
        return row >= 0 && row < state.length && col >= 0 && col < state[0].length && state[row][col] === blankCell;
    }

    // Iterate through columns to find a valid move
    for (let column = 0; column < state[0].length; column++) {
        // Check if the top row of the current column is empty
        if (state[0][column] === blankCell) {
            // Check if making this move leads to a winning position for either player
            for (let row = state.length - 1; row >= 0; row--) {
                if (isValidMove(row, column)) {
                    // Check for both player and opponent
                    if (
                        isWinningMove(row, column, 0, 1, playerOccupiedCell) || // Horizontal
                        isWinningMove(row, column, 1, 0, playerOccupiedCell) || // Vertical
                        isWinningMove(row, column, 1, 1, playerOccupiedCell) || // Diagonal \
                        isWinningMove(row, column, 1, -1, playerOccupiedCell)   // Diagonal /
                    ) {
                        // This move leads to a winning position for the player, so return it
                        return column;
                    } else if (
                        isWinningMove(row, column, 0, 1, opponentOccupiedCell) || // Horizontal
                        isWinningMove(row, column, 1, 0, opponentOccupiedCell) || // Vertical
                        isWinningMove(row, column, 1, 1, opponentOccupiedCell) || // Diagonal \
                        isWinningMove(row, column, 1, -1, opponentOccupiedCell)   // Diagonal /
                    ) {
                        // This move blocks the opponent from winning, so consider it
                        // Continue checking other columns before making a decision
                        break;
                    }
                    return column; // Return the leftmost available column if neither player wins nor blocks
                }
            }
        }
    }

    // Fallback: return 0 if all else fails (you can modify this part)
    return 0;
}
