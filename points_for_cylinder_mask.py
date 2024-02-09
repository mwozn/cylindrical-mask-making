#!/usr/bin/env python
# mwozny 20240117
# Example usage with file input and dynamic output file name
pt_input = 'oct_centres.pt'  # replace with the path to your input .pt file, generate from .mod with IMOD's model2points
cylinder_radius = 17  # replace with your desired radius in px of the cylinder

import os
import numpy as np

def calculate_vector(point1, point2):
    return np.array(point2) - np.array(point1)

def create_cylinder_points(point1, point2, cylinder_radius, sphere_spacing):
    vector = calculate_vector(point1, point2)
    cylinder_length = np.linalg.norm(vector)

    num_points = int(cylinder_length / sphere_spacing)
    step = vector / num_points

    cylinder_points = [tuple(np.round(np.array(point1) + i * step, 2)) for i in range(num_points + 1)]

    return cylinder_points, cylinder_length

def read_points_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        point1 = tuple(map(float, lines[0].split()))
        point2 = tuple(map(float, lines[1].split()))
    return point1, point2

def write_points_to_file(file_path, points, cylinder_length, cylinder_radius):
    if os.path.exists(file_path):
        overwrite = input(f"The file {file_path} already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != 'y':
            print("Exiting without overwriting the file.")
            return

    with open(file_path, 'w') as file:
        for point in points:
            file.write('\t'.join(map(str, point)) + '\n')

    print(f"Created points for a cylinder {cylinder_length:.2f} in length, with a radius of {cylinder_radius}, "
          f"between {point1} and {point2}. Saved to {file_path}")

# Space the spheres
sphere_spacing = cylinder_radius / 8.0

# Generate dynamic output file path
pt_output = f"{os.path.splitext(pt_input)[0]}_vector_r{cylinder_radius}.pt"

point1, point2 = read_points_from_file(pt_input)
cylinder_points, cylinder_length = create_cylinder_points(point1, point2, cylinder_radius, sphere_spacing)

write_points_to_file(pt_output, cylinder_points, cylinder_length, cylinder_radius)