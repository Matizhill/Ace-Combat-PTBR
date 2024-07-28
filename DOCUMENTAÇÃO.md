# Documentação de Air Combat (PSX)
# Súmario
- Introdução
- Créditos
## Diretórios
- Pastas
- Tipo de arquivos
## Modificação
- Texto
- Ponteiros
- Gráficos
- Compressão
- 


# Introdução
Esta documentação foi feita após a finalização do projeto de tradução brasileira de Air Combat,
seu intuito é detalhar como o jogo funciona, assim ajudando outras pessoas conseguirem traduzir para
outros idiomas. O foco do documento será voltado para tradução, então coisas que envolva além deste intuito
não será comentados ou aprofundados aqui.

<hr>

| Pastas | Descrição |
| --- | --- |
| `DA` | List all *new or modified* files |
| `DMO` | Show file differences that **haven't been** staged |
| `M(XX)` |
| `P(X)` |
| `SND` |
| `STR` | Vídeos no formato STR |
| `VO` |
| `X` | Arquivos executaveis que armazena toda lógica do jogo |

Não tem muito segredo diante as chaves, 00 faz com que o texto pare de ler o que está por vir.

São exibidos 38 caracteres por linha, sendo recomendado usar 34 para ficar uniforme.
em casos extremos, use 38 como limite

## Ponteiros

Os ponteiros deste jogo é simples, é apenas uma soma e subtração de valores.

### Lógica dos ponteiros
Como se mover entre ponteiros:
Texto para Ponteiros:
[XXYY] XX + 28 = ZZ > R: YYZZ
OBS: USE CTRL+F para achar.

Ponteiros para Texto:
[XXYY] YY - 28 = ZZ > R: ZZXX
OBS: USE CTRL+G para achar.

### Endereços dos Ponteiros de cada Missão:

- M01: 4E28C
- M02: 4EB44
- M03: 4F5E4
- M04: 4FD2C
- M05: 50844
- M06: 511D0
- M07: 51848
- M08: 52CF0
- M09: 53BC8
- M10: 54638
- M11: 54FA4
- M12: 5639C
- M13: 56E8C
- M14: 578E4
- M15: 588D4
- M16: 590FC
- M17: 594A4-594C

========
Em trechos que o jogo precisa só exibir uma linha, ele utiliza um ponteiro apropriado para esconder a segunda linha "5C 99 08 80"
<hr>
========
NOTAÇÕES DE MODIFICAÇÕES

Tabela:
| Numeração | Caractere | Acentuação | Valor   (HEX)|
|---|---|---|---|
|22|"|Ç|E7|
|23|#|Á|E0|
|24|$|Ã|E3|
|25|%|Â|E2|
|26|&|Ú|FA|
|27|'|Ó|F3|
|2A|*|Ê|EA|
|2B|+|É|E9|
|2F|/|Õ|F5|
|3D|=|Í|ED|


`HEX:  1A 35 02 80` = Endereço do Ponteiro: "Good Luck!" (_Boa Sorte_)
<br>
`offset: C488` = Endereço do Ponteiro: "LEVE:HARD" (_NÍVEL:DIFÍCIL_)

