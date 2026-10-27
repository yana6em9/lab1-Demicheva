import csv
import random
import xml.etree.ElementTree as ET

BOOKS_FILE = "books-en.csv"
XML_FILE = "currency.xml"
BIBLIOGRAPHY_FILE = "bibliography.txt"


def read_books(filename):
    file = open(filename, "r", encoding="cp1252", newline="")

    reader = csv.DictReader(file, delimiter=";")
    books = list(reader)
    file.close()
    return books


def main():
    books = read_books(BOOKS_FILE)

    # 1. Количество названий длиннее 30 символов.
    long_titles = [
        book for book in books
        if len(book["Book-Title"]) > 30]
    print("Количество названий длиннее 30 символов:", len(long_titles))

    # 2. Поиск по автору с ограничением :
    # книги, изданные в 2000 году или позднее.
    author = input("Введите имя автора (как в файле): ").strip()
    found = []
    for book in books:
        try:
            year = int(book["Year-Of-Publication"])
        except (ValueError, TypeError):
            continue

        if book["Book-Author"].strip().casefold() == author.casefold() and year >= 2000:
            found.append(book)

    print(f"Книги автора {author}, опубликованные с 2000 года:")
    if found:
        for book in found:
            print(f'- {book["Book-Title"]} ({book["Year-Of-Publication"]})')
    else:
        print("Подходящие книги не найдены.")

    # 3. Случайные 20 записей для библиографического списка.
    valid_books = [
        book for book in books
        if book["Book-Title"].strip() and book["Book-Author"].strip()]
    selected = random.sample(valid_books, min(20, len(valid_books)))
    file = open(BIBLIOGRAPHY_FILE, "w", encoding="utf-8")

    for number, book in enumerate(selected, start=1):
        print(
            f'{number}. {book["Book-Author"]}. '
            f'{book["Book-Title"]} - {book["Year-Of-Publication"]}',
            file=file)

    file.close()

    print(f"Библиографический список сохранён в {BIBLIOGRAPHY_FILE}")

    # 4. словарь «Name - CharCode» из currency.xml.
    file = open(XML_FILE, "rb")

    tree = ET.parse(file)
    root = tree.getroot()

    file.close()

    currencies = {}
    for valute in root.findall("Valute"):
        name = valute.findtext("Name")
        char_code = valute.findtext("CharCode")
        if name is not None and char_code is not None:
            currencies[name] = char_code

    print('\nСловарь валют «Name - CharCode»:')
    print(currencies)


if __name__ == "__main__":
    main()