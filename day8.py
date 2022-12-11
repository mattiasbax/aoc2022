import numpy as np


with open("day8_input.txt") as f:
    forest = [list(map(int, list(sub))) for line in f.readlines()
              for sub in zip(*line.rstrip())]
    forest = np.array(forest)


def calculate_visibility_for_forest(forest):
    def calculate_visibility_for_rows(forest, visibility_matrix):
        def calculate_visibilty_for_row(row, visibility_matrix):
            max_height = -1
            for ci, col in enumerate(row):
                if col == 9:
                    visibility_matrix[ci] = True
                    break
                elif col > max_height:
                    visibility_matrix[ci] = True
                    max_height = col

            max_height = -1
            for ci, col in reversed(list(enumerate(row))):
                if col == 9:
                    visibility_matrix[ci] = True
                    break
                elif col > max_height:
                    visibility_matrix[ci] = True
                    max_height = col

        for ri, row in enumerate(forest):
            calculate_visibilty_for_row(row, visibility_matrix[ri])

    visibility_matrix = np.full(forest.shape, False)
    calculate_visibility_for_rows(forest, visibility_matrix)
    calculate_visibility_for_rows(
        forest.transpose(), visibility_matrix.transpose())
    return visibility_matrix


def calculate_highest_viewscore(forest):
    def calculate_viewscore(ri, ci):
        tree = forest[ri, ci]
        row = forest[ri, :]
        col = forest[:, ci]

        left = 1
        for i in range(ci-1, -1, -1):
            next_tree = forest[ri, i]
            if next_tree >= tree:
                break
            left += 1

        right = 1
        for i in range(ci+1, forest.shape[0]):
            next_tree = forest[ri, i]
            if next_tree >= tree:
                break
            right += 1

        down = 1
        for i in range(ri+1, forest.shape[1]):
            next_tree = forest[i, ci]
            if next_tree >= tree:
                break
            down += 1

        up = 1
        for i in range(ri-1, -1, -1):
            next_tree = forest[i, ci]
            if next_tree >= tree:
                break
            up += 1
        return up*down*left*right

    best_viewscore = 0
    for ri, row in enumerate(forest):
        for ci, col in enumerate(row):
            viewscore = calculate_viewscore(ri, ci)
            if viewscore > best_viewscore:
                best_viewscore = viewscore
    return best_viewscore


visibility_matrix = calculate_visibility_for_forest(forest)
best_viewscore = calculate_highest_viewscore(forest)

print("The answer for day 8 part 1: ", visibility_matrix.sum())
print("The answer for day 8 part 2: ", best_viewscore)
