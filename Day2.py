file_path = 'Day2Input.txt'  # Replace 'your_file.txt' with the actual file path

with open(file_path, 'r') as file:

    dic = {"red": 12, "green": 13, "blue": 14}
    # Iterate over each line in the file
    sumId = 0
    sumP = 0
    for line in file:
        possible = True
        game = line.split(':')
        gameId = game[0].split(' ')[1]
        rounds = game[1].split('; ')

        for r in rounds:
            if not possible:
                break
            cubes = r.split(', ')
            for c in cubes:
                c = c.strip()
                cubes_num = c.split(' ')[0]
                cubes_color = c.split(' ')[1]
                if int(cubes_num) > dic[cubes_color]:
                    possible = False
                    break

        if possible:
            sumId += int(gameId)

        max_color = {'red': 0, 'green': 0, 'blue': 0}
        for r in rounds:
            cubes = r.split(', ')
            for c in cubes:
                c = c.strip()
                cubes_num = c.split(' ')[0]
                cubes_color = c.split(' ')[1]

                if int(cubes_num) > max_color[cubes_color]:
                    max_color[cubes_color] = int(cubes_num)

        sumP += max_color['red'] * max_color['green'] * max_color['blue']
    print(sumP)

