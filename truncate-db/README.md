##Очистка всех всех таблиц с сохранением связей и constraints между ними
# Порядок выполнения
* подключение к нужной бд по заднному хосту порту с использованием username и pass
* Получение списка всех таблиц
* Последовательный проход по списку и очистки таблицы с использованеим TRUNCATE CASCADE 


## Насткройка окружения  
1) Перейти в директорию проекта  
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/1.png)  
2) Нажатать правой кнопкой мыши по 'pom.xml' и выбрать 'Add as Maven Project'   
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/2.png)
3) Подождать пока не закончится импорт   
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/3.png)
4) После выполнения импорта появится ошибка об отсутсвии JDK   
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/4.png)
5) Необходимо нажать 'Set JDK', выбрать 'Add JDK' и далее 'Download JDK'   
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/5.png)
6) В диалоговом окне нужно выбрать '17' версию. Нажать 'OK'   
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/6.png)
7) Необходимо дождаться установки   
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/7.png)
8) Далее выбрать 'File' и 'Project Settings'   
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/8.png)
9) Далее выбрать 'Modules', 'truncate-db', 'sources' и 'Language level' выставить в  '10-Local variable type inference'. Нажать 'OK'.   
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/9.png)
10) Далее нажать 'File' и выбрать 'Settings'   
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/10.png)
11) В окно поиска вбить 'java compiler'. Должно появится 'Build, Execution, Deployment > Compiler > Java Compiler'.  Необхоимо выбрать 'Target bytecode version' как 17. Нажать 'OK'.   
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/11.png)

## Запуск
1) В файле 'PostgresTruncate.java' необходимо поменять следующие переменные:   
- hostname   
- port   
- dbName    
- user    
- pass   

  И запустить с помощью конпки 'Play'    
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/12.png)   
   
2) Пример результата работы       
![Alt text](https://github.com/AsonovNikolay/ICT-HACK-V/blob/main/truncate-db/readme_pictures/13.png)

