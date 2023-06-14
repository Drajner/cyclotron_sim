import sympy as sp
import numpy as np

#calculate_particle_position(q, m, v, d, )

def calculate_path(q, m, v, b):

    q *= 1.6e-19
    m *= 1.67e-27
    v *= 1000
    b_vector = np.array([0.0,0.0,b])

    cyclotron_radius = .05
    gap_size = 1e-4
    t = 0 
    dt = 1e-11 

    particle_position = np.array([0.0,0.0,0.0])
    particle_velocity = np.array([0.0,0.0,0.0]) 

    particle_position_x = [particle_position[0]] 
    particle_position_y = [particle_position[1]] 

    electric_field = v/(gap_size) 
    frequency = q*np.linalg.norm(b_vector)/m 

    while (np.linalg.norm(particle_position) < cyclotron_radius): 
        
        force = np.array([0.0,0.0,0.0]) 
        
        if np.absolute(particle_position[0]) < gap_size/2: 
            force[0] = q*electric_field*np.cos(frequency*t)
        else: 
            force = q*np.cross(particle_velocity, b_vector)

        particle_velocity = particle_velocity + force*dt/m
        particle_position = particle_position + particle_velocity*dt
        
        particle_position_x = np.append(particle_position_x, particle_position[0])
        particle_position_y = np.append(particle_position_y, particle_position[1])
        t = t + dt

    return (particle_position_x, particle_position_y)