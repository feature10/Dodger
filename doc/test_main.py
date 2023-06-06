import os
import pytest


# импорт функций из тестируемого модуля
from main.py import initialize, waitForPlayerToPressKey, playerHasHitBaddie, drawText#, main

# тестирование функции initialize()
def test_initialize():
    #os.environ - это словарь, предоставляющий доступ к переменным среды. В данном случае, мы устанавливаем значения переменной среды "PLAYER_SPEED" на 5 и переменной среды "BADDIE_SPEED" на 10.
    os.environ["PLAYER_SPEED"] = "5"
    os.environ["BADDIE_SPEED"] = "10"
    #вызов функции
    initialize()
    #Затем используется assert для проверки, что переменная среды "EXPECTED_PLAYER_SPEED" установлена на 5 и переменная среды "EXPECTED_BADDIE_SPEED" установлена на 10. 
    assert int(os.environ["EXPECTED_PLAYER_SPEED"]) == 5
    assert int(os.environ["EXPECTED_BADDIE_SPEED"]) == 10

# тестирование функции waitForPlayerToPressKey()
def test_waitForPlayerToPressKey():
    assert waitForPlayerToPressKey() != "Esc"

# тестирование функции playerHasHitBaddie()
def test_playerHasHitBaddie():
    player_rect = (0, 0, 50, 50)
    baddie_rect = (25, 25, 75, 75)
    assert playerHasHitBaddie(player_rect, baddie_rect) == True

# тестирование функции drawText()
def test_drawText():
    surface = pygame.Surface((800, 600))
    color = (255, 255, 255)
    text = "Hello, World!"
    drawText(surface, text, color, 100, 100)
    assert surface.get_at((100, 100)) == color

# тестирование функции main()
#def test_main():
   # assert main() != None
