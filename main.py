from enum import Enum


class EnumGameSate(Enum):
    INITIAL = 0
    RUNNING = 1
    PAUSED = 2
    GAME_OVER = 3


class EnumTankDirection(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class EnumTankState(Enum):
    IDLE = 0
    MOVING = 1
    SHOOTING = 2


class Game:
    def __init__(self):
        self.state = EnumGameSate
        self.score = 0
        self.deltaTime = 0
        self.movableObjects = []
        self.immovableObjects = []

    def tick(self, deltaTime):
        pass

    def getState(self):
        return self.state

    def getScore(self):
        return self.score

    def getMovableObjects(self):
        return self.movableObject

    def getImmovableObjects(self):
        return self.immovableObjects

    def setState(self, state):
        self.state = state

    def setScore(self, score):
        self.score = score

    def setMovableObjects(self, movableObjects):
        self.movableObject = movableObjects

    def setImmovableObjects(self, immovableObjects):
        self.immovableObject = immovableObjects


class MovableObject:
    def __init__(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed


class Tank(MovableObject):
    def __init__(self, health, direction, state, bullets, speed):
        super().__init__(speed)
        self.health = health
        self.direction = direction
        self.state = state
        self.bullets = bullets

    def fire(self):
        pass

    def update(self, deltaTime):
        pass

    def getHealth(self):
        return self.health

    def getDirection(self):
        return self.direction

    def getState(self):
        return self.state

    def getBullets(self):
        return self.bullets

    def setHealth(self, health):
        self.health = health

    def setDirection(self, direction):
        self.direction = direction

    def setState(self, state):
        self.state = state

    def setBullets(self, bullets):
        self.bullets = bullets


class PlayerTank(Tank):
    def __int__(self, lives, health, direction, state, bullets):
        super().__init__(health, direction, state, bullets)
        self.lives = lives

    def control(self):
        pass

    def getLives(self):
        return self.lives

    def setLives(self, lives):
        self.lives = lives


class EnemyTank(Tank):
    def __init__(self, type, health, direction, state, bullets):
        super().__init__(health, direction, state, bullets)
        self.type = type

    def update(self, deltaTime):
        pass

    def getType(self):
        return self.type

    def setType(self):
        self.type = type


class Bullet(MovableObject):
    def __init__(self, damage, speed):
        super().__init__(speed)
        self.damage = damage

    def getDamage(self):
        return self.damage

    def setDamage(self, damage):
        self.damage = damage


class StaticObject:
    def __init__(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def setPostion(self, positon):
        self.position = positon


class Wall(StaticObject):
    def __init__(self, durability, position):
        super().__init__(position)
        self.durability = durability

    def getDurability(self):
        return self.durability

    def setDurability(self, durability):
        self.durability = durability


class IDestroyable:
    def destroy(self):
        pass


class Bonuses(StaticObject):
    def __init__(self, duration, position):
        super().__init__(position)
        self.duration = duration

    def activable(self):
        pass

    def getDuration(self):
        return self.duration

    def setDuration(self, duration):
        self.duration = duration


class ExtraLife(Bonuses):
    def __init__(self, extraLives, duration, position):
        super().__init__(duration, position)
        self.extralives = extraLives

    def getExtraLives(self):
        return self.extralives

    def setExtraLives(self, extraLives):
        self.extralives = extraLives
