import json 

with open("storage.json") as fp:  #Берём информацию о машинах из файла и помещаем в словарь
	dictionary = json.load(fp)
#Создаём классы для задания свойств для машин	
class Vehicle(object):
	wheels = 4

class Car(Vehicle):
    def __init__(self,marka, color, doors, transmission, light):
        self.marka = marka    
        self.color = color
        self.doors = doors
        self.transmission = transmission
        self.light = light
while True:
	try:
		counter = len(dictionary) + 1
		light = "выключен"
		greed = input("\nВы хотите посмотреть ваши машины(введите 'l'), создать новую машину(введите 'm'), изменить характеристики машины(введите 'r'), удалить машину(введите 'd'), очистить гараж(введите 'p') или выйти(введите 'q')?\n")
		if greed.lower() == "l":
			if len(dictionary) == 0:
				print("\nУ вас пока нет машин\n")
			else:
				print("\nВот ваши машины\n")
				for car in dictionary:
					print(car, "-", dictionary.get(car), end="\n\n")
		elif greed.lower() == "m":
			print("\nХорошо, давайте создадим новую машину\n")
			counter_str = str(counter)
			marka = input("\nВведите марку автомобиля\n")
			color = input("\nВведите цвет будующей машины\n")
			while True:
				doors = input("\nВыберите количество дверей(2 или 4)\n")
				if doors not in "24":
					print("\nВы ввели некорректные данные\n")
				else:
					break
			while True:
				transmission = input("Выберите коробку передач(а - 'автоматическая', м - 'механическая')\n")
				if transmission == "а":
					transmission = "автоматическая"
					break
				elif transmission == "м":
					transmission = "механическая"
					break
				else:
					print("\nВы ввели некорректные данные\n")
			car = Car(marka, color, str(doors), transmission, light)  #Задаём класс Car для машины   
			while True:
				question = input("\nХотите ли вы дать название будующей машине?(д - да, н - нет)\n")
				if question.lower() == "д":
					name = input("\nВведите название для будующей машины\n")
					#Создаём машину передавая в качестве аргументов свойства для будущей машины
					dictionary[name] = {"Марка":car.marka, "Цвет": car.color, "Количество дверей": car.doors, "Коробка передач": car.transmission, "Свет": car.light, "Количество колёс": car.wheels}
					break
				elif question.lower() == "н": 
					dictionary["Car " + counter_str] = {"Марка":car.marka, "Цвет": car.color, "Количество дверей": car.doors, "Коробка передач": car.transmission, "Свет": car.light, "Количество колёс": car.wheels}
					break
				else:
					print("\nВы ввели некорректные данные\n")
					continue
				counter += 1
		elif greed.lower() == "r":
			if len(dictionary) == 0:
				print("\nУ вас нет машин\n")
			else:
				print(dictionary.keys())
				while True:
					name = input("\nВведите название машины, параметры которой вы хотите изменить\n")
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
							if dictionary[name]["Свет"] == "выключен":
								dictionary[name]["Свет"] = "включен"
							else:
								dictionary[name]["Свет"] = "выключен"
						elif character.lower() == "коробка передач":
							transmission = input("\nВыберите коробку передач(а - 'автоматическая', м - 'механическая')\n")
							if transmission.lower() == "а":
								transmission = "автоматическая"
							elif transmission.lower() == "м":
								transmission = "механическая"
							dictionary[name]["Коробка передач"] = transmission
						elif character.lower() == "количество колёс":
							print("\nДанный параметр невозможно изменить(он является основным для всех машин)\n")
							continue
						else:
							print(f"\nУ машины {name} нет такого параметра\n")
							continue
						print(f"\nПараметр {character} был успешно изменён.\n")
						print(f"\n{dictionary[name]}\n")
						break
					break
		elif greed.lower() == "d":  #Удаляет выбранную машину из словаря
			if len(dictionary) == 0:
				print("\nУ вас нет машин\n")
			else:
				print(dictionary.keys())
				name = input("\nВведите название машины, которую хотите удалить\n")
				dictionary.pop(name)
				print(dictionary.keys())
		elif greed.lower() == "p":
			dictionary.clear()
			print("\nВаш гараж был успешно очищен.\n")
		elif greed.lower() == "q":
			with open("storage.json", 'w') as output:  #Считываем информацию из словаря и записываем её в файл
				json.dump(dictionary, output)
				break
		else:
			print("\nВведите корректные данные\n")
	except NameError:
		print("\nВы ввели некорректные данные")
