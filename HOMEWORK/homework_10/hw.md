## Задача 1. Включение аппаратной виртуализации (Intel VT-x / AMD-V)
![Config → CPU. Опцию Intel Virtualization Technology](screen/01.png)
![Security → Virtualization](screen/02.png)

## Задача 2. Проверка статуса TPM и его связь с BitLocker
![Security → Security Chip](screen/03.png)

## Задача 3. Настройка поведения при потере питания (After Power Loss)
![](screen/04.png)
Поумолчанию соит off

## Задача 4. Отключение Secure Boot и проверка последствий
![Security → Secure Boot. Secure Boot (Off)](screen/05.png)

![Security → Secure Boot. Secure Boot (On)](screen/06.png)

## Задача 5. Настройка порядка загрузки через Fast Boot
![](screen/07.png)
Когда включен Fast Boot (Quick), пытается быстрее запустить систему, из-за этого он не проверяет USB-порты, поэтому он не видит флешку

## Задача 6. Установка пароля на включение (Power-On Password)
![](screen/08.png)

## Задача 7. Настройка SATA Controller Mode для установки ОС
![](screen/09.png)

## Задача 8. Просмотр и очистка системного журнала событий (Event Log)
![](screen/10.png)
В журнале BIOS обычно фиксируются ошибки при запуске компьютера (POST), замене деталий или настроек, прри попытики ввести неверный пароль

## Задача 9. Восстановление заводских настроек с сохранением пользовательских данных
![Restart → Load Factory Defaults](screen/11.png)
![Security → Reset System to Factory Defaults](screen/12.png)
![Подтверждения  сброса конфигурации BIOS](screen/13.png)

## Задача 10. Полный сценарий: подготовка нового сотрудника (IT-администратор)
![Подтверждения  сброса конфигурации BIOS](screen/14.png)