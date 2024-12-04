sf_population = 864816
sf_area = 231.89
rio_population = 6453682
rio_area = 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area
x = san_francisco_pop_density > rio_de_janeiro_pop_density
if x:
    print('True')
else:
    print("False")


avg = ((23+32+64)/3)
print (avg)