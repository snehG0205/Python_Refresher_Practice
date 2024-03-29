def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        full_area = side_area + 2 * top_area
        return full_area
    else:
        return side_area

area = cylinder_surface_area(10, 5, True)
print(area)
area = cylinder_surface_area(10, 5, False)
print(area)