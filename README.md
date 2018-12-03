# Math-Bot
**Math-Bot** é um bot calculadora para Telegram. É simples de usar e fornece versatilidade, além de conter ferramentas úteis para as necessidades diárias (como conversão de moedas e unidades) o programa também realiza plotagem de gráficos. O **Math-Bot** é inscrito em python e seus recursos incluem as bibliotecas do Qalculate e Sympy, todos esses recursos estarão disponíveis através do chat.

### Requisitos
+ Python3+
+ Telepot
+ Sympy
+ Qalculate

### Bot API Token
Para criar seu **Math-Bot** você deve gerar seu Api Token, para isso você necessita ir até o Telegram e falar com o **@BotFather** e criar um novo bot, depois de receber seu token de autorização, modifique a variável "bot" no script acrescentando seu **API Token**.

### Características
+ Operações básicas: + - * / ^ E () && || ! <>> = <=! = ~ & | << >>
+ Suporta todas as bases númericas, mais números sexagesimais, formato de hora e algarismos romanos
+ Cálculo simbólico: fatoração, simplificação, diferenciação e integração
+ Funções: todas as funções usuais: seno, log, sqrt, etc ...
Muitas funções estatísticas, financeiras, geométricas (aprox. 200)
+ Unidades: Suporta todas as unidades e prefixos do SI (incluindo binário), conversão cambial  
+ Variáveis e constantes: pi, e, entre outros.
+ Plotagem: usa a lib Sympy, pode traçar funções ou dados (matrizes e vetores)
+ e mais...

###### Exemplos
> Fatoração: 5! = 120 <br>
> Diferenciação: diff(x^2) = 2x; Diferenciação parcial: diff(xy^2; y) = 2xy <br>
> Integração indefinida: integrate(3x^2) = x^3 + C; Integração definida: integrate(x+2y; x; 1; 5) = 8y + 12 <br>
> Funções: (cosx)^2 + (sinx)^2 =  1; sqrt(225) = 15; log(2) = 0,3; log(2; 2) = 1 <br>
> Conversões: 5m/s to km/h = 18/km/h; 500g to N = 0,5(N*s^2)/m; USD to BRL <br>
> Plotagem: plot(x^2 + 5*x + 2) retorna gráfico da equação. <br> 
