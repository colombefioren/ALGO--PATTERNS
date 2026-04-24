def max_area(height):
    left,right = 0, len(height) - 1
    distance = len(height) - 1
    max_area=min(height[left],height[right]) * distance
    while left < right:

        if(height[left] < height[right]):
            left += 1
            distance -= 1
        

        else:
            right -= 1
            distance -= 1


        current_area=min(height[left],height[right]) * distance
        if(current_area>max_area):
                max_area=current_area

    return max_area
        

print(max_area([1,2,3,1000,9]))