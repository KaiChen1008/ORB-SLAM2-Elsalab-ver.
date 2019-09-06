import pygame
from communication import sender

speed_ratio_l = 0   # To slow down linear velocity smoothly
speed_ratio_a = 0   # To slow down angular velocity smoothly
pre_linear_v = 0    # Record previous motion
pre_angular_v = 0   # Record previous motion
full_speed = 0.5    # Highest speed


pygame.init()
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates.
clock = pygame.time.Clock()
# Initialize the joysticks.
pygame.joystick.init()

sendman = sender()

# -------- Main Program Loop -----------
while not done:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    # create message
    j = {
        'linear_x' : 0.0,
        'linear_y' : 0.0,
        'linear_z' : 0.0,
        'angular_x': 0.0,
        'angular_y': 0.0,
        'angular_z': 0.0,
    }
    
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    buttons = joystick.get_numbuttons()
    
    if joystick.get_button(3) == 1: # button Y
        full_speed = full_speed + 0.025 if full_speed < 1 else 1
        print('speed up')
    if joystick.get_button(1) == 1: # button A
        full_speed = full_speed - 0.025 if full_speed > 0.05 else 0.05
        print('speed down')
    if joystick.get_button(0) == 1: # button X
        speed_ratio_l = 0
        speed_ratio_a = 0
        full_speed = 0.5
        print('reset speed')
    
    hat = joystick.get_hat(0)
    linear_v = hat[1]
    angular_v= hat[0]

    # decide linear velocity
    if linear_v:
        if pre_linear_v * linear_v == -1: # Suddenly change of direction leads to speed drop to 0.
            speed_ratio_l = 0
        pre_linear_v = linear_v
        j['linear_x'] = speed_ratio_l * full_speed * linear_v
        speed_ratio_l = speed_ratio_l + 0.04 if speed_ratio_l < 1 else 1
    else:
        j['linear_x'] = speed_ratio_l * full_speed * pre_linear_v
        speed_ratio_l = speed_ratio_l - 0.04 if speed_ratio_l > 0 else 0
    # decide angular velocity
    if angular_v:
        if pre_angular_v * angular_v == -1: 
            speed_ratio_a = 0
        pre_angular_v = angular_v
        j['angular_z'] = speed_ratio_a * full_speed * angular_v
        speed_ratio_a = speed_ratio_a + 0.05 if speed_ratio_a < 1 else 1 
    else:
        j['angular_z'] = speed_ratio_a * full_speed * pre_angular_v
        speed_ratio_a = speed_ratio_a - 0.1 if speed_ratio_a >= 0.1 else 0


    if joystick.get_button(2) == 1: # button B shutdowwn
        print("shutdown!!!!!!!!")
        j = {
            'linear_x' : 0.0,
            'linear_y' : 0.0,
            'linear_z' : 0.0,
            'angular_x': 0.0,
            'angular_y': 0.0,
            'angular_z': 0.0,
        }
        speed_ratio_l = 0
        speed_ratio_a = 0
    
    if j['linear_x'] != 0 or j['angular_z'] != 0:
        sendman.send(j)
        print ('Linear Speed \t %f' % j['linear_x'])
        print ('Angular Speed \t %f' % j['angular_z'])
        print ('Full Speed \t %f' % full_speed)
        print('------------------------------------------')

    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
