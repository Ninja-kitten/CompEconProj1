# CompEconProj1
1 Reserve Price
Let’s extend our Monte Carlo simulation of the ascending clock auction to allow the seller to choose
a reserve price. A reserve price is the minimum price a seller is willing to accept to sell the item. If
the final clock price is below the reserve price the seller receives zero revenue.
For this assignment, assume the following parameters:
1. There are 5 buyers
2. Buyer values are drawn between 0 and 100 in increments of 5
3. Seller reserve prices are allowed to be between 0 and 100 in increments of 5
4. The item is considered sold when the clock price is greater than or equal to the reserve price
5. The auctions ending rules have now changed. The auction ends when either there are zero
buyers bidding at the current clock price, or there is one buyer bidding and the reserve price
has been met.
6. In the case of two buyers dropping out at the same price, you can go back to the previous
price and randomly choose the winning buyer (if there is a winner).
What reserve price should the seller choose (which price generates the most revenue)? Provide
an illustration that supports your result.
2 Number of Paths
You find yourself in the center of an NxN grid of points (where N is odd). At random you choose
a direct neighbor (left, right, up, down) and walk to that point. You do this M times to generate a
random path subject to the following constraints:
• The edge of the grid does not wrap around. Therefore if you are in a corner there are only
two potential moves.
• You cannot walk to the same point twice on the same path.
• A path must be M points long.
Any path that does not correspond to the above conditions is invalid.
• How many paths are there in a 3 x 3 grid of length 4?
• How many paths are there in a 11 x 11 grid of length 13?
Hint: Use weighted sampling.

3 Conway’s Game of Life
Conway’s Game of Life is a ”game” with a simple set of rules that yields complex results. It works
as follows:
• There is an NxN matrix of alive and dead cells, typically by 1’s and 0’s, respectively
• Each cell has 8 surrounding neighbors. Cells on the edge and the corners wrap around to the
other side.
• Each period, the cells update according to the following rules:
– If a dead cell has exactly 3 alive neighbors next to it, it becomes alive.
– If an alive cell has either 2 or 3 alive neighbors next to it, it remains alive.
– If an live cell has fewer than 2 alive neighbors next to it, it dies of loneliness.
– If an alive cell has more than 3 alive neighbors next to it, it dies of overcrowding. Such
is life.
• The cells should be updated independently. So, If I am a cell, and my neighbor is currently
dead it must be counted as dead to me this period, even if it turns out it will be alive next
period.
Program the Game of Life. Run a test by creating a 4x4 matrix with only the 4 corners alive.
The four cells should remain stationary. After the test is working, create a 50x50 matrix with each
cell randomly turned on or off. Run it for 100 periods. Plot it using matplotlib.pyplot.matshow.
There are many ways to display the 100 matrix plots and I will leave it up to you to find an elegant
solution.
