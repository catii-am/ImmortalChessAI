


class SearchPos:
    def GetX1(self, move):
        move_list = list(move)
        if move_list[0] == 'a':
            x1 = 41
        elif move_list[0] == 'b':
            x1 = 41 + 83
        elif move_list[0] == 'c':
            x1 = 41 + 83 * 2
        elif move_list[0] == 'd':
            x1 = 41 + 83 * 3
        elif move_list[0] == 'e':
            x1 = 41 + 83 * 4
        elif move_list[0] == 'f':
            x1 = 41 + 83 * 5
        elif move_list[0] == 'g':
            x1 = 41 + 83 * 6
        elif move_list[0] == 'h':
            x1 = 41 + 83 * 7
        return x1

    def GetY1(self, move):
        move_list = list(move)
        if move_list[1] == '1':
            y1 = 41
        elif move_list[1] == '2':
            y1 = 41 + 83
        elif move_list[1] == '3':
            y1 = 41 + 83 * 2
        elif move_list[1] == '4':
            y1 = 41 + 83 * 3
        elif move_list[1] == '5':
            y1 = 41 + 83 * 4
        elif move_list[1] == '6':
            y1 = 41 + 83 * 5
        elif move_list[1] == '7':
            y1 = 41 + 83 * 6
        elif move_list[1] == '8':
            y1 = 41 + 83 * 7
        return y1

    def GetX2(self, move):
        move_list = list(move)
        if move_list[2] == 'a':
            x2 = 41
        elif move_list[2] == 'b':
            x2 = 41 + 83
        elif move_list[2] == 'c':
            x2 = 41 + 83 * 2
        elif move_list[2] == 'd':
            x2 = 41 + 83 * 3
        elif move_list[2] == 'e':
            x2 = 41 + 83 * 4
        elif move_list[2] == 'f':
            x2 = 41 + 83 * 5
        elif move_list[2] == 'g':
            x2 = 41 + 83 * 6
        elif move_list[2] == 'h':
            x2 = 41 + 83 * 7
        return x2

    def GetY2(self, move):
        move_list = list(move)
        if move_list[3] == '1':
            y2 = 41
        elif move_list[3] == '2':
            y2 = 41 + 83
        elif move_list[3] == '3':
            y2 = 41 + 83 * 2
        elif move_list[3] == '4':
            y2 = 41 + 83 * 3
        elif move_list[3] == '5':
            y2 = 41 + 83 * 4
        elif move_list[3] == '6':
            y2 = 41 + 83 * 5
        elif move_list[3] == '7':
            y2 = 41 + 83 * 6
        elif move_list[3] == '8':
            y2 = 41 + 83 * 7
        return y2

    def GetY3(self, move):
        move_list = list(move)
        if move_list[4] == '1':
            y3 = 41
        elif move_list[4] == '2':
            y3 = 41 + 83
        elif move_list[4] == '3':
            y3 = 41 + 83 * 2
        elif move_list[4] == '4':
            y3 = 41 + 83 * 3
        elif move_list[4] == '5':
            y3 = 41 + 83 * 4
        elif move_list[4] == '6':
            y3 = 41 + 83 * 5
        elif move_list[4] == '7':
            y3 = 41 + 83 * 6
        elif move_list[4] == '8':
            y3 = 41 + 83 * 7
        return y3