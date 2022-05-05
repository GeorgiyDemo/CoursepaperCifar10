# CourseworkCifar10
Курсовая работа, где я сравнивал алгоритмы классического обучения с алогритмами глубокого обучения на 3х разных датасетах

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


### Датасеты
[Датасет для StanfordCars](https://cloud.mail.ru/public/A1P2/NmNJvdMzS)

[Собственноручно собранный датасет с Drom.ru](https://cloud.mail.ru/public/2Hwh/qXHpGZMZK)