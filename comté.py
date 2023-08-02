import sys
from math import floor


def main():
    s=sys.stdin.readlines() #pythonic entry of multi-lined input. Stores as a list.
    books=convert_input_to_dictionary(s)
    newer_books=filter_by_year(books)
    sorted_newer_books=sort_by_author(newer_books)
    format_my_list_of(sorted_newer_books)

    #start part 2:
    list_decades(books)

def convert_input_to_dictionary(s): #Returns dictionary of entries.
    my_books = {} #dictionary to store each book from the dataset
    k = 0 #key value for my_books. Increased on each iteration of the following loop.
    for book in s:
        item = book.split("|")
        item[2]=item[2].replace("\n", "") #this removes the "/n" from the date (added from .readlines())
        my_books.update({k:item})
        k += 1
    return my_books

def filter_by_year(my_books, year=1900): #function to filter books by year. Optional parameter of year; default value 1900. Returns list of newer books.
    newer_books = []
    for item in my_books:
        publication_date=my_books[item][2]
        if int(publication_date)> year:
            newer_books.append(my_books[item])
    return newer_books

def sort_by_author(my_books): #this functionality was absent from my original code.
    my_books.sort(key=lambda x:x[1])
    return my_books

def format_my_list_of(books): #this will create the formatted output.
    for book in books:
        try:
            author_listed = book[1].split(", ")
            if len(author_listed)==2:
                author = author_listed[1] +" "+author_listed[0]
                book[1] = author
            else:
                author = author_listed[1] + " " + author_listed[0]+" "+author_listed[3] #accounts for honorary titles
                book[1] = author
        except IndexError: #accounts for authors with single names
            continue

    for book in books:
        print(f"\"{book[0]}\" by {book[1]} ({book[2]})")

#================END OF PART 1=====================================

def list_decades(my_list):
    earliest_decade = 2024
    decades = {}
    decade = 0
    for item in my_list:
        if int(my_list[item][2]) <= earliest_decade:  # setting lowest decade
            earliest_decade = floor(int(my_list[item][2]) / 10) * 10
        decade = floor(int(my_list[item][2]) / 10) * 10

        if decade in decades.keys():
            decades.update({decade: int(decades[decade])+1})
        else:
            decades.update({decade:1})

        i = earliest_decade


    for i in range(earliest_decade,2020, 10):
        if i in decades.keys():
            print(f"{i} ({decades[i]})")
        else:
            print(f"{i} (0)")

main()