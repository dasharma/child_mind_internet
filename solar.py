# OBJECTIVE: create a program that lets us enter some things:

# how many solar panels

# how big m^2 each solar panel is

# how far the panels are from the sun

# we need to figure out the energy produced by a solar panel using code

# solar panels on the ISS produce 190 W/m^2
# we need to see how far the ISS is from the sun (150,000,000 km)
# how much does distance from the sun change solar panel energy production
# the solar panel efficiency is inversely proportional to the square of the 
# distance from the sun

# x_o / x_1 = r_o^2 / r_1^2
# x_o = 190, r_o = 150,000,000
# r_1 = 155,000,000, x_1 = x_0 * r_1^2 / r_o^2

sp = int(input("How many solar panels:"))

sm2 = float(input("How many M^2 per solar panel:"))

dist = float(input("How many kilometers from the sun:"))

# watts per solar panel calculated
watts = sm2 * 190

# general watts on ISS on all solar panels
issp = watts * sp

print("Solar panel energy output on ISS is ", issp)

# x_o / x_1 = r_o^2 / r_1^2
# x_o = 190, r_o = 150,000,000
# r_1 = 155,000,000, x_1 = x_0 * r_1^2 / r_o^2

mikep = 190 * dist**2 / 150000000**2

print("Solar panel energy output at your distance:", mikep)