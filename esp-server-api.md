# нужно
- # процедура рукопожатия
	- esp передает id карты, чтобы Паша понял, что за esp
- # обновления (самое важное)
	- у Паши хранится табличка вида - `id - fwVersion - fwUrl`. Там все наши устройства по id, какая у них должна быть прошивка и путь к файлу прошивки.
	- fwVersion 0x0000 - резерв. В этом случае я не меняю прошивку. В строке url сервер шлет "xxx"
- # передача координат
- # передача моточасов

общение
- сервер ничего не шлет сам, только по запросу
- после отосланных данных всегда ждем ок
- таймаут ожидания ок - 15 сек.
- общий таймаут на любые посылки 60 сек 

структура пакета (little endian)
- 2 байта длина uint16 - длина с учетом этих байт
- 2 байта команда
- 2 байта команда второго порядка (опционально)
- остальные байты данные

команды
- 0x1001 - ок - посылка получена или просто ping - в теле может быть команда
	- если всего 4 байта - просто ок
	- 4й и 5й байты - команда из этого списка от сервера
- 0x10FF - ошибка (в теле расшифровка)
	- слишком длинное сообщение
	- не могу обновиться
- 0x1055 - update
	- если запрос esp - то это всего 4 байта
	- если ответ сервера - 2 длина, 2 ок, 2 upd, 2fwVer, url
- 0x10CC - координаты
	- после первых 4 байт идут блоки по 12 байт - lat, lng, time
- 0x10AC - моточасыц
- 0x10ED - id карты передаю
	- 2 + 2 + 15 байт на id ( незанятые байты в конце - забиты нулями)

что я вообще делаю
- коннект к серверу
- как только сервер доступен (id передал) - отсылаю все координаты из памяти. Жду ок и след партию
- если координат нет (больше нет) - запрашиваю обновление, если нужно обновляюсь - запрос обновления - раз в 5 мин
- если делать нечего - шлю ок. И только на пустой ок сервер может мне отправить доп команду, иначе я ее и не читаю.
+++++++++++++
2023-07-22 13:20
[[]]
[[]]
#
