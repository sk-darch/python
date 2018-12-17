from xml.dom import minidom
DOMTree = minidom.parse('books.xml')
bookstore = DOMTree.documentElement
if bookstore.hasAttribute("shelf"):
    print "Book Shelf : %s" % bookstore.getAttribute("shelf")

# Get all the Books in the bookstore.    
booklist = DOMTree.getElementsByTagName('book')

#Print detail of each Book.
for book in booklist :
    print "\n___Book Name___\n"
    if book.hasAttribute("category"):
        print "Category: %s" % book.getAttribute("category")

    title = book.getElementsByTagName('title')[0]
    print "Title: %s" % title.childNodes[0].data
    author = book.getElementsByTagName('author')[0]
    print "Author: %s" % author.childNodes[0].data
    year = book.getElementsByTagName('year')[0]
    print "Year: %s" % year.childNodes[0].data
    price = book.getElementsByTagName('price')[0]
    print "Price: %s" % price.childNodes[0].data
