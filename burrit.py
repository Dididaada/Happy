import motor
import runloop
from hub import port

# Function to make the robot move forward
async def move_forward(degrees, speed):
    await motor.run_for_degrees(port.A, degrees, speed)
    await motor.run_for_degrees(port.B, degrees, speed)

# Function to make the robot turn left
async def turn_left(degrees, speed):
    await motor.run_for_degrees(port.A, -degrees, speed)
    await motor.run_for_degrees(port.B, degrees, speed)

# Function to make the robot turn right
async def turn_right(degrees, speed):
    await motor.run_for_degrees(port.A, degrees, speed)
    await motor.run_for_degrees(port.B, -degrees, speed)

# Function to make the robot do a full rotation
async def full_rotation(degrees, speed):
    await motor.run_for_degrees(port.A, degrees, speed)
    await motor.run_for_degrees(port.B, -degrees, speed)

# Function for line following
async def line_follow():
    # Implement your line following logic here
    pass

# Example usage within the main coroutine
async def main():
    await move_forward(360, 720)  # Move forward 360 degrees at 720 degrees per second
    await turn_left(180, 360)    # Turn left 180 degrees at 360 degrees per second
    await turn_right(180, 360)   # Turn right 180 degrees at 360 degrees per second
    await full_rotation(360, 720) # Perform a full rotation

    # Execute line following function
    await line_follow()

runloop.run(main())
