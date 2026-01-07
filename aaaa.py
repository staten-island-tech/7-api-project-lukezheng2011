import requests

def get_book():
    response = requests.get('https://potterapi-fedeperin.vercel.app/en/books')
    books = response.json()
    # return books
    return {
        "title": books["title"],
        "release": books["releaseDate"],
        "pages": books["pages"]
    }


books = get_book()
print(books)






