import pygame
import math

# Initialize Pygame
pygame.init()

# Window size
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Lidar Simulation")

# Lidar sensor location
lidar_x = 300
lidar_y = 350

# Range of angles (in degrees) - sending rays towards the right side
start_angle = 0 - 5  # 10 degrees to the left of the center (right side)
end_angle = 0 + 5  # 10 degrees to the right of the center (right side)

# Factor to reduce the length of the rays before reaching the window boundaries
reduce_factor = 0.9


# Function to calculate intersection point with window boundaries
def calculate_intersection_point(angle):
    angle_radians = math.radians(angle)
    x_increment = window_width * reduce_factor * math.cos(angle_radians)
    y_increment = window_height * reduce_factor * math.sin(angle_radians)

    intersect_x = lidar_x + x_increment  # Sending rays towards the right side
    intersect_y = lidar_y + y_increment

    return intersect_x, intersect_y


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))  # Fill the window with white color

    # Draw lidar sensor
    pygame.draw.circle(window, (255, 0, 0), (lidar_x, lidar_y), 5)

    # Send rays and draw lines to intersect with window boundaries
    for angle in range(start_angle, end_angle + 1):
        intersect_x, intersect_y = calculate_intersection_point(angle)
        pygame.draw.line(window, (0, 0, 255), (lidar_x, lidar_y), (intersect_x, intersect_y))

    pygame.display.flip()
pygame.quit()
