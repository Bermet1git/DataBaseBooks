# Для начала скачиваем postgres -->    

# Создаем нового юзера перейдя: psql postgres
# Командой --> create user testuser with password 'test1';
# Даем права новому юзеру --> alter role testuser with superuser;
# Выходим из postgres комнадой --> \q

# Заходим в терминале через нового юзера --> psql -h localhost -U testuser
# Создаем новую базу через терминал командой --> CREATE DATABASE list_of_products_db;



# ДЛЯ СПРАВКИ

# Как подключиться к БД? -->   \c name_of_database
# После подключения к БД можно узнать какие таблицы есть в данной БД -->   \d or \dt
# Проверка на существующие БД -->   \l
# Выход из postgres -->   \q
# 





import psycopg2   #Импортируем модуль psycopg2

# Подсоединяемся к базе данных  
connection = psycopg2.connect(
  database="list_of_products_db", 
  user="testuser", 
  password="test1", 
  host="127.0.0.1", 
  port="5432"
)

print("Database opened successfully")



cursor = connection.cursor()  #будет использоваться для выполнения наших команд

# -> обращаемся к курсору для создания талблицы
cursor.execute('''CREATE TABLE authors 
     (author_id VARCHAR(200) PRIMARY KEY NOT NULL,
      author_name VARCHAR(255));''')

print("Table 'authors' created successfully")



cursor.execute('''CREATE TABLE categories
     (category_id VARCHAR(100) PRIMARY KEY NOT NULL,
      category_name VARCHAR(100) UNIQUE);''')

print("Table 'categories' created successfully")



cursor.execute('''CREATE TABLE subcategories
     (subcategory_id SERIAL PRIMARY KEY NOT NULL,
     subcategory_title VARCHAR(100),
     category_id VARCHAR(100) REFERENCES categories(category_id));''')

print("Table 'subcategories' created successfully")



cursor.execute('''CREATE TABLE books 
     (book_id SERIAL PRIMARY KEY,
     title VARCHAR(255),
     year INT NOT NULL,
     author VARCHAR(100) REFERENCES authors(author_id),
     category SERIAL REFERENCES subcategories(subcategory_id),
     price INT NOT NULL);''')

print("Table 'books' created successfully")

# -> теперь необходимо зафиксировать и закрыть наше соединение
# -> фиксация говорит драйверу psycopg о необходимости посылать какие-то команды в базу данных

cursor.execute('''ALTER TABLE  ADD FOREIGN KEY (orderid) REFERENCES Orders(ORDERID);
                  ALTER TABLE ORDERLINES ADD FOREIGN KEY (orderid) REFERENCES Orders(ORDERID);''')


connection.commit()  
print('Commition done successfully')
# -> метод коммит помогает применить те изменения, которые мы внесли в БД 
# -> и эти изменения уже не могут быть отменены, если наш метод commit() выполнился успешно
connection.close()
# -> закрывает соединение с БД, чтобы не было вмешательств в БД



# Товар - книга 
# Поля: id, title, year, author, category, price

# Категории: 
# prose ()
# novel (contemporary, historical, classical), 
# business literature (economics, marketing, programming, business, personal growth), 
# detective (crime, classic, historical, foreign, psychological), 
# non-fiction (biography, notes, journalism), 
# art (art, design)

cursor.execute(
    '''INSERT INTO categories(category_id, category_name) VALUES 
        ('prose', 'prose'), 
        ('novel', 'novel'), 
        ('business_lit', 'business_literature'), 
        ('detective', 'detective'), 
        ('non_fic', 'non_fiction'), 
        ('art', 'art'),
        ('adventure', 'adventure'),
        ('fiction', 'fiction')'''
)
print('Categories successfully added')


cursor.execute(
    '''INSERT INTO categories(category_id, category_name) VALUES 
        ('prose', 'prose'), 
        ('novel', 'novel'), 
        ('business_lit', 'business_literature'), 
        ('detective', 'detective'), 
        ('non_fic', 'non_fiction'), 
        ('art', 'art'),
        ('adventure', 'adventure'),
        ('fiction', 'fiction')'''
)
print('Categories successfully added')


cursor.execute(
    '''INSERT INTO subcategories(subcategory_title, category_id) VALUES
        ('classical_prose', 'prose'), ('contemporary_prose', 'prose'),
        ('contemporary_novel', 'novel'), ('historical_novel', 'novel'), ('classical_novel', 'novel'), 
        ('economics', 'business_lit'), ('marketing', 'business_lit'), ('programming', 'business_lit'), ('business', 'business_lit'), ('personal growth', 'business_lit'),
        ('crime', 'detective'), ('classic_detective', 'detective'), ('historical_detective', 'detective'), ('foreign_detective', 'detective'), ('psychological_detective', 'detective'),
        ('biography', 'non_fic'), ('notes', 'non_fic'), ('journalism', 'non_fic'),
        ('art', 'art'), ('design', 'art'),
        ('adventure', 'adventure'),
        ('science_fiction', 'fiction'), ('fantasy', 'fiction'), ('mysticism', 'fiction'), ('horror', 'fiction')'''
)
print('Subcategories successfully added')


cursor.execute(
    '''INSERT INTO books(title, year, author, category, price) VALUES 
        ('Убить пересмешника', 2018, 'Харпер Ли', "classical_novel", 300),
        ('Над пропастью во ржи', 2013, 'Джером Д.Сэлинджер', "classical_prose", 400),
        ('Преступление и наказание', 2012, 'Федор Достоевский', "classical_prose", 450),
        ('Капитал', 2019, 'Карл Маркс', "economics", 300),
        ('Голая экономика', 2017, 'Чарльз Уилан', "economics", 400),
        ('Самый богатый человек в Вавилоне', 2020, 'Джордж Клейсон', "business", 230),
        ('Где мой сыр?', 2012, 'Спенсер Джонсон', "business", 320),
        ('Десять негритят', 2004, 'Агата Кристи', "classic_detective", 400),
        ('Кода да Винчи', 2017, 'Дэн Браун', "foreign_detective", 420),
        ('Азазель', 2019, 'Борис Акунин', "historical_detective", 300),
        ('Крестный отец', 2009, 'Марио Пьюзо', "foreign_detective", 410),
        ('Гарри Поттер и философский камень', 2016, 'Джоан Роулинг', "fantasy", 500),
        ('Властелин колец', 2019, 'Джон Р.Р. Толкин', "fantasy", 600),
        ('Дом странных детей', 2019, 'Ренсом Ригз', "fantasy", 450),
        ('История с кладбищем', 2018, 'Нил Гейман', "mysticism", 380),
        ('Жажда жизни', 2019, 'Ирвинг Стоун', "biography", 600),
        ('Не навреди. Истории о жизни, смерти и нейрохирургии', '2019', 'Генри Марш', "biography", 480),
        ('Дневник Анны Франк', 2018, 'Анна Франк', "notes", 400),
        ('Граф Монте-Кристо', 2019, 'Александр Дюма', "adventure", 500),
        ('Три мушкетера', 2020, 'Александр Дюма', "adventure", 420),
        ('Таинственный остров', 2019, 'Жюль Верн', "adventure", 410),
        ('Понедельник начинается в субботу', 2019, 'Аркадий и Борис Стругцкие', "science_fiction", 250),
        ('Марсианин', 2018, 'Энди Вейер', "science_fiction", 400),
        ('Остаток дня', 2010, 'Кадзуо Исигуро', "historical_novel", 410),
        ('Бойцовский клуб', 2017, 'Чак Паланик', "сontemporary_novel", 450)'''
)
print('Books successfully added')

connection.commit()
print("Inserted successfully")
connection.close()


