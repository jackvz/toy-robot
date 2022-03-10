import os, sys
from rich import print
from toy_robot.toy_robot import ToyRobot

the_toy_robot = ToyRobot()
the_toy_robot.verbose = True
the_toy_robot.visualise_board = True

def process_command(command, is_from_file):
  match command:
    case 'LEFT':
      the_toy_robot.left()
    case 'RIGHT':
      the_toy_robot.right()
    case 'MOVE':
      the_toy_robot.move()
    case 'REPORT':
      print(the_toy_robot.report())
    case command:
      command_is_valid = False
      if command.startswith('PLACE'):
        command_parts = command.split(' ')
        if len(command_parts) == 2:
          command_details = command_parts[1].split(',')
          if len(command_details) == 3:
            try:
              command_x = int(command_details[0])
              command_y = int(command_details[1])
              command_f = command_details[2]
              if (command_f == 'NORTH' 
                or command_f == 'EAST' 
                or command_f == 'SOUTH' 
                or command_f == 'WEST') \
                and command_x >= 0 and command_x < 5 \
                and command_y >= 0 and command_y < 5:
                command_is_valid = True
                the_toy_robot.place(command_x, command_y, command_f)
            except:
              pass

      if command_is_valid == False:
        if is_from_file:
          print('[bold red]Invalid command[/bold red].')
        else:
          print('[bold red]Invalid command. Please try again.[/bold red]')


def main():

  try:
    os.system('cls')
  except:
    pass

  # --------------------------------------------------
  # Getting commands from a text file  
  # --------------------------------------------------

  if len(sys.argv) == 2:

    try:
      file=open(sys.argv[1], 'r')
      commands = file.readlines()
      for command in commands:
        process_command(command.strip().upper(), True)

    except IOError:
      print('[bold red]File not found.[/bold red]')
      exit(1)

  # --------------------------------------------------
  # Getting commands from user input  
  # --------------------------------------------------

  else:
    get_user_input = True
    while get_user_input:
      print('[bold blue]Enter a command (? for help):[/bold blue] ')
      user_input = input()
      match user_input.upper():
        case '?':
          print('[bold green]To place the robot, enter PLACE [X],[Y],[DIRECTION], e.g. PLACE 0,0,NORTH[/bold green]')
          print('[bold green]To change the direction that the robot is facing, enter LEFT or RIGHT[/bold green]')
          print('[bold green]To make the robot move one unit ahead, enter MOVE[/bold green]')
          print('[bold green]To display the current location of the robot and the direction that it is facing, enter REPORT[/bold green]')
          print('[bold green]To quit, enter QUIT[/bold green]')
        case 'QUIT':
          get_user_input = False
        case command:
          process_command(command, False)

if __name__ == '__main__':
  main()
