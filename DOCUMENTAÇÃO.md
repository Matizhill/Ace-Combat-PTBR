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


# Introdução
Esta documentação foi feita após a finalização do projeto de tradução brasileira de Air Combat,
seu intuito é detalhar como o jogo funciona, assim ajudando outras pessoas conseguirem traduzir para
outros idiomas. O foco do documento será voltado para tradução, então coisas que envolva além deste intuito
não será comentados ou aprofundados aqui.

<hr>

| Pastas | Descrição |
| --- | --- |
|`DA`| --- |
| `DMO` | Imagens comprimidas apresentadas durante a gameplay|
|`VO`| Estão localizados as vozes do narrador das missões |
| `M(XX)` | Arquivos utilizados (Imagens e Modelos das aeronaves e cenário) em  cada fase do jogo |
| `P(X)` | Aeronaves compráveis dentro do jogo utilizada pelo jogador|
| `SND` | Arquivos de áudio e efeitos sonoros do ambiente|
| `STR` | Vídeos no formato STR, abertura e créditos |
| `X` | Arquivos executaveis que armazena toda lógica do jogo |

Obs: M(00) é  a fase inicial e  cada segmento numérico seguinte é um nível da gameplay com suas texturas, modelos de tanto aeronaves quanto do cenário em que se passa a missão.
<br> 
Obs.2: Todos os textos de apresentação das missões estão no arquivo __MISSEL.EXE__

## Ponteiros

Os ponteiros deste jogo é simples, é apenas uma soma e subtração de valores.

### Lógica dos ponteiros
Como se mover entre ponteiros:
Texto para Ponteiros:
[XXYY] XX + 28 = ZZ > R: YYZZ
<br>
OBS: USE CTRL+F para achar.

Ponteiros para Texto:
[XXYY] YY - 28 = ZZ > R: ZZXX
<br>
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

<br>
Em trechos que o jogo precisa só exibir uma linha, ele utiliza um ponteiro apropriado para esconder a segunda linha "5C 99 08 80"
Não tem muito segredo diante as chaves, 00 faz com que o texto pare de ler o que está por vir.
São exibidos 38 caracteres por linha, sendo recomendado usar 34 para ficar uniforme.
em casos extremos, use 38 como limite.
<hr>
========
ANOTAÇÕES DE MODIFICAÇÕES

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


## Gráficos

### introdução
Os gráficos do Ace Combat estão distribuidos ao longo dos diretórios, mas divididos em sua aparição dentro do jogo. Para modificar as texturas relacionadas ao: menu principal, tela de carregamento, abertura e menu de configurações os arquivos que contém tais imagens estão localizados na pasta (X) dentro dos arquivos (.EXE).

Já para modificar as imagens referentes a jogabilidade e gameplay, cada fase do jogo possui um determinado diretório M(XX) e nele estão dispostos os gráficos dos cenários, aviões inimigos e toda a interface do jogador (**M00/MAP00.TD**) e (**M00/AIR00.TD**) respectivamente.

### Fontes 

Apesar das fontes estarem repetidas durante todos os diretórios do jogo as principais que, de fato, aparecem na gameplay são: 
(**DM0/MIS.TD/MIS.TD[0] || DM0/MIS.TD/MIS.TD[1]**) para os textos que são apresentados no início de cada missão, (**M19/AIR19.TD/AIR19.TD[1]**) para apresentar a conclusão do jogo logo após o término da missão e (**X/TITLE.EXE/TITLE.EXE[0] || X/TITLE.EXE/TITLE.EXE[1]**) para exibir os modos disponíveis na tela de ínicio do jogo.

### Modificando as texturas (TIM's File)
