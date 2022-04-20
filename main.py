from time import time

class ChessBoard:

    def __init__(self):

        self.grid = []

        for i in range(1,9):

            for j in range(1,9):

                self.grid.append((i,j))


    def getGrid(self):

        return self.grid

    def getNeigbours(self, position):

        neighbours = []

        for line_neighbourhood in [1,2]:

            if position[0] - line_neighbourhood > 0 :

                if position[1] - (3 - line_neighbourhood) > 0:

                    neighbours.append((position[0] - line_neighbourhood, position[1] - (3 - line_neighbourhood)))

                if position[1] + (3 - line_neighbourhood) < 9:

                    neighbours.append((position[0] - line_neighbourhood, position[1] + (3 - line_neighbourhood)))

            if position[0] + line_neighbourhood < 9:

                if position[1] - (3 - line_neighbourhood) > 0:
                    neighbours.append((position[0] + line_neighbourhood, position[1] - (3 - line_neighbourhood)))

                if position[1] + (3 - line_neighbourhood) < 9:
                    neighbours.append((position[0] + line_neighbourhood, position[1] + (3 - line_neighbourhood)))

        return neighbours

    def getDistance(self, first_point, second_point):

        return max(abs(first_point[0] - second_point[0]), abs(first_point[1] - second_point[1]))

    def clearOutliers(self, goal_point, elements_list, proximity):

        for i in range(len(elements_list)-1, -1, -1):

            if self.getDistance(goal_point, elements_list[i]) > proximity:

                del(elements_list[i])

        return elements_list

    def get_Minimum_Amount_of_Steps(self,starting_position,ending_position):

        if starting_position == ending_position:

            return 0

        neighbours = self.getNeigbours(starting_position)

        steps = 1

        proximity = 6

        while (not ending_position in neighbours):

            neighbours = self.clearOutliers(ending_position, neighbours, proximity)

            for i in range(len(neighbours)-1,-1,-1):

                second_neighbours = self.getNeigbours(neighbours[i])

                for element in second_neighbours:


                    if not element in neighbours:

                        neighbours.append(element)

                del(neighbours[i])

            proximity -= 1

            steps += 1

        return steps


if __name__ == '__main__':

    c = ChessBoard()

    start = time()

    print(c.get_Minimum_Amount_of_Steps((1,1),(8,8)))

    end = time()

    print("Duration:", end-start)
