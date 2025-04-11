from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Book(models.Model):
    """
    Model representing a book in the library.
    """
    title = models.CharField(max_length=255, help_text="Enter the book title")
    author = models.CharField(max_length=255, help_text="Enter the book author")
    genre = models.CharField(max_length=100, help_text="Enter the book genre")
    isbn = models.CharField(max_length=13, unique=True, help_text="Enter the 13-character ISBN number")
    available_copies = models.PositiveIntegerField(default=1, help_text="Number of copies available")

    def __str__(self):
        return f"{self.title} by {self.author}"
    
#model representing a library member (extending Django's built-in user model).
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('admin','Admin'), ('member','Member')], default='member')
        
    def __str__(self):
        return self.user.username
#models representing a librarian who manages library operations.
class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True, help_text="Enter the librarian's employee ID")
    
    def __str__(self):
        return f"librarian: {self.user.username}"
    
    #model represent a book borrowing record.
    class BorrowRecord(models.Model):

        member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrowed_books")
        book = models.ForeignKey(Book, on_delete=models.CASCADE)
        borrow_date = models.DateField(auto_now_add=True)
        return_date = models.DateField(null=True, blank=True, help_text="Expected retuen date")

        def __str__(self):
            return f"{self.member.user.username} borrowed {self.book.title}"