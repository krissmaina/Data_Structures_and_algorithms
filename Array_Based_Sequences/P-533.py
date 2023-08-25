class Matrix:
    """A matrix class that can add and multiply two-dimensional array of numbers."""

    def add(self, A, B):
        """Adds two dimensional array of numbers."""
        result = []
        layer1 = len(A)
        layer2 = len(A[0])

        for i in range(layer1):
            column = []
            for j in range(layer2):
                
                column.append(A[i][j] + B[i][j])
            
            result.append(column)

        return result
    
    def multipy(self, A, B):
        """Multiplies two dimensional array of numbers."""
        result = []
        layer1 = len(A)
        layer2 = len(A[0])

        for i in range(layer1):
            column = []
            for j in range(layer2):
                
                column.append(A[i][j] * B[i][j])
            
            result.append(column)

        return result


matrix = Matrix()
listA = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

listB = [[10, 11, 12],
         [13, 14, 15],
         [16, 17, 18]]

print(matrix.add(listA, listB))
print(matrix.multipy(listA, listB))
