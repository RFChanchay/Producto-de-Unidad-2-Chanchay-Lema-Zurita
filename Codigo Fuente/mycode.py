#PROGRAMA CALCULADORA
import math
import RPi.GPIO as GPIO
class CalcuCientifica():#CLACES QUE CONTIENE A LA CALCULADORA EN GENERAL
    resultado=0#ATRIBUTO
    def __init__(self,resultado):#CONSTRUCTOR
        self.resultado=resultado
# menu general del programa
    def menu(self):
        print("Calculadora Cientifica")
        print("---------------------------------------------")
        print("Para la seleccion de funciones use los interruptores unicamente  activado 1 a la vez, despues pulse enter")
        print("Para el ingreso de numeros use el teclado, despues pulse enter                                            ")
        print("----------------------------------------------")
        print("1: Operaciones Basicas\n2: Funciones trigonometricas\n3: Raices,Potencias y Logaritmos\n4: Otros")
        vacio=input()#VARIABLE VACIA PARA RECIBIR UN ENTER Y PASAR A LA SIGUIENTE INSTRUCCION
        seleccion=self.pinSelector()#LLAMADO A LA FUNCION SELECTOR DE PIN PARA LEER EL GPIO
        #SELECTOR DE CASOS PARA DIRIGIRSE A UN SUBMENU
        if seleccion==1:
            self.basicas()
        elif seleccion==2:
            self.trigonometricas()
        elif seleccion==3:
            self.racExpLog()
        elif seleccion==4:
            self.otros()
        else:
            print("Opcion no valida")
            self.menu()

#Seccion de operaciones basicas
    def basicas(self):
        print("Basicas")
        print("Seleccione opcion a realizar: ")
        print("1: Suma\n2: Resta\n3: Multiplicacion\n4: Division")
        vacio=input()#VARIABLE VACIA PARA RECIBIR UN ENTER Y PASAR A LA SIGUIENTE INSTRUCCION
        selBas=self.pinSelector()#LLAMADO A LA FUNCION SELECTOR DE PIN PARA LEER EL GPIO
        if selBas==1:
            self.suma()
        elif selBas==2:
            self.resta()
        elif selBas==3:
            self.multipli()
        elif selBas==4:
            self.division()
        else:
            print("Opcion no valida")
            self.basicas()
#PARA LAS OPERACIONES BASICAS SE PEDIRAN 2 NUMEROS A OPERAR Y EL RESULTADO SE ALMACENARA E IMPRIMIRA
    def suma(self):
        print("Ingrese el primer numero")
        num1=float(input())
        print("Ingrese el segundo numero")
        num2=float(input())
        resultado=num1+num2
        print(num1,'+',num2,'=',resultado)
    def resta(self):
        print("Ingrese el minuendo")
        num1=float(input())
        print("Ingrese el sustraendo")
        num2=float(input())
        resultado=num1-num2
        print(num1,'-',num2,'=',resultado)
    def multipli(self):
        print("Ingrese el primer numero")
        num1=float(input())
        print("Ingrese el segundo numero")
        num2=float(input())
        resultado=num1*num2
        print(num1,'*',num2,'=',resultado)
    def division(self):
        print("Ingrese el dividendo")
        num1=float(input())
        print("Ingrese el divisor")
        num2=float(input())
        resultado=num1/num2
        print(num1,'/',num2,'=',resultado)

#seccion funciones trigonometricas

    def trigonometricas(self):
        print("Trigonometricas")
        print("Seleccione tipo de funcion trigonometrica: ")
        print("1: SENO\n2: COSENO\n3: TANGENTE\n4: ARCOSENO\n5: ARCOCOSENO\n6: ARCOTANGENTE")
        vacio=input()#VARIABLE VACIA PARA RECIBIR UN ENTER Y PASAR A LA SIGUIENTE INSTRUCCION
        seltri=self.pinSelector()#LLAMADO A LA FUNCION SELECTOR DE PIN PARA LEER EL GPIO
        #CASOS PARA REALIZAR DISTINTAS FUNCIONES TRIGONOMETRICAS
        if seltri==1:
            self.seno()
        elif seltri==2:
            self.coseno()

        elif seltri==3:
            self.tangente()

        elif seltri==4:
            self.arcoseno()

        elif seltri==5:
            self.arcocoseno()

        elif seltri==6:
            self.arcotangente()

        else:
            print("Opcion no valida")
            self.trigonometricas()

    #PARA LAS FUNCIONES TRIGONOMETRICAS SE SOLICITAR UN UNICO VALOR DE ANGULO O X A ENCONTRAR Y SE LO ALMACENARA EN UNA VARIABLE LLAMADA ANGULO
    def seno(self):
        print("Seno(x)")
        print("Ingrese el valor del angulo x en radianes")
        angulo=float(input())
        resultado=math.sin(angulo)
        print("El seno de ",angulo," es: ",resultado)
    def coseno(self):
        print("Coseno(x)")
        print("Ingrese el valor del angulo x en radianes")
        angulo=float(input())
        resultado=math.cos(angulo)
        print("El coseno de ",angulo," es: ",resultado)
    def tangente(self):
        print("Tangente(x)")
        print("Ingrese el valor del angulo x en radianes")
        angulo=float(input())
        resultado=math.tan(angulo)
        print("La tangente de ",angulo," es: ",resultado)
    def arcoseno(self):
        print("ArcoSeno(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.asin(angulo)
        print("El arcoseno de ",angulo," es el angulo: ",resultado," rad")
    def arcocoseno(self):
        print("ArcoCoseno(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.acos(angulo)
        print("El arcocoseno de ",angulo," es el angulo: ",resultado," rad")
    def arcotangente(self):
        print("ArcoTangente(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.atan(angulo)
        print("La arcotangente de ",angulo," es el angulo: ",resultado," rad")


#seccion raices exponentes y logaritmos
    def racExpLog(self):
        print("Raices,Potencias y Logaritmos")
        print("Seleccione tipo de operacion: ")
        print("1: Raiz\n2: Potencia\n3: Logaritmo")
        vacio=input()#VARIABLE VACIA PARA RECIBIR UN ENTER Y PASAR A LA SIGUIENTE INSTRUCCION
        selRacExpLog=self.pinSelector()#LLAMADO A LA FUNCION SELECTOR DE PIN PARA LEER EL GPIO
        if selRacExpLog==1:
            self.raices()
        elif selRacExpLog==2:
            self.potencia()
        elif selRacExpLog==3:
            self.logaritmos()
        else:
            print("Opcion no valida")
            self.racExpLog()

    #PARA RAICES SE SOLICITARA RADICANDO E INDICE PARA REALIZAR LA OPERACION 
    def raices(self):
        print("Raices")
        print("Ingrese el indice")
        indice=int(input())
        print("Ingrese el radicando")
        radicando=float(input())
        resultado=radicando**(1/indice)
        print("La respuesta de esa raiz es: ",resultado)
    #PARA POTENCIAS SE SOLICITARA BASE Y EXPONENTE PARA REALIZAR LA OPERACION 
    def potencia(self):
        print("Potencias")
        print("Ingrese la base")
        base=float(input())
        print("Ingrese el exponente")
        exponente=int(input())
        resultado=base**exponente
        print("La respuesta de la potencia es: ",resultado)
    #PARA LOS LOGARITMOS PRIMERO SE DEBE ELEGIR EL TIPO DE BASE A OPERAR YA SEA NATURAL O EULER
    #PARA LAS BASES NATURALES SE SOLICITARA EL VALOR DE LA BASE
    #PARA LA BASE EULER UNICAMENTE SE SOLICITARA EL ARGUMENTO
    def logaritmos(self):
        print("Logaritmos")
        print("Seleccione el tipo de Logaritmo")
        print("1: Logaritmo Decimal\n2: Logaritmo Natural")
        vacio=input()#VARIABLE VACIA PARA RECIBIR UN ENTER Y PASAR A LA SIGUIENTE INSTRUCCION
        selecLog=self.pinSelector()
        if selecLog==1:
            self.logB()
        elif selecLog==2:
            self.logNat()
        else:
            print("Opcion no valida")
            self.logaritmos()
    def logB(self):
        print("Logaritmos decimales")
        print("Ingrese la base:")
        base=int(input())
        print("Ingrese el argumento:")
        argumento=float(input())
        resultado=math.log(argumento,base)
        print("El logaritmo base ",base," de ",argumento," es: ",resultado)

    def logNat(self):
        print("Logaritmos naturales")
        print("Ingrese el argumento")
        argumento=float(input())
        resultado=math.log(argumento,math.e)
        print("El logaritmo natural de",argumento," es: ",resultado)


#seccion de operaciones
    def otros(self):
        print("Otras operaciones")
        print("Seleccione la opcion a realizar")
        print("1:Factorial de un numero\n2:Valor Absoluto de un numero\n3:Funciones Hiperbolicas")
        vacio=input()#VARIABLE VACIA PARA RECIBIR UN ENTER Y PASAR A LA SIGUIENTE INSTRUCCION
        selecOtros=self.pinSelector()#LLAMADO A LA FUNCION SELECTOR DE PIN PARA LEER EL GPIO
        if selecOtros==1:
            self.factorial()
        elif selecOtros==2:
            self.vabsoluto()
        elif selecOtros==3:
            self.hiperbolicas()
        else:
            print("Opcion no valida")
            self.otros()
    #PARA EL NUMERO FACTORIAL SE SOLICITARA AL USUARIO INGRESAR UN VALOR ENTERO UNICAMENTE
    def factorial(self):
        print("Factorial")
        print("Ingrese el numero")
        numerof=int(input())
        resultado=math.factorial(numerof)
        print("El factorial de ",numerof," es ",resultado)
    #PARA EL VALOR ABSOLUTO SE SOLICITARA UN NUMERO CUALQUIERA
    def vabsoluto(self):
        print("Valor Absoluto")
        print("Ingrese el numero")
        numero=float(input())
        resultado=math.fabs(numero)
        print("El valor absoluto de ",numero," es ",resultado)
    #PARA LAS FUNCIONES HIPERBOLICAS SE SOLICITAR UN VALOR X A ENCONTRAR Y SE LO ALMACENARA EN UNA VARIABLE LLAMADA ANGULO
    def hiperbolicas(self):
        print("Funciones hiperbolicas")
        print("Seleccione tipo de funcion hiperbolica: ")
        print("1: SENO HIPERBOLICO\n2: COSENO HIPERBOLICO\n3: TANGENTE HIPERBOLICA")
        print("4: ARCOSENO HIPERBOLICO \n5: ARCOCOSENO HIPERBOLICO\n6: ARCOTANGENTE HIPERBOLICA")
        vacio=input()#VARIABLE VACIA PARA RECIBIR UN ENTER Y PASAR A LA SIGUIENTE INSTRUCCION
        selecHiper=self.pinSelector()#LLAMADO A LA FUNCION SELECTOR DE PIN PARA LEER EL GPIO
        #CASOS PARA CADA FUNCION
        if selecHiper==1:
            self.senoh()
        elif selecHiper==2:
            self.cosenoh()

        elif selecHiper==3:
            self.tangenteh()

        elif selecHiper==4:
            self.arcosenoh()

        elif selecHiper==5:
            self.arcocosenoh()

        elif selecHiper==6:
            self.arcotangenteh()

        else:
            print("Opcion no valida")
            self.hiperbolicas()

    def senoh(self):
        print("Senh(x)")
        print("Ingrese el valor de x")
        angulo=float(input())
        resultado=math.sinh(angulo)
        print("El seno hiperbolico de ",angulo," es: ",resultado)
    def cosenoh(self):
        print("Cosh(x)")
        print("Ingrese el valor de x")
        angulo=float(input())
        resultado=math.cosh(angulo)
        print("El coseno hiperbolico de ",angulo," es: ",resultado)
    def tangenteh(self):
        print("Tanh(x)")
        print("Ingrese el valor de x")
        angulo=float(input())
        resultado=math.tanh(angulo)
        print("La tangente hiperbolica de ",angulo," es: ",resultado)
    def arcosenoh(self):
        print("ArcSenh(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.asinh(angulo)
        print("El arcoseno hiperbolico de ",angulo," es: ",resultado)
    def arcocosenoh(self):
        print("ArcCosh(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.acosh(angulo)
        print("El arcocoseno hiperbolico de ",angulo," es: ",resultado)
    def arcotangenteh(self):
        print("ArcTanh(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.atanh(angulo)
        print("La arcotangente hiperbolica de ",angulo," es: ",resultado)

    #funciones para raspberry
    #FUNCION PARA INICIAR LOS PUERTOS GPIO COMO ENTRADAS
    def iniciarGPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3,GPIO.IN)
        GPIO.setup(5,GPIO.IN)
        GPIO.setup(7,GPIO.IN)
        GPIO.setup(11,GPIO.IN)
        GPIO.setup(13,GPIO.IN)
        GPIO.setup(15,GPIO.IN)
        
    #FUNCION PARA CONTROLAR LOS PINES ACTIVOS 
    def pinSelector(self):

        seleccionador=0
        #CADA PIN ACTIVO SERA UNA VARIABLE LOGICA QUE SE REGISTRA EN UNA TABLA DE VERDAD
        #LA VARIABLE SELECCIONADOR GUARDARA EL ESTADO EN EL QUE  TODOS LOS PINES ESTAN MEDIANTE NUMEROS ENTEROS ASIGNADOS
        #ESTOS NUMEROS SON ASIGNADOS SEGUN LOS BALORES BINARIOS MSI Y LSI PARA CADA PIN
        #PIN 3=1
        #PIN 5=2
        #PIN 7=4
        #PIN 11=8
        #PIN 13=16
        #PIN 15=32

        if GPIO.input(3) == GPIO.HIGH:
            seleccionador= seleccionador+1
        if GPIO.input(5) == GPIO.HIGH:
            seleccionador= seleccionador+2
        if GPIO.input(7) == GPIO.HIGH:
            seleccionador= seleccionador+4
        if GPIO.input(11) == GPIO.HIGH:
            seleccionador= seleccionador+8
        if GPIO.input(13) == GPIO.HIGH:
            seleccionador= seleccionador+16
        if GPIO.input(15) == GPIO.HIGH:
            seleccionador= seleccionador+32
        
        #AQUI SE DETECTA LOS CASOS EN LOS QUE NO HAY PINES QUE RECIBAN UNA SENAL LOGICA O QUE 2 O MAS RECIBAN UNA SENAL LOGICA
        #SI SE RECIBE UNA UNICA SENAL LOGICA LA FUNCION RETORNARA EL TIPO DE SELECCION QUE SE LE ATRIBUYE AL MENU
        #SI NO RECIBE UNA UNICA SENAL LOGICA LA FUNCION RETORNARA UN VALOR ALTO QUE NINGUN MENU RECONOCERA
        if seleccionador == 1:
            return 1
        elif seleccionador == 2:
            return 2
        elif seleccionador == 4:
            return 3
        elif seleccionador == 8:
            return 4
        elif seleccionador == 16:
            return 5
        elif seleccionador == 32:
            return 6
        else:
            return 100
#PROGRAMA PRINCIPAL
#CREAMOS UN CICLO INFINITO QUE HARA QUE EL PROGRAMA SE REPITA CONSTANTEMENTE
while 1:
  calculo=CalcuCientifica(0)#INICIAMOS LA CLASE
  calculo.iniciarGPIO()#INICIAMOS LOS PUERTOS GPIO
  resultado=calculo.menu()#ATRIBUIMOS UN RESULTADO MEDIANTE LA FUNCION MENU
  

