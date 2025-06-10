import math

def calculate_circle_properties(radius):
    """Calculates the area and perimeter of a circle.

    Args:
      radius: The radius of the circle.

    Returns:
      A tuple containing the area and perimeter of the circle.
    """
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    area, perimeter = calculate_circle_properties(radius)
    print(f"Area of the circle: {area:.2f}")
    print(f"Perimeter of the circle: {perimeter:.2f}")