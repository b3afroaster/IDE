Сердечно-сосудистые заболевания являются серьезной проблемой здравоохранения, и раннее выявление может улучшить результаты лечения. Существует необходимость в эффективных методах анализа данных для прогнозирования и диагностики.
Предлагается использовать Python и методы машинного обучения для анализа данных о сердечно-сосудистых заболеваниях. Python выбран из-за его безопасности, широкого применения в медицине, простоты использования и наличия необходимых библиотек (Pandas, Matplotlib, IPython, NumPy, SciPy). Упоминается соответствие требованиям HIPAA.
Особое внимание уделяется потенциалу Python для создания приложений, которые могут предсказывать сердечно-сосудистые заболевания на ранних стадиях, когда симптомы могут отсутствовать (например, ишемическая болезнь сердца на ранних стадиях).
Python — это язык программирования с высоким уровнем объектно-ориентированной абстракции. Это, а также простота(быстрота написания кода), открытый код делают его отличным инструментом для разработки моделей машинного обучения в рамках исследовательских проектов в сфере здравохранения.
Текст акцентирует внимание на важности применения методов кибербезопасности в секторах здравоохранения, котороые поддерживаются в Phyton:
(Критическое применение методов кибербезопасности)
1)Анализ угроз: Использование Python позволяет применять библиотеки, такие как Scapy для анализа и манипуляции сетевыми пакетами, а также библиотеки, такие как Requests для выполнения HTTP-запросов, что важно для выявления уязвимостей веб-приложений.
2)Сканирование и тестирование на проникновение: Python также предоставляет возможности для разработки инструментов, которые могут использоваться для сканирования портов и проведения тестирования на проникновение. Модули, такие как Nmap и Metasploit, могут быть интегрированы с Python для автоматизации данного процесса.
3)Обнаружение и анализ вредоносного ПО: Важной задачей для сектора здравоохранения является защита конфиденциальной информации пациентов. Python может быть использован для создания программ, которые обнаруживают подозрительные операции или аномалии в данных, что позволяет улучшить безопасность.
Также отмечается, что Phyton предоставляет системы обнаружения заболеваний с применением методов машинного обучения, также может быть реализована с помощью Python. Библиотеки, такие как TensorFlow и scikit-learn, способствуют созданию моделей, которые могут распознавать паттерны, связанные с заболеваниями.
Его возможности по анализу киберугроз, интеграции с системами управления и внедрению автоматизированных процессов делают его идеальным выбором для разработки приложений, направленных на защиту конфиденциальной информации и обеспечение безопасности данных пациентов.

Далее отмечается важность диагностики сердечных заболеваний, которые несут критическую угрозу для жизни, ухудшающую здоровье как в развивающихся, так и в развитых странах.
Авторы говорят о возможностях библиотеки Matplotlib Она даёт возможность представить набор данных в виде гистограммы, которая помогает проанализировать и интерпретировать данные о сердечных заболеваниях, что важно для дальнейшего исследования и оценки состояния здоровья пациентов.
Интерпритация данных включает в себя результаты анализа данных и делает выводы об отношениях. Отмечается роль метрик для оценивания качества предсказания модели, которые необходимы для верной интерпритации результатов
Отдельно выделили матрицу кореляций, для оценки взаимосвязи между признаками
Упоминается компромисс между точностью модели и ее интерпретируемостью, что является общей проблемой в машинном обучении.


В разделе "обсуждение" говорилось о разном выборе алгоритмов машинного обучения, а также их результаты, которые сравнивались друг с другом. Кратко оворилось о "подкапотке" и плюсах каждого из алгоритмов.
5.2 Классификатор K -соседей
Классификатор k-соседей распознает вектор на основе большинства голосов его соседей. Маршрут классификации этого классификатора очень важен, т.к. этот метод используется на основе большинства голосов соседа. Расстояние в виде вектора определяет классификацию
5.3 Классификатор дерева решений
Классификатор дерева решений создает дерево из набора данных Этот элемент данных состоит из ветвей, которые соединяют ветви, они в свою очередь разветвляются до листьев. Дерево решений используется для классификации наличичя/отсутствия сердечных заболеваний Алгоритм дерева решений рассматривается как древовидная блок-схема, которая может достигать больших размеров, из-за чего модель уязвима перед переобучением. Каждый лист узла включает результат. Деревья решеий использовались для оценки важеости признаков, чтобы отсечь незначимые признаки
5.4 . Метод опорных векторов
Алгоритм машины опорных векторов (SVM) генерирует модель, которая классифицирует новые примеры в одну из нескольких категорий. Помимо этого, он делится на две группы. Модель SVM можно назвать «невероятностным классификатором», поскольку ее можно рассматривать как пространственную характеристику экземпляров. Гиперплоскость считается зданием, которое делит различные примеры на различные категории. SVM контролирует алгоритм машинного обучения, используемый как для задач классификации, так и для задач регрессии
Опорный вектор разграничивает координаты отдельных наблюдений. После этого классификатор SVM рассматривается как граница, которая наилучшим образом разделяет два класса.
5.5 Случайный лесной классификатор
Классификация случайного леса считается ансамблевым подходом к обучению , используемым для решения задач машинного обучения, таких как классификация и регрессия. Эта классификация случайного леса алгоритма обнаружения сердечных заболеваний заболеваний сердца работает путем построения нескольких деревьев решений. Помимо этого, этот классификатор использует технику, называемую «бутстрап-агрегацией».
Scikit-learn вычисляет важность узла с помощью Gini Importance
набор деревьев решений, построенных из случайно выбранных подмножеств обучающего набора. Затем данные о сепсисе агрегируются из различных деревьев решений, определяя окончательный класс тестового объекта. Прогноз случайного леса отображает графическое представление модели, а также ее точность для сбора данных набора данных. При использовании случайного леса точность системы обнаружения заболеваний сердца составляет 0,821875.
При использовании алгоритма случайного леса в исследовании была достигнута максимально высокая точность проноза.
5.6 Логистическая регрессия
Переменные логистической регрессии показывают класс. Этот класс является переменной категориальной зависимости для логистического уравнени Помимо этого, зависимая переменная имеет дихотомическую природу, что означает, что ее можно классифицировать на две группы.
Эти модели сравнивались в зависимости от точности, специфичности, f-меры, точности, а также чувствительности.
За исключением дерева решений, наилучшие значения, предоставляемые моделью МО, предоставляются случайным лесом. Это самый простой метод прогнозирования заболеваний сердца для получения точных результатов.
