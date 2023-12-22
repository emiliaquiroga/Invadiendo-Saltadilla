Juego hecho con Pygame para Laboratorio de Programación I. 
El juego es un remake del Space Invaders, donde Princesa debe derribar a las Chicas Superpoderosas (Bombón, Burbuja y Bellota), y esquivar sus ataques.
El juego cuenta con un menú inicial y, al finalizar, muestra el puntaje del jugador y en qué posición  en la tabla de puntajes se encuentra. 

El juego cuenta con sonidos cuando Princesa dispara lasers, mata a un enemigo, cuando es golpeada por algún laser, cuando es golpeada por un enemigo y cuando pierde.

El juego cuenta con niveles, arrancando desde el nivel 0 con unicamente 5 enemigos. Por cada nivel, se añaden 5 nuevos enemigos y su velocidad de movimiento aumenta. 
Cada nivel se supera matando a todos los enemigos, los mismos pueden ser esquivados pero volveran a aparecer nuevamente hasta ser eliminados o hasta que uno de sus disparos
le pegue a Princesa. 
El juego se pierde cuando Princesa se queda sin vida.
Como lo importante es la vida de Princesa, el sistema de Puntuación del Jugador funciona así:
- Si Princesa derriba un enemigo: +50 puntos
- Si el enemigo se choca con Princesa: - 15 puntos
- Si el enemigo pasa el alto de la pantalla de juego: -10 puntos
Los enemigos dispararán lasers, en caso de pegarle a Princesa, se le descontará vida a la misma.
Los puntajes son almacenados en una base de datos, utilizando sqlite3. Al momento de iniciar el programa, se valida la existencia previa de dicha base de datos:
en caso de NO existir previamente, se crea la base de datos; en caso de que la misma ya exista, los nuevos datos son agregados a la misma.


Updates que debería incluir: 
El juego no cuenta con un límite de niveles ni de puntuación, por lo que no se puede "Ganar", solo se puede obtener la puntuación mas alta en el registro de puntos.
Debería incluir algun limitante para esto.
Podría incluir un botón para silenciar los sonidos del juego.

