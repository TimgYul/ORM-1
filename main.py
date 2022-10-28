import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:12121987@localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

    
def search_publisher_name():
    query = session.query(Shop).join(Stock).join(Book).join(Publisher)
    search_name = input('Введите имя (name) издателя: ')
    result = query.filter(Publisher.name == search_name)
    for res in result.all():
        print(f'Издатель "{search_name}" найден в магазине "{res.name}" с идентификатором {res.id}')


def search_publisher_id():
    query = session.query(Shop).join(Stock).join(Book).join(Publisher)
    id = input('Введите идентификатор (id) издателя: ')
    result = query.filter(Publisher.id == id)
    for res in result.all():
        print( f'Издатель c id: {id} найден в магазине "{res.name}" '
               f'с идентификатором {res.id}')
        
#def get_data():
#    with open('data.json', 'r') as fd:
        # data = json.load(fd)

        # for record in data:
        #     model = {
        #         'publisher': Publisher,
        #         'shop': Shop,
        #         'book': Book,
        #         'stock': Stock,
        #         'sale': Sale,
        #     }[record.get('model')]
        #     session.add(model(id=record.get('pk'), **record.get('fields')))

if __name__ == '__main__':
    # get_data()
    search_publisher_name()
    search_publisher_id()
        
session.close()