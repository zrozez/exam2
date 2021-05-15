def func(name, **kwargs):
    print(name)
    for i in kwargs:
        print(f'{i} - {kwargs[i]}')
    return

func(name='USA', population = '330 million', is_democratic=True)
func(name='Kyrgyzstan', area='200 km2', have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])