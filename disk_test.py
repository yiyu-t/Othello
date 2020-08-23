from disk import Disk


def test_constructor():
    disk_1 = Disk(0, 100, 90, 50, 1, 2)
    assert disk_1.color == 0
    assert disk_1.SPACING == 100
    assert disk_1.DIAMATER == 90
    assert disk_1.LOCATION == 50
    assert disk_1.x == 1
    assert disk_1.y == 2

    disk_2 = Disk(255, 200, 100, 40, 10, 3)
    assert disk_2.color == 255
    assert disk_2.SPACING == 200
    assert disk_2.DIAMATER == 100
    assert disk_2.LOCATION == 40
    assert disk_2.x == 10
    assert disk_2.y == 3

    disk_3 = Disk(100, 500, 400, 60, 2, 5)
    assert disk_3.color == 100
    assert disk_3.SPACING == 500
    assert disk_3.DIAMATER == 400
    assert disk_3.LOCATION == 60
    assert disk_3.x == 2
    assert disk_3.y == 5
