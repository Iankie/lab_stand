# Лабораторный стенд для практической части ЛП (ВКР)
## Установка
### Зависимости 
```
docker.io
docker-compose
openssh
```
### Развертывание стенда
! Для развертывания стенда необходима виртуальная (или хостовая) машина Linux. 
! Необходимо использовать не стандартный порт для основной службы `openssh`, поскольку 22 порт заберет на себя контейнер с веб-приложением.
После размещения исходных материалов в папке проекта, выполните следующие шаги:
1. Запсук сборки стенда
```
sudo docker-compose build
sudo docker-compose up -d
```
2. Настройка автозапуска стенда при загрузке системы (в примере используется `systemd`).
Создайте файл со службой `systemd`.
```
sudo nano /etc/systemd/system/run-lab.service
```
Запишите в файл подобное следующему содержимое и сохраните файл.
```
[Unit]
Description=Docker Compose Application Service
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=true
WorkingDirectory=/home/debian/lab
ExecStart=/usr/bin/docker-compose start
ExecStop=/usr/bin/docker-compose stop

[Install]
WantedBy=multi-user.target
```
Перезагрузите демон-службы:
```
sudo systemctl daemon-reload
```
Добавьте службу в автозагрузку.
```
sudo systemctl enable run-lab.service
```
