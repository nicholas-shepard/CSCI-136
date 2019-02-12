#Original code
force = G * mass1 * mass2 / radius * radius

#Fixed code (operator rules caused for G*mass1*mass2 to be divided by radius before the radius could be squared)
force = G * mass1 * mass2 / (radius * radius)
