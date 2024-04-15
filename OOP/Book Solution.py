# class Book:
#
#     def __init__(self, isbn, title, author, publisher, pages, price, copies):
#         self.isbn = isbn
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#         self.pages = pages
#         self.price = price
#         self.copies = copies
#
#     def display(self):
#         print(self.title)
#         print(f'ISBN : {self.isbn}')
#         print(f'Price : {self.price}')
#         print(f'Number of copies : {self.copies}')
#         print('.' * 50)
#
#     def in_stock(self):
#         return True if self.copies > 0 else False
#
#     def sell(self):
#         if self.in_stock():
#             self.copies -= 1
#         else:
#             print('The book is out of stock')
#
#
# book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
# book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
# book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
# book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)
#
# book1.display()
# book2.display()
# book3.display()
# book4.display()

class Booking:
    def __init__(self, booking_id, booking_date, booking_time, booking_status, booking_amount):
        self.booking_id = booking_id
        self.booking_date = booking_date
        self.booking_time = booking_time
        self.booking_status = booking_status
        self.booking_amount = booking_amount

    def display(self):
        print(f'Booking ID : {self.booking_id}')
        print(f'Booking Date : {self.booking_date}')
        print(f'Booking Time : {self.booking_time}')
        print(f'Booking Status : {self.booking_status}')
        print(f'Booking Amount : {self.booking_amount}')
        print('.' * 50)

    def cancel(self):
        if self.booking_status == 'Confirmed':
            self.booking_status = 'Cancelled'
        else:
            print('Booking is already cancelled')

    def confirm(self):
        if self.booking_status == 'Cancelled':
            print('Booking is already cancelled')
        else:
            self.booking_status = 'Confirmed'

    def check_status(self):
        return self.booking_status

    def pay(self, amount):
        if self.booking_status == 'Confirmed':
            self.booking_amount -= amount
        else:
            print('Booking is not confirmed')

    def check_amount(self):
        return self.booking_amount

    def check_date(self):
        return self.booking_date

    def check_time(self):
        return self.booking_time


booking1 = Booking(1, '2021-09-01', '10:00', 'Confirmed', 2000)
booking2 = Booking(2, '2021-09-02', '11:00', 'Confirmed', 3000)
booking3 = Booking(3, '2021-09-03', '12:00', 'Cancelled', 4000)
booking4 = Booking(4, '2021-09-04', '13:00', 'Confirmed', 5000)

booking1.display()
booking2.display()
booking3.display()
booking4.display()

booking1.cancel()
booking1.display()

booking2.confirm()
booking2.display()

booking3.cancel()
booking3.display()

booking4.pay(1000)
booking4.display()

print(booking4.check_amount())
print(booking4.check_status())
print(booking4.check_date())


