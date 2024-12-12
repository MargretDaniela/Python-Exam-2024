# Question one (i)
def circle_area (the_radius_of_a_circle):
    if(the_radius_of_a_circle > 0):
        pie = 3.14
        area = pie * (the_radius_of_a_circle)**2
        print(area)
    else:
        area = 0
    return area
print('The area is:')
circle_area (4)
    