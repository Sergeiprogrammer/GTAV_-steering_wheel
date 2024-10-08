# GTAV_-steering_wheel
## Проект: Эмулятор рулевого колеса для игр, таких как GTA, Mafia, Cyberpunk, Far Cry и других

# если вам лень читать
## проверьте ваш руль
## скачйте все фалйы и рапакуйте куда нибудь
## устнаовите python по гайдам с ютуб после запустите файл install_all.py
## заупстите файл main.py или main_no_gamepad.py (если игра без поддерижки геймпда) выберите своя зык а в селедующем этапе введите 2 и запустите игру

# *Как использовать?*
## Программа состоит из 4 файлов:
## - [main.py](https://github.com/Sergeiprogrammer/GTAV_-steering_wheel?tab=readme-ov-file#other-file-criticall-need-and-he-in-all-situation-must-be-installed)
## - [main_no_gamepad.py](https://github.com/Sergeiprogrammer/GTAV_-steering_wheel?tab=readme-ov-file#main_no_gamepadpy-1)  
## **!! НЕ УДАЛЯЙТЕ НИКАКИЕ ФАЙЛЫ, ВСЕ ФАЙЛЫ КРИТИЧЕСКИ НЕОБХОДИМЫ !!**

# Выбор файлов
## Проверьте, поддерживает ли ваша игра геймпад или нет.
### Существует 3 способа проверки:
### 1. Запустите программу с помощью `main.py`, зайдите в библиотеку Steam вашей игры, и Steam автоматически покажет, поддерживает ли игра геймпад.
### 2. Проверьте настройки игры.
### 3. Если вам сложно, просто поищите в Google :)

# main.py
## Кто должен выбрать этот файл?
### Выберите этот файл, если ваша игра поддерживает геймпад.

# main_no_gamepad.py
## Кто должен выбрать этот файл?
### Выберите этот файл, если ваша игра *не* поддерживает геймпад.

# Настройка программы
1. Сначала [установите Python](https://youtu.be/nU2Egc3Zx3Q?si=UKn9doIC49yTroGD).
2. Во-вторых, установите необходимые библиотеки, запустив скрипт "install_all" (если возникнут проблемы, ознакомьтесь с разделом "Ошибки" ниже).
3. В-третьих, выберите свой язык и после этого введите "1" (для калибровки руля) сначал найстройте руль а потом мертвую зону.
4. В-четвертых, после завершения предыдущих шагов запустите либо `main.py`, либо `main_no_gamepad.py`, введите "2" для запуска игры (моя программа работает как с легальными, так и с нелегальными копиями на Steam, Epic Games и других платформах), и наслаждайтесь :)

# Для тех, кто интересуется, как это работает
## Моя программа получает информацию о руле с помощью Pygame. Когда вы выбираете режим калибровки и поворачиваете руль влево или вправо, программа понимает, что левый поворот — это одна координата, а правый — другая координата. На основе этих координат определяется количество ввода, необходимое для виртуального геймпада или клавиатурной кнопки.

# ОШИБКИ

## Если программа говорит, что что-то не найдено, попробуйте поискать в интернете, как вручную установить необходимые библиотеки.
### Пример:
- pygame: `pip install pygame`
- keyboard: `pip install keyboard`
- vgamepad: `pip install vgamepad`

## Если программа говорит "руль не найден", возможно, ваш руль не поддерживается Pygame или не подключен. Если он не подключен, проверьте документацию к вашему рулю, установите необходимые плагины или посмотрите помощь на YouTube.

## Если в программе возникают другие ошибки, которые не решены в моей документации, пожалуйста, сообщите о них в разделе Issues моего репозитория на GitHub.
