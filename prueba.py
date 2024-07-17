import os, random
os.system('cls')

def sueldo_aleatorio(nombres):
    sueldos=[]
    for i in range(10):
        sueldo=random.randint(300000, 2500000)
        sueldos.append(sueldo)
    
    empleados=list(zip(nombres, sueldos))
    return empleados

trabajadores=['juan perez',
              'maria garcia',
              'carlos lopez',
              'ana martinez',
              'pedro rodriguez',
              'laura hernandez',
              'miguel sanchez',
              'isabel gomez',
              'francisco diaz',
              'elena fernandez'
              ]
empleados_mas_sueldos=sueldo_aleatorio(trabajadores)

def menu(titulo,lista):
    while True:
        i=1
        for item in lista:
            print(i,'.-',item)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('La opción debe estar entre 1 y ',i)
        else:
            print('Debe Ingresar un Número')

lista_todo=[]  
while True:
    opc=menu('menu principal',['asignar sueldos aleatorios','clasificar sueldos','reporte de sueldos',])
    if opc==1:
        empleados_mas_sueldos=sueldo_aleatorio(trabajadores)
        diccionario={}
        diccionario['sueldo']=empleados_mas_sueldos
        lista_todo.append(diccionario)
        print(lista_todo)
    elif opc==2:
        print('sueldos menores a $800.000\n')
        for nombre, sueldo in empleados_mas_sueldos:
            if sueldo<800000:
                print(f'{nombre}    {sueldo}')
        print('\nsueldos entre $800.000 y $2.000.000\n')
        for nombre, sueldo in empleados_mas_sueldos:
            if sueldo>=800000 and sueldo<=2000000:
                print(f'{nombre}    {sueldo}')
        print('\nsueldos superiores a $2.000.000\n')
        for nombre, sueldo in empleados_mas_sueldos:
            if sueldo>2000000:
                print(f'{nombre}    {sueldo}')
    elif opc==3:
        print()
        for nombre, sueldo in empleados_mas_sueldos:
            descuento_salud=sueldo*0.07
            descuento_afp=sueldo*0.12
            sueldo_liquido=sueldo-descuento_afp-descuento_salud
            print(nombre,'\n',sueldo,'\n',descuento_salud,'\n',descuento_afp,'\n',sueldo_liquido,'\n',end='-')
    else:
        print('finalizando programa...','\n','desarrollado por el crack del juan vera','\n','rut 21.245.279-3')
        break
