def jugarDeNuevo():
    r = input('¿Deseas ingresar otro peso? (S/N): ')
    if r == '':
        return True

    if r.startswith('s') or r.startswith('S'):
        return True
    else:
        return False

def comprobarKgOLb(p):
    if p.endswith('b'):
        p = ' '.join(p)
        lista = p.split()
        lista.pop()
        lista.pop()
        lista=''.join(lista)
        return lista, 'lb'

    elif p.endswith('g'):
        p = ' '.join(p)
        lista = p.split()
        lista.pop()
        lista.pop()
        lista=''.join(lista)
        return lista, 'kg'
    else:
        while True:
            input('Ingresa tu peso: ')
            
            if p.endswith('b'):
                p = ' '.join(p)
                lista = p.split()
                lista.pop()
                lista.pop()
                lista=''.join(lista)
                return lista, 'lb'

            elif p.endswith('g'):
                p = ' '.join(p)
                lista = p.split()
                lista.pop()
                lista.pop()
                lista=''.join(lista)
                return lista, 'kg'

print('Ingresa tu peso seguido de kg si es en kilos o lb si es libras.')

while True:
    print('¿Cuánto pesas?')
    
    peso = input()
    peso, comprobante = comprobarKgOLb(peso)

    if comprobante == 'lb':
        peso = int(peso)
        peso /= 2.205
        peso *= 35
        peso /= 1000

    elif comprobante == 'kg':
        peso = int(peso)
        peso *= 35
        peso /= 1000
    print()
    print('Debes consumir (%slitros) al día' % (peso))

    if not(jugarDeNuevo()):
        break



