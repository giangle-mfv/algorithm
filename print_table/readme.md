write the program with the task  as below by python:
you have an array of number and you would like to print these number in a tabular to make them look more organized. Each cell of the table contains exactly one number and is surrouded by exactly 4 edges:
+-+
|4|
+-+

+-----+
|12345|
+-----+
As you can see above, each corner of the cell is represented by a "+ sign, vertical edges by "-" sign and horizontal edges by "|" sign. The width of the cell adjusts to accommodate the number of digits of the number written within it. Ther can be many cells in a row. Adjacent cell share an edge:
+---+---+---+---+
|  4| 35|  80|123|
+---+---+---+---+
Note that each cell has the same width. The width of the cell adjust to match the width of the longest number in the table. The number in cells are aligned to the right, with any unused area in each cell filled with spaces. The table can consist of many rows, and adjacent rows share an edge:
+-----+-----+-----+-----+
|    4|  35|   80|  123|
+-----+-----+-----+-----+
|12345|   44|    😎    5|
Your goal is to output a table containing all the numbers from a give array such that each row contains exactly K numbers. The last row can contain fewer numbers.
Write the function:
def solution (A, K)
that, given a nion-empty array A consisting of N integers and an interger K, print a string representing the formatted arrray. The number in the table should appear in the same order as the numbers in the array.
For example, given arrray A = [4, 35, 80, 123, 12345, 44, 8, 5] and K = 10, the resultant table with contain exactly one row as show below:

The function shouldn't return any value.
You can print a string to the output(without or with the end -of-line character) as follow:
sys.stdout.write("sample string")
sys.stdout.write("whole line\n")