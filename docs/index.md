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
x = x_{0} + v_{x}t  
$$

$$
y = y_{0} + v_{y}t
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
y - r \leq \frac{-a}{2}
$$

$$
y + r \geq \frac{a}{2}
$$

donde $l$ es largo de la caja, $a$ es el alto y $r$ el radio del disco.


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
v_{yrelativa} =  v_{y1} - v_{y2}.
$$


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
Además de utilizar clases, se crearon diversas funciones independientes para obtener el tipo de evento màs probable a suceder en un tiempo $t$ y para visualizar un histograma. 

## Evento más probable a suceder. 
La idea de esta parte es obtener cuál es el evento más probable a suceder para determinado disco, es decir, a partir del tiempo inicial, qué evento sucede primero, ya sea colisión con pared o colisión con otro disco. Para ello se crearon tres funciones que se detallan a continuación.

### time\_to\_wall\_collision(disk, width, height)
Esta función calcula el tiempo mínimo en el cual un disco colisiona con alguna pared de la caja. Para ello se implementaron las siguientes condiciones: 


Si $v_{x} > 0$ (el disco se mueve hacia la derecha), entonces:

$$
t_{xmin} = \frac{\frac{l}{2}-r-x}{v_{x}}.
$$ 

Si $v_{x} < 0$ (el disco se mueve hacia la izquierda), entonces:

$$
t_{xmin} = \frac{\frac{-l}{2}+r-x}{v_{x}}.
$$

Si $v_{y} > 0$ (el disco se mueve hacia arriba), entonces:  

$$
t_{ymin} = \frac{\frac{a}{2}-r-y}{v_{y}}.
$$

Si $v_{y} < 0$ (el disco se mueve hacia abajo), entonces:

$$
t_{ymin} = \frac{\frac{-a}{2}+r-y}{v_{y}}.
$$

Donde $l$ es el largo de la caja, $a$ es el ancho de la caja y $r$ el radio del disco. 

### time\_to\_disk\_collision(disk1, disk2)
Esta función calcula el tiempo mínimo en el cual un disco colisiona con otro. Para ello se trabaja con cálculo de vectores. Obteniendo: 

$$
\vec{R_{rel}} = (x_{1} - x_{2}, y_{1} - y_{2}, ... )
$$ 

vector relativo entre los centros de los discos. 

$$
\vec{V_{rel}} = (v_{x1} - v_{x2}, v_{y1} - v_{y2}, ... )
$$

vector relativo entre las velocidades de los discos. 

De esta manera se pueden aplicar condiciones para saber qué evento sucederá: 


Si $\sqrt{\vec{V_{rel}}^2} = 0$ los discos están en movimiento paralelo sin posibilidad de colisión. 


Si este no es el caso, entonces se requiere saber el tiempo en el cual existe una colisión. Dicho tiempo se puede calcular de la siguiente manera: 

$$
\vec{R_{rel}}^2 = \vec{R_{sum}}^2
$$

donde 

$$
\vec{R_{sum}}^2 = (r_{1} + r_{2})^2 = \vec{R_{rel}} \cdot \vec{R_{rel}}
$$

y, según ecuaciones de cinemática, 

$$
\vec{R_{rel}} = \vec{R_{rel0}} + t\vec{V_{rel}}.
$$
 
Por lo tanto, 

$$
\vec{R_{sum}}^2 = (\vec{R_{rel0}} + t\vec{V_{rel}}) \cdot  (\vec{R_{rel0}} + t\vec{V_{rel}})
$$

$$
\vec{R_{sum}}^2 = \vec{R_{rel0}} \cdot \vec{R_{rel0}} + 2t(\vec{R_{rel0}} \vec{V_{rel}}) + t^2(\vec{V_{rel}} \cdot \vec{V_{rel}})
$$

donde $(\vec{R_{rel0}} \cdot \vec{R_{rel0}}) = \vec{R_{rel}}^2$, $\vec{R_{rel0}} \cdot \vec{V_{rel}} = \vec{R_{rel}} \cdot \vec{V_{rel}}$ y $\vec{V_{rel}} \cdot \vec{V_{rel}} = \vec{V_{rel}}^2$. 

De esta manera se obtiene una ecuación cuadrática de la forma 

$$
at^2 + bt + c
$$

donde se define $a = \sqrt{\vec{V_{rel}}}$, $b = 2(\vec{R_{rel}} \cdot \vec{V_{rel}})$ y $c = \sqrt{\vec{R_{rel}}} - (r_{1} + r_{2})^2$.

De esta ecuación, se obtienen resultados con el discriminante. 


Si $\Delta < 0$ no existe colisión. 

Si $\Delta = 0$ los discos colisionan en un único punto.


Si $\Delta > 0$ hay dos momentos en los que los discos podrían colisionar en el futuro (de aquí la necesidad de buscar el tiempo mínimo para obtener el tiempo más pequeño).


De esta forma se obtiene el tiempo dado por:

$$
t = \frac{-b-\sqrt{\Delta}}{2a}
$$

### determine\_collision\_event(disks, width, height)
En esta función se define cuál es el evento más próximo a suceder entre una colisión con pared y una colisión entre discos. Implementa las funciones anteriores, de esta manera obtiene un tiempo para cada evento y utiliza el menor tiempo de estos.

# Resultado Discos.py

$$
KEVIN PONE AQUÍ EL RESULTADO DE LOS DISCOS, TAMBIÉN EN REFERENCE
$$

# Histograma 
Para realizar el histograma de la posición en x de los discos se crearon dos archivos .py, $mk\_csv-py$ y $mk\_histogram.py$

## mk\_csv.py

### guardar\_lista\_en\_csv(lista, nombre\_archivo)

## mk\_histogram.py  

# Resultado Histograma

$$
KEVIN PONÉ AQUÍ LA IMAGEN DEL HISTOGRAMA, TAMBIÉN EN REFERENCE 
$$
