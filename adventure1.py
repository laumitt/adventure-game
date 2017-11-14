class Room:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = self.x, self.y
        posHistory = []
        setPos = posHistory.append(self.position)
    def dirCheck(self):
        print(self.position)

if __name__ == "__main__":
    room = Room()
    room.x = 2
    room.y = 5
    print(room.x + room.y)
