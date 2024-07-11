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
  - $x - r \leq \frac{-l}{2}$
  - $x + r \geq \frac{l}{2}$
  - $y - r \leq \frac{-l}{2}$
  - $y + r \geq \frac{l}{2}$

donde $l$ es lado de la caja y $r$ el radio del disco. 

### check\_disk\_collision(self, other\_disk)

 












  
