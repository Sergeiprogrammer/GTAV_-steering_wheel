import time
import pygame
import keyboard
import sys
import json
import vgamepad as vg
import configparser

config = configparser.ConfigParser()
config.read('language.ini' ,encoding='UTF-8')

def get_lang_text(lang,text):
    with open("language.ini", "r+" , encoding='UTF-8') as file:
        return config[lang][text]

with open("language.txt" , "r+") as file:
    lang = file.readline().strip()
    try:
        if len(lang) > 0:
            pass
        else:
            lang = input("you dont have selected lanugage seclet 'ru' or ''en ")
            if lang == "ru" or lang == "en":
                file.write(lang)
            else:
                print("eror unkown language")
    except:
        print(Exception)

def get_info(arg):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.JOYAXISMOTION:
                return joystick.get_axis(arg)

def proximity_to_ends(number, act, dead_zone):
    with open("config1.json", "r") as file:
        config1 = json.load(file)
    dead_zone_values = config1["dead_zone"]
    if dead_zone_values[1] <= number <= dead_zone_values[0]:
        return None, 0
    with open("config.json", "r") as file:
        config = json.load(file)
    if act == 1:
        left_limit = config["left_limit"]
        right_limit = config["right_limit"]
        distance_to_minus_1 = abs(number - left_limit)
        distance_to_1 = abs(number - right_limit)
        if distance_to_minus_1 < distance_to_1:
            intensity = 1 - (distance_to_minus_1 / abs(right_limit - left_limit))
            return "left", intensity
        elif distance_to_minus_1 > distance_to_1:
            intensity = 1 - (distance_to_1 / abs(right_limit - left_limit))
            return "right", intensity
        else:
            return None, 0

    else:
        brake_limit = config["brake_limit"]
        gas_limit = config["gas_limit"]
        distance_to_minus_1 = abs(number - brake_limit)
        distance_to_1 = abs(number - gas_limit)
        if distance_to_minus_1 < distance_to_1:
            return "backward", 0
        elif distance_to_minus_1 > distance_to_1:
            return "forward", 0
        else:
            return None, 0

# Инициализация Pygame
pygame.init()
pygame.joystick.init()


if pygame.joystick.get_count() == 0:
    print(get_lang_text(lang,"wheel_404"))
    sys.exit()

else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

gamepad = vg.VX360Gamepad()
value_brake = 0
value_gas = 0

with open("config3.json", "r") as file:
    config2 = json.load(file)

history = None

def action(move, value):
    global value_brake, value_gas, history

    if move != "right" and move != "left" and history != "right" and history != "left":
        gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
        gamepad.update()

    if move != "forward" and history != "forward":
        gamepad.right_trigger(value=0)
        gamepad.update()

    if move != "backward" and history != "backward":
        gamepad.left_trigger(value=0)
        gamepad.update()

    if move == "left":
        gamepad.left_joystick_float(x_value_float=-value/config2['sens'], y_value_float=0.0)
        gamepad.update()

    elif move == "right":
        gamepad.left_joystick_float(x_value_float=value/config2['sens'], y_value_float=0.0)
        gamepad.update()

    elif move == "forward":  # Сброс значения поворота
        if value_gas < 255:
            value_gas += 1
        gamepad.right_trigger(value=value_gas)
        gamepad.update()

    elif move == "backward":
        if value_brake < 255:
            value_brake += 1
        gamepad.left_trigger(value=value_brake)
        gamepad.update()

    history = move  # Обновление истории

answer = int(input(get_lang_text(lang,"answer")))  # Пример переменной для логики выполнения

if answer == 1:
    config1 = {}
    answer1 = int(input(get_lang_text(lang,"answer1")))
    if answer1 == 1:
        list = []
        text = get_lang_text(lang,"list")
        exec("list = text")
        for i in list:
            print(i)
            keyboard.wait("enter")
            if "руль" in i or "wheel" in i:
                value = get_info(0)
                if "лево" in i or "right" in i:
                    config1["left_limit"] = value
                else:
                    config1["right_limit"] = value
                print(value)
            else:
                value = get_info(1)
                if "тормоза" in i or "brake" in i:
                    config1["brake_limit"] = value
                else:
                    config1["gas_limit"] = value
                print(value)
        with open("config.json", "w") as file:
            json.dump(config1, file)
    elif answer1 == 2:
        dead_zone = []
        for i in range(2):
            print(get_lang_text(lang,"dead_zone"))
            keyboard.wait("enter")
            dead_zone.append(get_info(0))
        config1["dead_zone"] = dead_zone
        with open("config1.json", "w") as file:
            json.dump(config1, file)
    elif answer1 == 3:
        while True:
            try:
                sens = float(input(get_lang_text(lang, "sens")))
                if sens > 3 and sens < 1:
                    print("eror value much that limit!")
                    break
                else:
                    pass
            except ValueError:
                print("value eror")

            try:
                with open("config3.json", "r") as file:
                    config2 = json.load(file)
                    print(config2['sens'])
            except FileNotFoundError:
                config2 = {}
            except json.JSONDecodeError:
                config2 = {}

            config2["sens"] = sens

            with open("config3.json", "w") as file:
                json.dump(config2, file)

            print(get_lang_text(lang, "succseful"))
    elif answer1 == 4:
        print(get_lang_text(lang, "button_add"))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.JOYBUTTONDOWN:
                    print(f"'{event.button}'" , get_lang_text(lang, "button_add2"))
                    first = event.button
                    key = keyboard.read_event()
                    # Проверяем, была ли клавиша нажата (KEY_DOWN)
                    if key.event_type == keyboard.KEY_DOWN:
                        if key.name != "esc":
                            print(get_lang_text(lang, "button_add3") , f": {key.name}")
                            second = key.name
                            with open("config3.json", "r") as file:
                                config4 = json.load(file)
                            new_button = {first: second}
                            config4["buttons"].append(new_button)
                            with open("config3.json", "w") as file:
                                json.dump(config4, file)
                        else:
                            print("ок")
elif answer == 2:
    # Основной цикл программы
    running = True
    with open("config.json", "r") as file:
        config = json.load(file)
    dead_zone = config.get("dead_zone", [0, 0])
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
                with open("config3.json", "r") as file:
                    config4 = json.load(file)
                for dictionary in config4["buttons"]:
                    if str(event.button) in dictionary:
                        action1 = dictionary[str(event.button)]
                        print(action1)
                        keyboard.press(action1)
                        time.sleep(0.2)
                        keyboard.release(action1)
                        break

            # Обрабатываем нажатие кнопок геймпада
        # Получаем текущее значение осей
        axis_0 = joystick.get_axis(0)
        axis_1 = joystick.get_axis(1)

        # Обрабатываем движение осей геймпада
        value, intensity = proximity_to_ends(axis_0, 1, dead_zone[0])
        if value != None:
            print(value, intensity)
        action(value, intensity)

        value, intensity = proximity_to_ends(axis_1, 2, dead_zone[1])
        if value != None:
            print(value, intensity)
        action(value, intensity)

        # Ограничиваем частоту кадров
        pygame.time.Clock().tick(60)
    # Завершаем работу Pygame
    pygame.quit()
else:
    print("command not found")