import os
import time
import sys
import secrets


class Gen():
    #nota: arreglar lo de que las contraseñas se ponen en un orden de num let para que sea por turnos esta posicion entre ellos

    #nota: verificar la existencia de los diccionarios antes de haber creado las contraseñas 

    VER = "1.2"

    #colors
    RE = "\033[91m"
    BL = "\033[34m"
    GR = "\033[32m"
    YE = "\033[33m"
    MA = "\033[35m"
    GRA = "\033[90m"
    CY = "\033[36m"
    WH = "\033[37m"

    LET = ['a', 
           'b', 
           'c', 
           'd', 
           'e', 
           'f', 
           'g', 
           'h', 
           'i', 
           'j', 
           'k', 
           'l', 
           'm', 
           'n', 
           'o', 
           'p', 
           'q', 
           'r', 
           's', 
           't', 
           'u', 
           'v', 
           'w', 
           'x', 
           'y', 
           'z']
    pin = ''
    pins_M = set()
    pins_m = set()
    pins_mM = set()
    pps = set()

    ves_M = 0
    ves_m = 0
    ves_mM = 0
    sub_ve = 0
    con_num = 0
    con_let = 0

    def archivo_creat(pins_format, arch_name):
        os.system(f'touch {arch_name}')
        with open(arch_name, 'w') as file:        
            for a in pins_format:
                file.write(f'{a}\n')

            print(f'El diccionario a hacido creado exitosamente.')
            sys.exit()

    def mayus_dict(name, user_ct, user_vs):
        if os.path.exists(f'{name}_crt_{user_ct}_cont_{user_vs}.txt') == True:
            print(f'{Gen.RE} Diccionario ya existente {name}_crt_{user_ct}_cont_{user_vs}.txt')
            time.sleep(3)
            return
        
        print(f'{Gen.YE} Este proceso puede tardar algunos minutos, por favor sea paciente.')
        
        while True:
            if Gen.ves_M == user_vs:
                Gen.archivo_creat(Gen.pins_M, f'{name}_crt_{user_ct}_cont_{user_vs}.txt')
            
            for _ in range(0, user_ct):
                lup = secrets.choice([True, False])
                # Ordenes aleatorio
                match lup:
                    case True:
                        Gen.pin += str(secrets.randbelow(9))
                    
                    case False:# Siempre mayúsculas
                        Gen.pin += secrets.choice(Gen.LET).upper()
                
                if len(Gen.pin) == user_ct:
                    break

            if Gen.pin in Gen.pins_M:
                Gen.ves_M -= 1
                Gen.pin = ''
                continue
                
            Gen.pins_M.add(Gen.pin)
            Gen.ves_M += 1
            Gen.pin = ''

    def minus_dict(name, user_ct, user_vs):
        if os.path.exists(f'{name}_crt_{user_ct}_cont_{user_vs}.txt') == True:
            print(f'{Gen.RE} Diccionario ya existente {name}_crt_{user_ct}_cont_{user_vs}.txt')
            time.sleep(3)
            return
        
        print(f'{Gen.YE} Este proceso puede tardar algunos minutos, por favor sea paciente.')
        
        while True:
            if Gen.ves_m == user_vs:
                Gen.archivo_creat(Gen.pins_m, f'{name}_crt_{user_ct}_cont_{user_vs}.txt')
            
            for _ in range(0, user_ct):
                lup = secrets.choice([True, False])
                # Ordenes aleatorios
                match lup:
                    case True:
                        Gen.pin += str(secrets.randbelow(9))
                    
                    case False:# Siempre mayúsculas
                        Gen.pin += Gen.LET[secrets.randbelow(21)]

                if len(Gen.pin) == user_ct:
                    break

            if Gen.pin in Gen.pins_m:
                Gen.ves_m -= 1
                Gen.pin = ''
                continue

            Gen.pins_m.add(Gen.pin)
            Gen.ves_m += 1
            Gen.pin = ''

    def minus_and_mayus_dict(name, user_ct, user_vs):
        if os.path.exists(f'{name}_crt_{user_ct}_cont_{user_vs}.txt') == True:
            print(f'{Gen.red} Diccionario ya existente {name}_crt_{user_ct}_cont_{user_vs}.txt')
            time.sleep(3)
            return
        
        print(f'{Gen.YE} Este proceso puede tardar algunos minutos, por favor sea paciente.')
        
        while True:
            if Gen.ves_mM == user_vs:
                Gen.archivo_creat(Gen.pins_mM, f'{name}_crt_{user_ct}_cont_{user_vs}.txt')

            for _ in range(0, user_ct):
                lup = secrets.choice([True, False])
                # Ordenes aleatorio
                match lup:
                    case True:
                        Gen.pin += str(secrets.randbelow(9))
                    
                    case False:# Mayus o Minus Aleatorio
                        Gen.pin += Gen.numlet(False, "Mym")

            if Gen.pin in Gen.pins_mM:
                Gen.ves_mM -= 1
                Gen.pin = ''
                continue
            
            Gen.pins_mM.add(Gen.pin)
            Gen.ves_mM += 1
            Gen.pin = ''
            Gen.con_num = 0
            Gen.con_let = 0

    def numlet(os, m=None):
        if os == True:
            Gen.con_num += 1
            return secrets.randbelow(9)

        elif os == False:
            Gen.con_let += 1
            match m:
                case "M":
                    return secrets.choice(Gen.LET).upper()

                case "m":
                    return secrets.choice(Gen.LET)

                case "Mym":
                    match secrets.choice([False, True]):
                        case True:
                            return secrets.choice(Gen.LET)
                        
                        case False:
                            return secrets.choice(Gen.LET).upper()
    
    def pers(ima, la, ca, di, dc, m):
        if os.path.exists(f'{dc}_crt_{di}_cont_{ca}.txt') == True:
            print(f'{Gen.RE} Diccionario ya existente {dc}_crt_{di}_cont_{ca}.txt')
            time.sleep(3)
            return
        
        print(f'{Gen.YE} Este proceso puede tardar algunos minutos, por favor sea paciente.')

        idf = {"la": int(la.split()[0]) + int(la.split()[1]),
               "ima": int(ima.split()[0]) + int(ima.split()[1]),
                "tul": None,
                "pin": str()
                }
        
        if idf['ima'] + idf['la'] < di:
            print(f"{Gen.RE} Error: ", idf['ima'] + idf['la'])
            print(f"{Gen.RE} Los intervalos de numero o letras deben abarcar el intervalo")
            print(f"{Gen.RE} digitos por clave. Ej: num(1,4), let(7,4) para claves de 8 digitos.")
            input(f"{Gen.GR} Enter para volver al menú...")
            return
        
        while True:
            try:
                idf['tul'] = secrets.choice([True, False])

                if len(idf['pin']) == di:
                    Gen.pps.add(idf['pin'])
                    idf['pin'] = str()
                    Gen.con_num = 0
                    Gen.con_let = 0
                
                if len(Gen.pps) == ca:
                    Gen.archivo_creat(Gen.pps, f'{dc}_crt_{di}_cont_{ca}.txt')

                match idf['tul']:
                    case True:
                        if Gen.con_let >= int(la.split()[1]):
                            idf['pin'] += str(Gen.numlet(True))
                            continue

                        idf['pin'] += Gen.numlet(False, m)
                    
                    case False:
                        if Gen.con_num >= int(ima.split()[1]):
                            idf['pin'] += Gen.numlet(False, m)
                            continue

                        idf['pin'] += str(Gen.numlet(True))

                if len(idf['pin']) == di:# verificador de caracteres por clave
                    if idf['pin'] in Gen.pps:
                        idf['pin'] = str()
                        Gen.con_num = 0
                        Gen.con_let = 0
                        continue

                    Gen.pps.add(idf['pin'])
                    idf['pin'] = str()
                    Gen.con_num = 0
                    Gen.con_let = 0

                if len(Gen.pps) == ca:
                    Gen.archivo_creat(Gen.pps, f'{dc}_crt_{di}_cont_{ca}.txt')

            except KeyboardInterrupt:
                pass

    def verdat(dat, type):
        match type:
            case "int":
                for nul in dat.split():
                    print(nul)
                    for sd in nul:
                        try:
                            a = int(sd)
                        except ValueError:
                            return [dat, False]
                return [dat, True]
            
            case "str":
                for nul in dat.split():
                    print(nul)
                    for sd in nul:
                        try:
                            a = int(nul)
                        except ValueError:
                            return [dat, False]
                return [dat, True]
