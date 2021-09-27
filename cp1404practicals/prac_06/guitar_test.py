from prac_06.guitar import Guitar

first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Some other guitar", 2013, 3045.58)

print(first_guitar.get_age())
print(another_guitar.get_age())
print(first_guitar.is_vintage())
print(another_guitar.is_vintage())
