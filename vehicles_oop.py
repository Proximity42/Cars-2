import json

with open("C:/Users/vlad_/Desktop/Машины/storage.json") as fp:
	dictionary = json.load(fp)
class Vehicle(object):
	wheels = 4

class Car(Vehicle):
    def __init__(self, color, doors, transmission, light):
        self.color = color
        self.doors = doors
        self.transmission = transmission
        self.light = light
while True:
	counter = len(dictionary) + 1
	light = "выключен"
	greed = input("\nВы хотите посмотреть ваши машины(введите 'l'), создать новую машину(введите 'm'), посмотреть характеристики машины(введите 'c'), изменить характеристики машины(введите 'r'), удалить машину(введите 'd'), очистить гараж(введите 'p') или выйти(введите 'q')?\n")
	if greed.lower() == "l":
		if len(dictionary) == 0:
			print("\nУ вас пока нет машин\n")
		else:
			print("\nВот ваши машины\n")
			print(dictionary.keys())
	elif greed.lower() == "m":
		print("\nХорошо, давайте создадим новую машину\n")
		counter_str = str(counter)
		color = input("\nВведите цвет будующей машины\n")
		while True:
			doors = input("\nВыберите количество дверей(2 или 4)\n")
			if doors not in "24":
				print("\nВы ввели некорректные данные\n")
			else:
				break
		transmission = input("Выберите коробку передач(а - 'автоматическая', м - 'механическая')\n")
		while True:
			if transmission == "а":
				transmission = "автоматическая"
				break
			elif transmission == "м":
				transmission = "механическая"
				break
			else:
				print("\nВы ввели некорректные данные\n")
		car = Car(color, str(doors), transmission, light)
		question = input("\nХотите ли вы дать название будующей машине?(д - да, н - нет)\n")
		while True:
			if question.lower() == "д":
				name = input("\nВведите название для будующей машины\n")
				dictionary[name] = {"Цвет": car.color, "Количество дверей": car.doors, "Коробка передач": car.transmission, "Свет": car.light, "Количество колёс": car.wheels}
				break
			elif question.lower() == "н": 
				dictionary["Car " + counter_str] = {"Цвет": car.color, "Количество дверей": car.doors, "Коробка передач": car.transmission, "Свет": car.light, "Количество колёс": car.wheels}
				break
			else:
				print("\nВы ввели некорректные данные\n")
				continue
			counter += 1
	elif greed.lower() == "c":
		if len(dictionary) == 0:
			print("\nУ вас нет машин\n")
		else:
			while True:
				print(dictionary.keys())
				name = input("\nВведите название машины, параметры которой вы хотите посмотреть\n")
				if name in dictionary: 
					print(f"\nВот характеристики машины {name}: {dictionary[name]}\n")
					break
				else:
					print("У вас нет машины, с таким названием")
	elif greed.lower() == "r":
		if len(dictionary) == 0:
			print("\nУ вас нет машин\n")
		else:
			print(dictionary.keys())
			while True:
				name = input("\nВведите название машины, параметры которой вы хотите изменить\n")
				if name in dictionary:
					while True:
						print(f"\n{dictionary[name]}\n")
						character = input("\nВведите название параметра, который вы желаете изменить(на русском)\n")
						if character.lower() == "цвет":
							color = input("\nВведите желаемый цвет\n")
							dictionary[name]["Цвет"] = color
						elif character.lower() == "количество дверей":
							doors = input("\nВведите количество дверей(2 или 4)\n")
							if doors in "24":
								dictionary[name]["Количество дверей"] = doors
							else:
								print("\nКоличество дверей может принимать только значения '2' или '4'\n")
								continue
						elif character.lower() == "свет":
							dictionary[name]["Свет"] = "включен"
							print(dictionary)
						elif character.lower() == "коробка передач":
							transmission = input("\nВыберите коробку передач(а - 'автоматическая', м - 'механическая')\n")
							if transmission.lower() == "а":
								transmission = "автоматическая"
							elif transmission.lower() == "м":
								transmission = "механическая"
							else:
								print("\nПараметр 'Коробка передач' может принимать только два значения\n")
								continue
							dictionary[name]["Коробка передач"] = transmission
						elif character.lower() == "количество колёс":
							print("\nДанный параметр невозможно изменить(он является основным для всех машин)\n")
							continue
						else:
							print(f"\nУ машины {name} нет такого параметра\n")
							continue
						print(f"\nПараметр {character} был успешно изменён.\n")
						print(f"\n{dictionary[name]}\n")
						more = input("\nЖелаете ли вы изменить другие параметры(д - 'да', н - 'нет')?\n")
						if more.lower() == "н":
							break
						elif more.lower() == "д":
							pass
						else:
							print("\nВы ввели некоректные данные\n")
					break
				else:
					print("\nУ вас нет машины с таким названием\n")
	elif greed.lower() == "d":
		if len(dictionary) == 0:
			print("\nУ вас нет машин\n")
		else:
			print(dictionary.keys())
			name = input("\nВведите название машины, которую хотите удалить\n")
			if name in dictionary:
				dictionary.pop(name)
				print(dictionary.keys())
			else:
				print("\nУ вас нет машины, с таким названием\n")
	elif greed.lower() == "p":
		if len(dictionary) == 0:
			print("\nУ вас нет машин\n")
		else:
			dictionary.clear()
			print("\nВаш гараж был успешно очищен.\n")
	elif greed.lower() == "q":
		with open("C:/Users/vlad_/Desktop/Машины/storage.json", 'w') as output:
			json.dump(dictionary, output)
			break
	else:
		print("\nВведите корректные данные\n")