def main():
    # Get input of the map, line by line
    line1 = input('Enter the 1st line, R & C, of the map: ')
    rows_columns = line1.split()
    rows = int(rows_columns[0])
    columns = int(rows_columns[1])

    map_rows = []
    for i in range(rows):
      add_line = input('Enter the next line: ')
      map_rows.append(add_line)
    
    check_space(rows, columns, map_rows)
    
def check_space(rows, columns, map_rows):
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    # Check for parking space by looping through characters in columns, row by row
    for col in range(columns - 1):
        for row in range(rows - 1):
            # Access the 2x2 cell
            space = map_rows[row][col:col+2] + map_rows[row+1][col:col+2]
            if '#' in space:
                continue
            
            x_count = 0
            for s in space:
                if 'X' == s:
                    x_count += 1
            if x_count == 0:
                count0 += 1
            elif x_count == 1:
                count1 += 1
            elif x_count == 2:
                count2 += 1
            elif x_count == 3:
                count3 += 1
            else:
                count4 += 1
    print(count0)
    print(count1)
    print(count2)
    print(count3)
    print(count4)
    
if __name__ == '__main__':
    main()