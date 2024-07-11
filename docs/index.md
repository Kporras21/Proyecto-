# Dinámica molecular en dos dimensiones: discos sólidos. 

El objetivo consiste en modelar el movimiento en el tiempo de $N$ cantidad de discos que se encuentran adentro de una caja de dos dimensiones y cuyo lado mide $1 (cm, m, mm, etc)$. Los discos pueden colisionar entre ellos o con las paredes de la caja. 


Para ello se implementó código orientado a objetos en Python. A continuación se detallarán las dos clases principales del código. 

## Class Disco 
* Esta clase cuenta con tres métodos principales:
  - move(self, dt)
  - check\_wall\_collision(self, width, height)
  - check\_disk\_collision(self, other\_disk)

### move(self, dt)
En este método se utilizó el método de Euler para resolver las ecuaciones de movimiento tanto para el eje $x$ como para el eje $y$, dichas ecuaciones son: 

$$
x = v_{x}t  
$$

$$
y = v_{y}t
$$

Posteriormente, se guardan las posiciones en arrays. 

### check\_wall\_collision(self, width, height)
Este método comprueba que el disco colisionó con la pared, para ello se utilizan las siguientes ecuaciones:

$$
x - r \leq \frac{-l}{2}
$$

$$
x + r \geq \frac{l}{2}
$$

$$
y - r \leq \frac{-l}{2}
$$

$$
y + r \geq \frac{l}{2}
$$

donde $l$ es lado de la caja y $r$ el radio del disco.


Si cualquiera de las ecuaciones anteriores se cumple, se invierte el signo de la velocidad, es decir, $-v_{x}$ y $-v_{y}$ según la conservación de momento lineal ya que se consideran colisiones elásticas.

### check\_disk\_collision(self, other\_disk)
Este método comprueba la colisión entre discos utilizando la distancia entre los centros de los discos, es decir

$$
d = \sqrt{dx^2 + dy^2}
$$

donde

$$
dx = x_{1} - x_{2}
$$

y

$$
dy = y_{1} - y_{2}
$$

donde el subíndice $1$ o $2$ indica disco 1 o disco 2 respectivamente.


Si se cumple que

$$
d < r_{1} + r_{2}
$$

existe una colisión y se toma en cuenta una relocidad relativa dada por

$$
v_{xrelativa} =  v_{x1} - v_{x2}
$$

$$
v_{yrelativa} =  v_{y1} - v_{y2}
$$

y se invierten las posiciones de los discos, es decir, $-x_{1}$, $-x_{2}$, $-y_{1}$ y $-y_{2}$.

## Class DiscoSimulation 
* Esta clase cuenta con tres métodos principales:
  - disk\_creation(self)
  - animate\_movement(self)
  - get\_positions(self)

### disk\_creation(self) 
Este método inicializa las posiciones y velocidades iniciales de cada disco utilizando la función $random$ y la clase Disco (también inicializa el color del disco). Por otro lado, calcula la distancia entre discos y verifica si hay o no colisión entre discos.

### animate\_movement(self)
Este método le da las características de circulo a cada disco, es decir, toma en cuenta que cada disco cubre un porcentaje de área en toda la caja. Por otro lado, crea la animación y le da movimiento a los discos con forme avanza el tiempo. Utiliza los métodos de la clase Disco para animar la colisón con pared y con otro disco.

### get\_positions(self)
Este método guarda las posiciones en el eje x y en el eje y de cada disco en listas.

## Funciones fuera de las clases. 
Además de utilizar clases, se crearon diversas funciones independientes para...


                                                                                                                                                                                                                                                                                                                                                                                              18,1     Comienzo



 












  
