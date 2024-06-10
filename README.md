# Jogo_do_NIM

No Jogo do NIM, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.

A estratégia para ganhar o jogo consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.

Considerando dois cenários: 

Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"
Caso contrário, o computador toma a iniciativa de começar o jogo, declarando "Computador começa!"

A estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, será tirado o número máximo de peças possíveis.
