# Producto-de-Unidad-2-Chanchay-Lema-Zurita

## 1.Planteamiento del Problema
Identificar, Investigar y llevar a la práctica una interfaz gráfica en Node-Red y una Calculadora Científica con POO(Programacion orientada a objetos) esto en una Raspberry Pi

## 2.Objetivos
- **General**
     - Diseñar programas funcionales para las plataformas o dispositivos Node-Red y Raspberry pi.
   - **Específicos**
     - Aplicar conceptos de programación orientada a objetos mediante la creación de un programa funcional en python que sea corrido en una Raspberry pi.
     - Implementar una calculadora científica en una raspberry pi agregando controles mediante el puerto GPIO y programación orientada a objetos.
     - Crear una interfaz humano máquina mediante Node-Red.
     
## 3.Estado del Arte
![](img/1.png)
![](img/2.png)
![](img/3.png)

En lo que respecta a nuestro Producto de Unidad cada una de estas investigaciones tienen su aportación pero estas deberán ser analizadas desde 2 perspectivas distintas.
 -Respecto al ámbito educativo Raspberry es un dispositivo con el cual podemos aprender acerca de distintas materias dentro de la computación como lo seria programacion o robotica a un bajo costo.
 - Herramientas como Raspberry o Node-Red no solamente nos son útiles para aprender, sino nos pueden ayudar  a solucionar problemas reales como lo son el control de tráfico de una ciudad y no solo solucionarlos, sino darles un valor agregado como lo es agregar IoT con Raspberry o plataformas de recopilación de datos visuales mediante Node-Red.
 
## 4.Marco Teórico
### Node-Red

### Raspberry Pi
#### ¿Qué es Raspberry y para qué sirve? 
Raspberry Pi, es un «es un ordenador de tamaño de tarjeta de crédito que se conecta a su televisor y un teclado». Es una placa que soporta varios componentes necesarios en un ordenador común.«Es un pequeño ordenador capaz, que puede ser utilizado por muchas de las cosas que su PC de escritorio hace, como hojas de cálculo, procesadores de texto y juegos. También reproduce vídeo de alta definición», apuntan en la página web del producto.
Este proyecto fue ideado en 2006 pero no fue lanzado al mercado en febrero de 2012. Ha sido desarrollado por un grupo de la Universidad de Cambridge y su misión es fomentar la enseñanza de las ciencias de la computación a los niños. De hecho, en enero de este año Google donó más de 15.000 Raspberry Pi para colegios en Reino Unido.
Es un ordenador muy funcional y debido a su tamaño puede funcionar para muchos otros propósitos, claro, hay que tener algunas ideas sobre programación o de computación. Por ejemplo, el primer proyecto de un joven con Raspberry Pi fue convertir su consola NES dañada en una operativa y pudo jugar algunos viejos títulos.
**Componentes del Raspberry Pi 4**
-Características de la Raspberry Pi 4 Broadcom BCM2711, Cortex núcleo cuádruple-A72 (ARM v8) 64-bit SoC @ 1.5GHz 
- SDRAM LPDDR4-2400 de 1 GB, 2 GB, 4 GB y 8 GB (según el modelo) 
- 2,4 GHz y 5,0 GHz IEEE 802.11ac inalámbrico, Bluetooth 5.0, BLE 
- Gigabit Ethernet 2 puertos USB 3.0; 2 puertos USB 2.0. 
- Cabezal GPIO estándar de 40 pines de Raspberry Pi (totalmente compatible con las placas anteriores) 
- 2 × puertos micro-HDMI (soportados hasta 4kp60) 
- Puerto de pantalla MIPI DSI de 2 vías 
- Puerto de cámara MIPI CSI de 2 carriles 
- Puerto de audio estéreo de 4 polos y de vídeo compuesto H.265 (decodificación 4kp60) 
- H264 (decodificación 1080p60, decodificación 1080p30) 
- Gráficos OpenGL ES 3.0 
- Ranura para tarjetas Micro-SD para cargar el sistema operativo y el almacenamiento de datos 
- 5V DC a través de conector USB-C (mínimo 3A*) 
- 5V DC vía cabezal GPIO (mínimo 3A*)
- Alimentación a través de Ethernet (PoE) habilitada (requiere PoE HAT separado) 
- Temperatura de funcionamiento: 0 – 50 grados C ambiente
#### ¿Que es GPIO?
General Purpose Input Output (GPIO) es un sistema de entrada y salida de propósito general, es decir, consta de una serie de pines o conexiones que se pueden usar como entradas o salidas para múltiples usos. Estos pines están incluidos en todos los modelos de Raspberry Pi aunque con diferencias.

![](img/4.png)

- Amarillo (2): Alimentación a 3.3V.
- Rojo (2): Alimentación a 5V.
- Naranja (26): Entradas / salidas de proposito general. Pueden configurarse como entradas o salidas. Ten presente que el nivel --alto es de 3.3V y no son tolerantes a tensiones de 5V.
- Gris (2): Reservados.
- Negro (8): Conexión a GND o masa.
- Azul (2): Comunicación mediante el protocolo I2C para comunicarse con periféricos que siguen este protocolo.
- Verde (2): Destinados a conexión para UART para puerto serie convencional.
- Morado (5): Comunicación mediante el protocolo SPI para comunicarse con periféricos que siguen este protocolo.

#### Programación orientada a objetos (POO)
La programación orientada a objetos es un paradigma de programación en que los programas son vistos como formados por entidades llamadas objetos que recuerdan su propio estado y que se comunican entre sí mediante el paso de mensajes que se intercambian con la finalidad de:cambiar sus estados internos,compartir información ,solicitar a otros objetos el procesamiento de dicha información (Lopez,2020)
Algunos conceptos basicos de POO son: 
- Clase
Definiciones de las propiedades y comportamiento de un tipo de objeto concreto. La instanciación es la lectura de estas definiciones y la creación de un objeto a partir de ellas.
- Objeto
Instancia de una clase. Entidad provista de un conjunto de propiedades o atributos (datos) y de comportamiento o funcionalidad (métodos), los mismos que consecuentemente reaccionan a eventos. Se corresponden con los objetos reales del mundo que nos rodea, o con objetos internos del sistema (del programa). Es una instancia a una clase.
- Método
Algoritmo asociado a un objeto (o a una clase de objetos), cuya ejecución se desencadena tras la recepción de un “mensaje”. Desde el punto de vista del comportamiento, es lo que el objeto puede hacer. Un método puede producir un cambio en las propiedades del objeto, o la generación de un “evento” con un nuevo mensaje para otro objeto del sistema.
- Mensaje
Una comunicación dirigida a un objeto, que le ordena que ejecute uno de sus métodos con ciertos parámetros asociados al evento que lo generó
- Comportamiento
Está definido por los métodos o mensajes a los que sabe responder dicho objeto, es decir, qué operaciones se pueden realizar con él.
- Evento
Es un suceso en el sistema (tal como una interacción del usuario con la máquina, o un mensaje enviado por un objeto). El sistema maneja el evento enviando el mensaje adecuado al objeto pertinente. También se puede definir como evento la reacción que puede desencadenar un objeto; es decir, la acción que genera.
- Atributos
Características que tiene la clase
- Propiedad o atributo
Contenedor de un tipo de datos asociados a un objeto (o a una clase de objetos), que hace los datos visibles desde fuera del objeto y esto se define como sus características predeterminadas, y cuyo valor puede ser alterado por la ejecución de algún método.
- Estado interno
Es una variable que se declara privada, que puede ser únicamente accedida y alterada por un método del objeto, y que se utiliza para indicar distintas situaciones posibles para el objeto (o clase de objetos). No es visible al programador que maneja una instancia de la clase.
- Componentes de un objeto
Atributos, identidad, relaciones y métodos.
- Identificación de un objeto
Un objeto se representa por medio de una tabla o entidad que esté compuesta por sus atributos y funciones correspondientes.
#### POO en python
En python la POO se expresa de manera simple y fácil de escribir pero debes tener en cuenta que para programar debes entender cómo funciona la teoría de POO y aplicarla al código.
La teoría de la POO nos dice que todos los objetos deben pertenecer a una clase, ya que esta es la base para diferenciarse unos de otros teniendo atributos y comportamientos que los distingan de otros objetos que pertenezcan a otras clases, para crear clases en python lo hacemos de la siguiente manera:
class Auto():
Para definir un atributo simplemente creamos una variable con total normalidad y un valor cualquiera por dar:
class Auto():
    ruedas=4
Para definir un método lo hacemos igual como lo hacemos con una función con la palabra por defecto def y el nombre de dicho método pero para diferenciar un método de una función lo hacemos escribiendo dentro de sus paréntesis el parámetro self:
def desplazamiento(self):
    pass
La palabra self hace referencia a los objetos que pertenezcan a la clase y la palabra pass que colocamos dentro del método le indica a el intérprete de python que todavía no le hemos definido ningún funcionamiento a ese método.
Cuando tenemos nuestra clase lista ya podemos empezar a crear objetos que pertenezcan a esa clase, para crear objetos lo hacemos de la siguiente manera:

miVehiculo=Auto()

Para mostrar atributos:

miObjeto.atributo

Para mostrar métodos:

miObjeto.metodo()
  
Constructor __init__()
El método __init__() es un método especial, el cual se ejecuta al momento de instanciar un objeto. El comportamiento de __init__() es muy similar a los “constructores” en otros lenguajes. Los argumentos que se utilizan en la definición de __init__() corresponden a los parámetros que se deben ingresar al instanciar un objeto.

   def __init__(self, cedula, nombre, apellido, sexo):
   
Constructor de clase Persona
        
self.cedula = cedula
        
self.nombre = nombre
       
self.apellido = apellido
       
self.sexo = sexo

#### Compilador create.with.code.uk
Este compilador nace como un proyecto en el Reino Unido destinado a la enseñanza de programación en python para los niños ofreciendo una gran cantidad de herramientas, librerías y tutoriales sin la necesidad de tener que descargar nada en nuestra computadora.
Dentro de las herramientas que nos ofrece este compilador contamos con la de en emulador de puertos GPIO del raspberry pi usando únicamente la librería de python propia del uso de una GPIO RPi.GPIO.

![](img/5.png)

## 5.Diagramas
### Node-Red
### Calculadora científica programada con python para RaspberryPi
El siguiente diagrama muestra el esquema de conexión de una calculadora científica en Raspberry pi, esta esta calculadora contará con distintos los siguientes cálculos: 
Operaciones Básicas
**1.Funciones trigonométricas
2.Raíces,Potencias y Logaritmos
3.Valores Absolutos
4.Factorial
5.Operaciones Basicas
6.Funciones hiperbólicas**










