def make_car(name, clas, **car_tex):
    
    car_tex['car'] = name
    car_tex['class'] = clas
    return car_tex
    

car = make_car('subaru', 'outback', color='blue', tow_package= True)
print(car)
