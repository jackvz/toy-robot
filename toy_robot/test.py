import unittest
from .toy_robot import ToyRobot

class TestToyRobot(unittest.TestCase):

  def test_init(self):
    the_toy_robot = ToyRobot()
    self.assertEqual(the_toy_robot.X, None)
    self.assertEqual(the_toy_robot.Y, None)
    self.assertEqual(the_toy_robot.F, None)

  def test_place(self):
    the_toy_robot = ToyRobot()
    self.assertEqual(the_toy_robot.is_placed(), False)
    the_toy_robot.place(5, 5, 'NONE')
    self.assertEqual(the_toy_robot.is_placed(), False)
    self.assertEqual(the_toy_robot.X, None)
    self.assertEqual(the_toy_robot.Y, None)
    self.assertEqual(the_toy_robot.F, None)
    the_toy_robot.place(0, 0, 'NORTH')
    self.assertEqual(the_toy_robot.is_placed(), True)
    self.assertEqual(the_toy_robot.X, 0)
    self.assertEqual(the_toy_robot.Y, 0)
    self.assertEqual(the_toy_robot.F, 'NORTH')
    the_toy_robot.place(4, 4, 'SOUTH')
    self.assertEqual(the_toy_robot.is_placed(), True)
    self.assertEqual(the_toy_robot.X, 4)
    self.assertEqual(the_toy_robot.Y, 4)
    self.assertEqual(the_toy_robot.F, 'SOUTH')

  def test_turn_left(self):
    the_toy_robot = ToyRobot()
    the_toy_robot.place(0, 0, 'NORTH')
    self.assertEqual(the_toy_robot.F, 'NORTH')
    the_toy_robot.left()
    self.assertEqual(the_toy_robot.F, 'WEST')
    the_toy_robot.left()
    self.assertEqual(the_toy_robot.F, 'SOUTH')
    the_toy_robot.left()
    self.assertEqual(the_toy_robot.F, 'EAST')
    the_toy_robot.left()
    self.assertEqual(the_toy_robot.F, 'NORTH')

  def test_turn_right(self):
    the_toy_robot = ToyRobot()
    the_toy_robot.place(0, 0, 'NORTH')
    self.assertEqual(the_toy_robot.F, 'NORTH')
    the_toy_robot.right()
    self.assertEqual(the_toy_robot.F, 'EAST')
    the_toy_robot.right()
    self.assertEqual(the_toy_robot.F, 'SOUTH')
    the_toy_robot.right()
    self.assertEqual(the_toy_robot.F, 'WEST')
    the_toy_robot.right()
    self.assertEqual(the_toy_robot.F, 'NORTH')

  def test_move_north(self):
    the_toy_robot = ToyRobot()
    the_toy_robot.place(0, 0, 'NORTH')
    self.assertEqual(the_toy_robot.Y, 0)
    the_toy_robot.move()
    self.assertEqual(the_toy_robot.Y, 1)
    the_toy_robot.place(0, 4, 'NORTH')
    self.assertEqual(the_toy_robot.Y, 4)
    the_toy_robot.move()
    self.assertEqual(the_toy_robot.Y, 4)

  def test_move_south(self):
    the_toy_robot = ToyRobot()
    the_toy_robot.place(0, 4, 'SOUTH')
    self.assertEqual(the_toy_robot.Y, 4)
    the_toy_robot.move()
    self.assertEqual(the_toy_robot.Y, 3)
    the_toy_robot.place(0, 0, 'SOUTH')
    self.assertEqual(the_toy_robot.Y, 0)
    the_toy_robot.move()
    self.assertEqual(the_toy_robot.Y, 0)

  def test_move_east(self):
    the_toy_robot = ToyRobot()
    the_toy_robot.place(0, 0, 'EAST')
    self.assertEqual(the_toy_robot.X, 0)
    the_toy_robot.move()
    self.assertEqual(the_toy_robot.X, 1)
    the_toy_robot.place(4, 0, 'EAST')
    self.assertEqual(the_toy_robot.X, 4)
    the_toy_robot.move()
    self.assertEqual(the_toy_robot.X, 4)

  def test_move_west(self):
    the_toy_robot = ToyRobot()
    the_toy_robot.place(4, 0, 'WEST')
    self.assertEqual(the_toy_robot.X, 4)
    the_toy_robot.move()
    self.assertEqual(the_toy_robot.X, 3)
    the_toy_robot.place(0, 0, 'WEST')
    self.assertEqual(the_toy_robot.X, 0)
    the_toy_robot.move()
    self.assertEqual(the_toy_robot.X, 0)

  def test_report(self):
    the_toy_robot = ToyRobot()
    the_toy_robot.place(0, 0, 'NORTH')
    self.assertEqual(the_toy_robot.report(), '[bold yellow]The robot is at {}, {}, facing {}.[/bold yellow]'.format(0, 0, 'NORTH'))
    the_toy_robot.place(1, 1, 'EAST')
    self.assertEqual(the_toy_robot.report(), '[bold yellow]The robot is at {}, {}, facing {}.[/bold yellow]'.format(1, 1, 'EAST'))
    the_toy_robot.place(2, 2, 'SOUTH')
    self.assertEqual(the_toy_robot.report(), '[bold yellow]The robot is at {}, {}, facing {}.[/bold yellow]'.format(2, 2, 'SOUTH'))
    the_toy_robot.place(3, 3, 'WEST')
    self.assertEqual(the_toy_robot.report(), '[bold yellow]The robot is at {}, {}, facing {}.[/bold yellow]'.format(3, 3, 'WEST'))
