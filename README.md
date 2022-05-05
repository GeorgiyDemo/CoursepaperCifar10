# MLCoursepapper
Курсовая работа, где я сравнивал алгоритмы классического обучения с алогритмами глубокого обучения (ANN, CNN) на 3х разных датасетах

### Ноутбуки

- [CIFAR-10](https://nbviewer.org/github/GeorgiyDemo/CoursepaperCifar10/blob/master/CIFAR/CIFAR.ipynb)
- [Stanford cars](https://nbviewer.org/github/GeorgiyDemo/CoursepaperCifar10/blob/master/StanfordCars/STANFORD.ipynb)
- [Собственный датасет с Drom.ru](https://nbviewer.org/github/GeorgiyDemo/CoursepaperCifar10/blob/master/Drom/DROM.ipynb)

### Итоги

Сравнение классических алгоритмов
|                        | **CIFAR-10** | **Drom.ru**    | **Stanford cars** |
| ---------------------- | ------------ | -------------- | ----------------- |
| **Алгоритм**           | **Точность** | **Время, сек** | **Точность**      | **Время, сек** | **Точность ** | **Время, сек ** |
| SVC                    | 46%          | 1986,03        | 24%               | 361,42 | 35% | 1,06 |
| RandomForestClassifier | 44%          | 6296,49        | 25%               | 1340,82 | 29% | 71,4 |
| LogisticRegression     | 29%          | 557,37         | 21%               | 534,2 | 22% | 12,69 |
| KNeighborsClassifier   | 28%          | 16,5           | 21%               | 3,18 | 28% | 0,11 |
| SGDClassifier          | 24%          | 1004,74        | 20%               | 1431,24 | 24% | 32,73 |
| MultinomialNB          | 23%          | 0,51           | 16%               | 0,3 | 29% | 0,05 |

Сравнение по общей эффективности (точность/время)
Классические алгоритмы              |  Классические + глубокие алгоритмы
:----------------------------------:|:-------------------------:
![](https://github.com/GeorgiyDemo/CoursepaperCifar10/blob/master/CIFAR/img/acc_time_plot1.png)  |  ![](https://github.com/GeorgiyDemo/CoursepaperCifar10/blob/master/CIFAR/img/acc_time_plot2.png)

Если важна точность, то предпочтительным будет использование машины опорных векторов (SVM) из классических алгоритмов обучения и сверточной нейросети (CNN) из глубоких.

Если важна скорость, то можно использовать наивный байесовский классификатор (Naive Bayes classifier) или метод k-ближайших соседей (k-nearest neighbors).

### Интересные наблюдения

Самые популярные и самые редкие автомобили в России на Drom.ru
Популярные              |  Редкие
:----------------------------------:|:-------------------------:
![](https://github.com/GeorgiyDemo/CoursepaperCifar10/blob/master/Drom/img/max.png)  |  ![](https://github.com/GeorgiyDemo/CoursepaperCifar10/blob/master/Drom/img/min.png)

Производительность OpenCV и PIL
По операциям              |  Общая
:----------------------------------:|:-------------------------:
![](https://github.com/GeorgiyDemo/CoursepaperCifar10/blob/master/StanfordCars/img/plot1.png)  |  ![](https://github.com/GeorgiyDemo/CoursepaperCifar10/blob/master/StanfordCars/img/plot2.png)

[Ноутбук](https://nbviewer.org/github/GeorgiyDemo/CoursepaperCifar10/blob/master/other/PillowVsOpenCV.ipynb)

### Датасеты
[Датасет для StanfordCars](https://cloud.mail.ru/public/A1P2/NmNJvdMzS)

[Собственноручно собранный датасет с Drom.ru](https://cloud.mail.ru/public/2Hwh/qXHpGZMZK)