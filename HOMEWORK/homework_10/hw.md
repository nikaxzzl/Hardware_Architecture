## Задача 1. Включение аппаратной виртуализации (Intel VT-x / AMD-V)
![](screen/01.png)
Config → CPU. Опция Intel Virtualization Technology
![](screen/02.png)
Security → Virtualization
## Задача 2. Проверка статуса TPM и его связь с BitLocker
![](screen/03.png)
Security → Security Chip

## Задача 3. Настройка поведения при потере питания (After Power Loss)
![](screen/04.png)
По умолчанию стоит Off.

## Задача 4. Отключение Secure Boot и проверка последствий
![](screen/05.png)
Security → Secure Boot. Secure Boot (Off)
![](screen/06.png)
Security → Secure Boot. Secure Boot (On)

## Задача 5. Настройка порядка загрузки через Fast Boot
![](screen/07.png)
Когда включен Fast Boot (Quick), компьютер пытается быстрее запустить систему, из-за этого он не проверяет USB-порты, поэтому не видит флешку.

## Задача 6. Установка пароля на включение (Power-On Password)
![](screen/08.png)

## Задача 7. Настройка SATA Controller Mode для установки ОС
![](screen/09.png)

## Задача 8. Просмотр и очистка системного журнала событий (Event Log)
![](screen/10.png)
В журнале BIOS обычно фиксируются ошибки при запуске компьютера (POST), замене деталей или настроек, при попытке ввести неверный пароль.

## Задача 9. Восстановление заводских настроек с сохранением пользовательских данных
![](screen/11.png)
Restart → Load Factory Defaults
![](screen/12.png)
Security → Reset System to Factory Defaults
## Задача 10. Полный сценарий: подготовка нового сотрудника (IT-администратор)
![](screen/14.png)
