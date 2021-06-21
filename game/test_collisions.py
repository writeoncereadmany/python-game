from game import collisions
from testsupport.visualiser import show
from pygame import Rect

def test_collides():
    first = Rect((100, 100), (200, 200))
    second = Rect((200, 200), (100, 100))

    # show(first, second)
    assert collisions.collides(first, second)

def test_does_not_collide():
    first = Rect((100, 100), (100, 100))
    second = Rect((300, 300), (100, 100))

    # show(first, second)
    assert not collisions.collides(first, second)