import os
import sys
import time
from Genen import Gen

MENU = f"""
 {Gen.WH}[{Gen.YE}1{Gen.WH}]{Gen.WH} Únicas M y A
 {Gen.WH}[{Gen.YE}2{Gen.WH}]{Gen.WH} Únicas m y A
 {Gen.WH}[{Gen.YE}3{Gen.WH}]{Gen.WH} Únicas M, m y A
 {Gen.WH}[{Gen.YE}4{Gen.WH}]{Gen.WH} Peronalizado
 \n {Gen.WH}Versión:{Gen.BL} {Gen.VER}
 {Gen.BL}Aleatorio: (A), Minúscula: (m), Mayúscula: (M)
"""

TE_1 = f"\n{Gen.YE} Cantidad de contraseñas (Obligatorio)"
TE_2 = f"{Gen.YE} Cantidad de digitos por clave (Obligatorio)"
TE_3 = f"{Gen.YE} Nombre del diccionario (Obligatorio)"
TE_4 = f"""
  {Gen.RE} Sección (Obligatoria)
  {Gen.WH}[{Gen.YE}1{Gen.WH}]{Gen.WH} Mayúsculas
  {Gen.WH}[{Gen.YE}2{Gen.WH}]{Gen.WH} Minusculas
  {Gen.WH}[{Gen.YE}3{Gen.WH}]{Gen.WH} Mayúsculas y Minusculas
\n  {Gen.WH}[{Gen.YE}00{Gen.WH}]{Gen.WH} Menú
"""
TE_5 = f"\n {Gen.YE} Intervalo de numeros minimi y maximo (4 o 0)"
TE_6 = f"\n {Gen.YE} Intervalo de letras minimo y maximo (4 o 0)"

def main():
    while True:
        try:
            os.system('clear')
            print(MENU)
            user = int(input(f'\n {Gen.WH}:{Gen.GR} '))
            match user:
                case 1:
                    while True:
                        try:
                            print(TE_1)
                            user_vs_op = int(input(f' {Gen.WH}:{Gen.GR} '))
                            print(TE_2)
                            user_ct_op = int(input(f' {Gen.WH}:{Gen.GR} '))
                            print(TE_3)
                            user_name = str(input(f' {Gen.WH}:{Gen.GR} '))
                            Gen.mayus_dict(user_name, user_ct_op, user_vs_op)
                            
                        except ValueError as e:
                            print("Opción no valida.", e)
                            continue

                case 2:
                    while True:
                        try:
                            print(TE_1)
                            user_vs_op = int(input(f' {Gen.WH}:{Gen.GR} '))
                            print(TE_2)
                            user_ct_op = int(input(f' {Gen.WH}:{Gen.GR} '))
                            print(TE_3)
                            user_name = str(input(f' {Gen.WH}:{Gen.GR} '))
                            Gen.minus_dict(user_name, user_ct_op, user_vs_op)

                        except ValueError as e:
                            print("Opción no valida.", e)
                            continue
                    
                case 3:
                    while True:
                        try:
                            print(TE_1)
                            user_vs_op = int(input(f' {Gen.WH}:{Gen.GR} '))
                            print(TE_2)
                            user_ct_op = int(input(f' {Gen.WH}:{Gen.GR} '))
                            print(TE_3)
                            user_name = str(input(f' {Gen.WH}:{Gen.GR} '))
                            Gen.minus_and_mayus_dict(user_name, user_ct_op, user_vs_op)

                        except ValueError as e:
                            print("Opción no valida.", e)
                            continue

                case 4:
                    while True:
                        try:
                            us_m = None
                            print(TE_4)
                            mus = int(input(f"\n: "))
                            match mus:
                                case 1:
                                    us_m = "M"
                                case 2:
                                    us_m = "m"
                                case 3:
                                    us_m = "Mym"
                                case 00:
                                    break
                                case _:
                                    print(f' Opcion no valida.')
                                    time.sleep(2)
                                    continue

                            print(TE_3)
                            us_dc = input(f" {Gen.WH}:{Gen.GR} ")
                            print(TE_1)
                            us_ca = int(input(f" {Gen.WH}:{Gen.GR} "))
                            print(TE_2)
                            us_di = int(input(f" {Gen.WH}:{Gen.GR} "))
                            print(TE_5)
                            us_ima = str(input(f" {Gen.WH}:{Gen.GR} "))
                            print(TE_6)
                            us_la = str(input(f" {Gen.WH}:{Gen.GR} "))

                            #verificador de datos
                            pases = True
                            DTS = [[str(us_ca), "int"], [str(us_di), "int"], [us_ima, "int"], [us_la, "int"]]
                            for x in DTS:
                                while True:
                                    asp = Gen.verdat(x[0], x[1])
                                    
                                    if asp[1] == False:
                                        print(f"{Gen.RE} Error: valor no valido ({asp[0]}).")
                                        pases = False
                                        break

                                    else:
                                        break

                                if pases == False:
                                    break

                            if pases == False:
                                print(f"Volviendo al menú....")
                                sys.exit()#
                                time.sleep(1)
                                break

                            Gen.pers(us_ima, us_la, us_ca, us_di, us_dc, us_m)

                        except ValueError as e:
                            print(f' Opcion no valida {e}')
                            time.sleep(2)
                            continue

                        except KeyboardInterrupt:
                            print(f'\n {Gen.RE}Cerrando programa.')
                            sys.exit()

                case _:
                    print("Opción no valida.")
                    time.sleep(2)
                    continue

        except KeyboardInterrupt:
            print(f'\n {Gen.RE}Cerrando programa.')
            sys.exit()

        except ValueError as ops:
            print(f' Opcion no valida {ops}')
            time.sleep(2)
            continue

if __name__ == '__main__':
    main()
