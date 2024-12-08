import sys; sys.path.append(".")
from kerykeion.charts.kerykeion_chart_svg import *
from kerykeion.utilities import setup_logging



class AstroImageGen:

    def __init__(self, full_name=None, birthday=None, birthtime=None, city=None, country=None): # ("John Lennon", 1940, 10, 9, 18, 30, "Liverpool", "GB")
        setup_logging(level="debug")
        year, month, day = birthday
        hour, minute = birthtime
        self.profile = AstrologicalSubject(full_name, year, month, day, hour, minute, city, country)
        self.internal_natal_chart = KerykeionChartSVG(self.profile, theme="dark-high-contrast")

    def image_generator(self):
        svg_path = self.internal_natal_chart.makeSVG()
        self.internal_natal_chart.capture_svg_screenshot(svg_path)

if __name__ == "__main__":
    # Get user input
    full_name = input("Enter the full name: ")  # e.g., "John Lennon"
    birthday = input("Enter the birthday (year, month, day) separated by commas: ").split(",")
    birthday = [int(x.strip()) for x in birthday]  # Convert to integers
    
    birthtime = input("Enter the birthtime (hour, minute) separated by commas: ").split(",")
    birthtime = [int(x.strip()) for x in birthtime]  # Convert to integers
    
    city = input("Enter the city of birth: ")  # e.g., "Liverpool"
    country = input("Enter the country code (e.g., 'GB' for Great Britain): ")  # e.g., "GB"
    
    # Create AstroImageGen instance and generate the chart image
    astro_gen = AstroImageGen(full_name, birthday, birthtime, city, country)
    astro_gen.image_generator()