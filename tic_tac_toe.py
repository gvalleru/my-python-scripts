class Ttt:

    def __init__(self,matrix):
        self.matrix = self.convert(matrix)

    def convert(self,matrix):
        out_matrix = []
        for row in matrix:
            row_convert = []
            for c in row:
                row_convert.append(c.lower())
            out_matrix.append(row_convert)
        return out_matrix

    def print_matrix(self):
        for row in self.matrix:
            r=''
            for c in row:
                r = r + c + " "
            print r

    def get_single_unique(self, matrix):
        result = ''
        for row in matrix:
            if len(sorted(set(row))) == 1:
                result = row[0]
                break
            elif matrix[0][0] == matrix[1][1] == matrix[2][2]:
                result = matrix[0][0]
        return result

    def get_winner(self):
        result = self.get_single_unique(self.matrix)
        if result == '':
            result = self.get_single_unique(zip(*self.matrix))
        return result

input = [['O', 'x', 'o'], ['o', 'O', 'X'], ['x', 'x', 'X']]
ttt = Ttt(input)
print ttt.matrix
ttt.print_matrix()
winner = ttt.get_winner()

if winner != '':
    print "The winner is {}".format(winner)
else:
    print "It's a draw"
