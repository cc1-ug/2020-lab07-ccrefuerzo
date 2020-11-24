[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3711160&assignment_repo_type=AssignmentRepo)

**Ejercicio #1: (Nombre del archivo: ejercicio1.py)**
Su profesor de Informatica le pide que haga un programa que encuentre si dos numeros son primos
relativos o no. Le recuerda que dos numeros son primos relativos, si el maximo factor comun
entre ellos es igual a 1. Para poder encontrar la solucion, su profesor le da la definicion de
la funcion que saca el maximo factor comun entre dos numeros, utilizando el Algoritmo de la
Division de Euclides:

```
  MFC(x,y) {
    IF y = 0 THEN
      RETURN x
    ELSE
      RETURN MFC(y, (x % y))
    END IF
  }
```

Utilizando esta funcion (implementandola con recursion), escriba otra funcion que reciba de parametro dos numeros y
devuelva mediante un boolean si son primos relativos o no. Se le provee el archivo **ejercicio1.py**
para que implemente su solucion, en el cual estan declaradas ambas funciones.
Este archivo provee un modo **autoevaluacion** para que pruebe su solucion.
  

**Ejercicio #2: (Nombre del archivo: ejercicio2.py)**
Su hermano esta llenando un album de estampitas de futbol y le cuenta que quiere utilizar un
programa para llevar el control de las que va obteniendo. Le propone que usted haga dicho
programa, y le pide uno que realice una version de prueba que cumpla con las siguientes
especificaciones:<br>

(1) Lleve el control de 100 estampitas (con numeros del 1 al 100)

(2) Despliegue el cuadro o lista (numeros desplegados horizontalmente separados por un guion ("-"), 10 por fila) de numeros de estampitas, con las estampitas que ya se tienen marcadas con una "X" (en vez del numero)

(3) Tenga un ciclo infinito en el cual se genere un numero de estampita aleatorio (entre 1 y 100). Si el numero ya tiene una "X" desplegar "ya tengo esta estampita", sino, marcar el numero con una "X" y volver a desplegar.

(4) Esperar a que el usuario de un ENTER para generar otro numero de estampita.

(5) Si el album ya esta lleno, desplegar "Album lleno" y ya no generar mas estampitas aleatorias