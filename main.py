import pygame, math

def branch(posx, posy, angle,recursion,len,last_color=False,last_width=False):
    if recursion > 0:
        # create color und width depending in the depth
        color = start_color.lerp(end_color,1-(recursion/recursion_depth))
        width = round((recursion/recursion_depth)*15)
        # create new point based on one position, angle and length
        pos2x = posx + int(math.cos(math.radians(angle)) * len)
        pos2y = posy + int(math.sin(math.radians(angle)) * len)
        # draw a line between the old and the newly created point
        pygame.draw.line(screen, color, (posx, posy), (pos2x, pos2y), width)
        # draws a circle to make rounded edges
        if last_color:
            pygame.draw.circle(screen,last_color,(posx,posy),last_width/2)
        # calls itself to create to other branches
        branch(pos2x, pos2y, angle - branch_angle + angle_differenz_left, recursion - 1,len* round(multiply,2))
        branch(pos2x, pos2y, angle + branch_angle + angle_differenz_right, recursion - 1,len* round(multiply,2),color,width)

# defined colors
start_color = pygame.Color(38, 70, 83)
end_color = pygame.Color(42, 157, 143)
background_color = pygame.Color(230,226,195)
# created font objekt
pygame.font.init()
font = pygame.font.SysFont('inputmonomedium', 15)

# defines all changable variables
branch_angle = 18
angle_differenz_right = 0
angle_differenz_left = 0
recursion_depth = 15
multiply = 0.8
first_branch = 120
branches = 3

# created varibles needed for better performance 
change = True
last_mouse = 0

# intililices pygame and creates new screen
pygame.init()
pygame.display.set_caption("fractal tree")
screen = pygame.display.set_mode((800, 800))

# defines start pont
startx = screen.get_width()/2
centery = screen.get_width()

# main loop
run = True
while run:

    event_list = pygame.event.get()
    for event in event_list:
        # if user closed the window stops loop
        if event.type == pygame.QUIT:
            run = False
        # checks for user input to change options
        if event.type == pygame.KEYDOWN:
            change = True
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_RIGHT:
                angle_differenz_right += 5
            if event.key == pygame.K_LEFT:
                angle_differenz_right -= 5
            if event.key == ord('a'):
                angle_differenz_left -= 5
            if event.key == ord('d'):
                angle_differenz_left += 5
            if event.key == pygame.K_UP:
                recursion_depth += 1
            if event.key == pygame.K_DOWN:
                recursion_depth -= 1
            if event.key == ord('w'):
                multiply += 0.05
            if event.key == ord('s'):
                multiply -= 0.05
            if event.key == pygame.K_1:
                first_branch += 5
            if event.key == pygame.K_2:
                first_branch -= 5

    # clears screen 
    screen.fill(background_color)

    # creates text lines that show the state of the options
    row1 = font.render(f"differenz right angle [left, right]: {angle_differenz_right} , differenz left angle [a,d] : {angle_differenz_left} ", False, (0, 0, 0))
    row2 = font.render(f"depth [up, down] : {recursion_depth} , first branch [1,2] : {first_branch}", False, (0, 0, 0))
    row3 = font.render(f"multiply length [w,s]: {round(multiply,2)} , branch angle [mouse pointer] : {branch_angle}", False, (0,0,0))

    screen.blit(row1, (0,0))
    screen.blit(row2, (0,20))
    screen.blit(row3, (0,40))


    # gets mouse position
    mousex, _ = pygame.mouse.get_pos()
    # f mouse position changed change "change" variable
    if mousex != last_mouse:
        change = True
        last_mouse = mousex
        # uses the x pos of the mouse to change the branch angle
        branch_angle = round((mousex/800)*180)

    # of a option changed draws fractal tree and refreches screen
    if change:
        branch(startx,centery,-90,recursion_depth,first_branch)
        pygame.display.update()
    # resets change variable
    change = False

# quits
pygame.image.save(screen, "screenshot.png")
pygame.quit()
pygame.font.quit()