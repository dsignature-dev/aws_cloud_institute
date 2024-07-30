class Employee:
    # class attribute to track current number of employees
    employee_count = 0

    def __init__(self, name, email, hire_date):
        """
        Constructor method for Employee class
        Initializes an Employee object with name, email, and hire date. 
        Adjusts the employee_count class attribute when a new employee 
            is created. 
        """
        self.name = name
        self.email = email
        self.hire_date = hire_date
        Employee.employee_count += 1

        self.total_score = 0
        self.posts = []
        self.comments = []

    def post_message(self, message):
        post = Post(self, message)
        self.total_score += 5

        self.posts.append(post.message)
        return post

    def comment_on_post(self, message, post):
        comment = Comment(self, message, post)
        post.comments.append(comment)  # appends comment to the post object
        self.comments.append(comment)  # appends comment to the Employee object
        return comment

    # def __str__(self):
    #     """
    #     Method that returns a string describing the object
    #     """
    #     return f"Employee: {self.name}\nHire date:{self.hire_date}"

    # def __repr__(self):
    #     """
    #     Method that returns identifying information on the object
    #     """
    #     return f"Employee object repr {self.name}"


# Create a Post class for creating new Post objects. Be sure your new class is not indented inside the previous class definition.

class Engineer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = "enginering"

    def comment_on_post(self, message, post):
        if post.author.department is "engineering":
            points = 1
        else:
            points = 5
        return super().comment_on_post(message, post, points)


class Marketer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = "marketing"

    def comment_on_post(self, message, post):
        if post.author.department is "marketing":
            points = 1
        else:
            points = 5
        return super().comment_on_post(message, post, points)
    def __str__(self):


class Post:

    def __init__(self, author, message):
        # print(message)
        self.message = message
        self.author = author
        self.comments = []

    def edit_message(self, new_message):
        self.post = new_message


class Comment:
    def __init__(self, author, message, post):
        self.author = author
        self.message = message
        self.post = post

    def edit_message(self, new_message):
        self.message = new_message


e1 = Employee("Jimmy", "j@gmail.com", "07/18/21")
e2 = Employee("Dina", "d@gmail.com", "12/15/66")
e1.post_message("hi i am jimmy")
# e2.post_message("hi I am dina")

e3 = Engineer("Toby", "t@gmail", "01/28/23")
e4 = Marketer("Teresa", "t@gmail", "02/25/27")

print(Employee.employee_count)
print(e1.posts)
print(e3.name)
print(e4.department)
# print(e1)
# print(repr(e1))
