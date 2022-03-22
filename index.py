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
            print('¿Cuánto pesas?')
            p = input()
            
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
        vaso = peso / 250
        peso /= 1000

    elif comprobante == 'kg':
        peso = int(peso)
        peso *= 35
        vaso = peso / 250
        peso /= 1000

    pagina = 'https://www.google.com/search?q=vasos+de+250+ml&source=lmns&bih=667&biw=1264&client=opera&hl=es-419&sa=X&ved=2ahUKEwi8lfPOvdr2AhXGXDABHVTLCmAQ_AUoAHoECAEQAA'
    
    print('\nAporximadamente debes consumir "%s litros" de agua al día, o "%s vasos de 250ml" al día.' % (peso, vaso))
    print("\nVistia la siguiente página para ver como son los vasos.\n%s" % (pagina))
    if not(jugarDeNuevo()):
        break
