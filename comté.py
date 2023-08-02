my_books = {}

my_list = s.split(“ / n”)

k = 0
for book in my_list:
    item = book.split(“ | ”)
    my_books.update(k: item)
    k += 1

newer_books = []
for item in my_books:
    if my_books[2] > 1900:
        newer_books.append(item)

// newer_books.sort()

for new_book in newer_books:
    author_listed = newer_book[1].split(“, ”)
    author = author_listed[1] +” “+author[0]
    new_book[1] = author

for new_book in newer_books:
    print(f”\”{newer_book[0]}\” by
    {newer_book[1]}({newer_book[3]})”)

    == == == == =


    A
    list
    of
    all
    decades
    from the earliest

    decade in the
    book
    list.
    And
    the
    number
    of
    books in that
    decade, up
    to
    the
    present.

    1800(1)
    1810(23)
    1820(0)
    1830(15)
    …
    2020(10)

    my_books = {}

    my_list = s.split(“ / n”)

    k = 0
    for book in my_list:
        item = book.split(“ | ”)
        my_books.update(k: item)
        k += 1

    newer_books = []
    for item in my_books:
        if my_books[2] > 1900:
            newer_books.append(item)

    // newer_books.sort()

    for new_book in newer_books:
        author_listed = newer_book[1].split(“, ”)
        author = author_listed[1] +” “+author[0]
        new_book[1] = author

    for new_book in newer_books:
        print(f”\”{newer_book[0]}\” by
        {newer_book[1]}({newer_book[3]})”)

        earliest_decade = 0
        decades = {}
        decade = 0
        for item in my_list:
            if item[2] <= earliest_decade:  # setting lowest decade
                earliest_decade = floor(item[2] / 10) * 10
            decade = int(floor(item[2] / 10) * 10

            if decade in decades.keys():
                decades.update(decade: decades[decade] += 1)
            else:
            decades.update(decade: 1)

            i = earliest_decade

            for i in range(2020):
                if
            i in decades.keys():
            print(f”{i} \({decades[i]}\))
            else:
            print(f”{i} \(0\))
            i += 10


        def decadeify(year):
            return math.floor(year / 10) * 10

