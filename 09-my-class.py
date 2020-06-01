class Car:
    def __init__(self, **kwargs):
        self._make = kwargs['make'] if 'make' in kwargs else 'BMW'
        self._model = kwargs['model'] if 'model' in kwargs else 'MX5'
        self._year = kwargs['year'] if 'year' in kwargs else '2020'

    def make(self, mk=None):
        if mk:
            self._make = mk
        return self._make

    def model(self, md=None):
        if md:
            self._model = md
        return self._model

    def year(self, y=None):
        if y:
            self._year = y
        return self._year

    def __str__(self):
        return f'{self._year} {self._make} {self._model}'


def main():
    c1 = Car(model='Civic', make='Honda', year=2020)
    print(c1)
    c1.model('Accord')
    print(c1)
    c2 = Car()
    print(c2)
    print(c1 != c2)


if __name__ == "__main__":
    main()
