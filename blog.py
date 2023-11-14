class Blog():
    def __init__(self, message):
        self.message = message
        self.likes = 0

    def post(self):
        print(self.message)


blog1 = Blog("What are the mains points of Chapter 7?")
blog2 = Blog("Classes are blueprints of objects")
blog3 = Blog("Objects are instances of classes")
blog4 = Blog("This is called object oriented programming OOP")
blog5 = Blog("Classes should use Pascal naming convention")


# Output blogs
blog1.post()
blog2.post()
blog3.post()
blog4.post()
blog5.post()

# set some likes on certain blogs
blog1.likes = 2
blog3.likes = 3

print(blog1.likes)
print(blog2.likes)
print(blog3.likes)
