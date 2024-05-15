vendedores={
    '01':{
        'name': 'Juan Perez',
        'ventas':[2500]
    },
    '02':{
        'name':'Maria Linares',
        'ventas':[5600]
    },
    '03':{
        'name':'Jose Castro',
        'ventas':[1700]
    }
}

vendedor = input('Hola, por favor ingrese la cantidad de datos que va a procesar')


while len(vendedor)  == 0 or vendedor not in vendedores:
    vendedor=(input('Debe llenar el campo, porfavor seleccione su número de Usuario Correctamente: '))
    
    
if vendedor in vendedores:
    print(f'Hola, {vendedores[vendedor]['name']}, carguemos una venta: ')
    print('*****')
    print('*****')
    
cargadeDatos= int(input('Cargue el valor de la venta: '))

while cargadeDatos <= 0:
    input('La venta no puede ser registrada con valores en 0, vuelva a ingresar un número ')



if cargadeDatos > 5000:
    print(f'Muy bien {vendedores[vendedor]['name']}, has ganado un premio')
    vendedores[vendedor]['ventas'].append(cargadeDatos)
    nuevaVenta = input('¿Deseas serguir cargando mas ventas?. Presione "y" para continuar, o "n" para terminar ')
    while nuevaVenta == "y":
        cargadeDatos= int(input('Cargue el valor de la venta: '))
        while cargadeDatos > 5000:
            print(f'Muy bien {vendedores[vendedor]['name']}, has ganado un premio')
            vendedores[vendedor]['ventas'].append(cargadeDatos)
            break
        vendedores[vendedor]['ventas'].append(cargadeDatos)
        nuevaVenta = input('¿Deseas serguir cargando mas ventas?. Presione "y" para continuar, o "n" para terminar ')
        if nuevaVenta == 'n':
           changevendedor = input('¿Deseas cambiar de usuario? "y" para continuar, "n" para terminar y ver todas las ventas')
elif cargadeDatos < 5000:
    vendedores[vendedor]['ventas'].append(cargadeDatos)
    nuevaVenta = input('¿Deseas serguir cargando mas ventas?. Presione "y" para continuar, o "n" para terminar ')
    while nuevaVenta == "y":
        cargadeDatos= int(input('Cargue el valor de la venta: '))
        while cargadeDatos > 5000:
            print(f'Muy bien {vendedores[vendedor]['name']}, has ganado un premio')
            vendedores[vendedor]['ventas'].append(cargadeDatos)
            break
        vendedores[vendedor]['ventas'].append(cargadeDatos)
        nuevaVenta = input('¿Deseas serguir cargando mas ventas?. Presione "y" para continuar, o "n" para terminar ')
        if nuevaVenta == 'n':
           changevendedor = input('¿Deseas cambiar de usuario? "y" para continuar, "n" para terminar y ver todas las ventas')


#2_
ventas_juan = sum(vendedores['01']['ventas'])
ventas_maria = sum(vendedores['02']['ventas'])
ventas_jose = sum(vendedores['03']['ventas'])

if ventas_jose ==  max(ventas_juan, ventas_maria, ventas_jose):
    print(f'Jose es el que mas ventas hizo, su total de ventas es: ${ventas_jose}')
elif ventas_maria ==  max(ventas_juan, ventas_maria, ventas_jose):
    print(f'Maria es el que mas ventas hizo, su total de ventas es: ${ventas_maria}')
elif ventas_juan ==  max(ventas_juan, ventas_maria, ventas_jose):
    print(f'Juan es el que mas ventas hizo, su total de ventas es: ${ventas_juan}')

#3_
ventasJuan = len(vendedores['01']['ventas'])
ventasMaria = len(vendedores['02']['ventas'])
ventasJose= len(vendedores['03']['ventas'])

nroDeVentasTotales = ventasJuan+ventasMaria+ventasJose
totalRecaudado = ventas_juan+ventas_jose+ventas_maria

promedioVentas = totalRecaudado/nroDeVentasTotales

print('El promedio de ventas generales es : $', format(promedioVentas))


#5_
print('El total recaudado por los diferentes vendedores es $',totalRecaudado )
