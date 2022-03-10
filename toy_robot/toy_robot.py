from rich import print

class ToyRobot:

  X = None
  Y = None
  F = None

  verbose = False
  visualise_board = False

  def __init__(self):
    self.X = None
    self.Y = None
    self.F = None

  def is_placed(self):
    if self.X == None and self.Y == None and self.F == None:
      return False
    else:
      return True

  def left(self):
    if self.is_placed():
      match self.F:
        case 'NORTH':
          self.F = 'WEST'
        case 'EAST':
          self.F = 'NORTH'
        case 'SOUTH':
          self.F = 'EAST'
        case 'WEST':
          self.F = 'SOUTH'
      if self.verbose: print('[bold green]Turning left. Now facing {}.[/bold green]'.format(self.F))
    else:
      if self.verbose: print('[bold red]Ignoring command. Not placed yet.[/bold red]')
    if self.visualise_board: self.show_board()

  def right(self):
    if self.is_placed():
      match self.F:
        case 'NORTH':
          self.F = 'EAST'
        case 'EAST':
          self.F = 'SOUTH'
        case 'SOUTH':
          self.F = 'WEST'
        case 'WEST':
          self.F = 'NORTH'
      if self.verbose: print('[bold green]Turning right. Now facing {}.[/bold green]'.format(self.F))
    else:
      if self.verbose: print('[bold red]Ignoring command. Not placed yet.[/bold red]')
    if self.visualise_board: self.show_board()

  def move(self):
    if self.is_placed():
      has_moved = False
      match self.F:
        case 'NORTH':
          if self.Y < 4:
            has_moved = True
            self.Y += 1
          else:
            if self.verbose: print('[bold red]Preventing move so as to not fall to destruction.[/bold red]')
        case 'EAST':
          if self.X < 4:
            has_moved = True
            self.X += 1
          else:
            if self.verbose: print('[bold red]Preventing move so as to not fall to destruction.[/bold red]')
        case 'SOUTH':
          if self.Y > 0:
            has_moved = True
            self.Y -= 1
          else:
            if self.verbose: print('[bold red]Preventing move so as to not fall to destruction.[/bold red]')
        case 'WEST':
          if self.X > 0:
            has_moved = True
            self.X -= 1
          else:
            if self.verbose: print('[bold red]Preventing move so as to not fall to destruction.[/bold red]')
      if has_moved:
        if self.verbose: print('[bold green]Moved one unit {}.[/bold green]'.format(self.F))
    else:
      if self.verbose: print('[bold red]Ignoring command. Not placed yet.[/bold red]')
    if self.visualise_board: self.show_board()

  def show_board(self):
    for y in range(4,-1,-1):
      line_output = ''
      for x in range(5):
        if self.X == x and self.Y == y:
          line_output += ' {} '.format(self.F[0])
        else:
          line_output += ' - '
      print('[bold blue]{}[/bold blue]'.format(line_output))

  def report(self):
    if self.is_placed():
      return '[bold yellow]The robot is at {}, {}, facing {}.[/bold yellow]'.format(self.X, self.Y, self.F)
    else:
      return '[bold red]Not placed yet.[/bold red]'
    if self.visualise_board: self.show_board()

  def place(self, x, y, f):
    if (f == 'NORTH' 
      or f == 'EAST' 
      or f == 'SOUTH' 
      or f == 'WEST') \
      and x >= 0 and x < 5 \
      and y >= 0 and y < 5:
        self.X = x
        self.Y = y
        self.F = f
        if self.verbose: print('[bold green]Placing robot at {}, {}, facing {}.[/bold green]'.format(self.X, self.Y, self.F))
    else:
      if self.verbose: print('[bold red]Invalid place command.[/bold red]')
    if self.visualise_board: self.show_board()
