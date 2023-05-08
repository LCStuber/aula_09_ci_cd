import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sum():
    # given a number a = 3 and a number b = 4
    a = 3
    b = 4

    # when we calculate the sum
    output = methods.sum(a, b)
    
    # then the sum should be 7
    assert output == 7

def test_dif():
    # given a number a = 3 and a number b = 4
    a = 3
    b = 4

    # when we calculate the dif
    output = methods.dif(a, b)
    
    # then the dif should be -1
    assert output == -1

def test_product():
    # given a number a = 3 and a number b = 4
    a = 3
    b = 4

    # when we calculate the product
    output = methods.product(a, b)
    
    # then the product should be 12
    assert output == 12

def test_div():
    # given a number a = 12 and a number b = 4
    a = 12
    b = 4

    # when we calculate the div
    output = methods.div(a, b)
    
    # then the div should be 7
    assert output == 3