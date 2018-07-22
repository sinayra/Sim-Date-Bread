# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pao = Character("Pão", color="#A96445")
define geleia = Character("Geleia", color="#EE3034")
define manteiga = Character("Manteiga", color="#FFC926")
define requeijao = Character("Requeijão", color="#1F489D")

# The game starts here.

label start:

    scene bg cozinha

    show pao default at center

    pao "Que dia bonito!"

    pao "Vou escolher uma rota"

    menu:
        "Escolher a rota da manteiga":
            jump rota_manteiga

        "Escolher a rota do requeijão":
            jump rota_requeijao

        "Escolher rota da geleia":
            jump rota_geleia

    return
