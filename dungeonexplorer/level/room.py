import random

class Room:

    def __init__(self, randomize=False, min_room_size=1, max_room_size=5, map_max=99, x=0, y=0, width=1, height=1):
        
        if randomize:
            self.x = random.randint(0, map_max - max_room_size)
            self.y = random.randint(0, map_max - max_room_size)
            self.width = random.randint(min_room_size, max_room_size)
            self.height = random.randint(min_room_size, max_room_size)

            if(self.width % 2 == 0):
                self.width = self.width + 1

            if(self.height % 2 == 0):
                self.height = self.height + 1

        else:
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.centerX = x + width // 2 
            self.centerY = y + height // 2

        self.centerX = self.x + self.width // 2 
        self.centerY = self.y + self.height // 2

    def intersects(self, room):
        R1 = (self.x, self.y, self.x + self.width, self.y + self.height)
        R2 = (room.x, room.y, room.x + room.width, room.y + room.height)

        if (R1[0] - R2[2] >= 1) or (R2[0] - R1[2] >= 1) or (R2[1] - R1[3]>= 1) or (R1[1] - R2[3] >= 1):
            return False
        else:
            return True