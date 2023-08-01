from csv_file import read_rows_csv, write_rows_csv
from contacts import Contact
from pprint import pprint
import re

def adjust_contact_book(contact_book_in):
    for c in contact_book_in:
        person = Contact(c[0],c[1],c[2],c[3],c[4],c[5],c[6])
        person.check_fio()
        c[0] = person.lastname
        c[1] = person.firstname
        c[2] = person.surname

    sorted_contact_book = sorted(contact_book, key=lambda lastname: lastname[0], reverse=False)
    unique_contact_book = find_and_merge_duplicate(sorted_contact_book)

    for c in unique_contact_book:
        c[5] = adjust_phone(c[5])

    return unique_contact_book


def find_and_merge_duplicate(book):
    person_dupl = Contact()
    for c in book:
        person_cur = Contact(c[0], c[1], c[2], c[3], c[4], c[5], c[6])
        if person_dupl.lastname == person_cur.lastname and person_dupl.firstname == person_cur.firstname and \
                (person_dupl.surname == person_cur.surname or person_cur.surname ==''):
            if person_cur.surname =='':
                person_cur.surname = person_dupl.surname
            if person_cur.organization == '':
                person_cur.organization = person_dupl.organization
            if person_cur.position == '':
                person_cur.position = person_dupl.position
            if person_cur.phone == '':
                person_cur.phone = person_dupl.phone
            if person_cur.email == '':
                person_cur.email = person_dupl.email

            book.remove([person_dupl.lastname, person_dupl.firstname, person_dupl.surname, person_dupl.organization,
                         person_dupl.position, person_dupl.phone, person_dupl.email])

        c[0] = person_cur.lastname
        c[1] = person_cur.firstname
        c[2] = person_cur.surname
        c[3] = person_cur.organization
        c[4] = person_cur.position
        c[5] = person_cur.phone
        c[6] = person_cur.email

        person_dupl = person_cur

    return book

def adjust_phone(number):
    pattern = r"(\+7|8)\s?[(]?(\d{3,3})[)]?\s?[-]?(\d{3,3})[-]?(\d{2,2})[-]?(\d{2,2})\s?[(]?([доб.]+)?\s?(\d+)?[)]?"
    replace1 = r"+7(\2)\3-\4-\5"
    replace2 = r"+7(\2)\3-\4-\5 доб.\7"

    res = re.match(pattern, number)
    result = ""
    if res is None:
        result = "phone"
    else:
        if res.group(7) is None:
            result = re.sub(pattern, replace1, number)
        else:
            result = re.sub(pattern, replace2, number)
    return result

if __name__ == '__main__':
    file_input = "phonebook_raw.csv"
    file_output = "phonebook_raw_final.csv"

    contact_book = read_rows_csv(file_input)
    contact_book_final = adjust_contact_book(contact_book)

    write_rows_csv(file_output, contact_book_final)

    print(f'\nСоздан файл с именем {file_output}.')







