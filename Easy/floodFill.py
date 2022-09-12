# 733. Flood Fill

class Solution:

    def fill4directions(self, image: list[list[int]], sr: int, sc: int, color: int, start_color, rows, cols):
        curr_color = image[sr][sc]
        if curr_color == start_color:
            image[sr][sc] = color
            if sr - 1 >= 0 and image[sr - 1][sc] == start_color:
                self.fill4directions(image, sr - 1, sc, color, start_color, rows, cols)

            if sr + 1 <= rows and image[sr + 1][sc] == start_color:
                self.fill4directions(image, sr + 1, sc, color, start_color, rows, cols)

            if sc - 1 >= 0 and image[sr][sc - 1] == start_color:
                self.fill4directions(image, sr, sc - 1, color, start_color, rows, cols)

            if sc + 1 <= cols and image[sr][sc + 1] == start_color:
                self.fill4directions(image, sr, sc + 1, color, start_color, rows, cols)

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows = len(image) - 1
        cols = len(image[0]) - 1
        starting_color = image[sr][sc]
        if starting_color != color:
            self.fill4directions(image, sr, sc, color, starting_color, rows, cols)
        return image
