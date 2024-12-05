# Import the main class for creating a kerykeion instance:
from kerykeion import AstrologicalSubject

# Create a kerykeion instance:
# Args: Name, year, month, day, hour, minuts, city, nation
kanye = AstrologicalSubject("Kanye", 1977, 6, 8, 8, 45, "Atlanta", "US")

# Get the information about the sun in the chart:
# (The position of the planets always starts at 0)
kanye.sun

#> {'name': 'Sun', 'quality': 'Mutable', 'element': 'Air', 'sign': 'Gem', 'sign_num': 2, 'pos': 17.598992059774275, 'abs_pos': 77.59899205977428, 'emoji': '♊️', 'house': '12th House', 'retrograde': False}

# Get information about the first house:
kanye.first_house

#> {'name': 'First_House', 'quality': 'Cardinal', 'element': 'Water', 'sign': 'Can', 'sign_num': 3, 'pos': 17.995779673209114, 'abs_pos': 107.99577967320911, 'emoji': '♋️'}

# Get element of the moon sign:
kanye.moon.element

#> 'Water'