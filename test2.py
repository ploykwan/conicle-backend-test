# Run python3 test2.py

author_list = [{'id': 1, 'name': 'Herman Melville'},
               {'id': 2, 'name': 'Newton Man'}]
book_list = [{'id': 1, 'name': 'Billy Budd'}, {
    'id': 2, 'name': 'Physic Intemediate'}, {'id': 3, 'name': 'Sci fi realy'}]
author_book_map = [{'author_id': 1, 'book_id': 1}, {'author_id': 2, 'book_id': 2}, {
    'author_id': 1, 'book_id': 3}, {'author_id': 2, 'book_id': 3}]


id_to_author_dict = {author_dict['id']: author_dict for author_dict in author_list}
id_to_book_dict = {book_dict['id']: book_dict for book_dict in book_list}
book_list_result = []
for author_book_map_dict in author_book_map:
    book_data_dict = id_to_book_dict[author_book_map_dict['book_id']]
    if 'author_list' not in book_data_dict:
        book_data_dict['author_list'] = []
    book_data_dict['author_list'].append(id_to_author_dict[author_book_map_dict['author_id']])
    id_to_book_dict[author_book_map_dict['book_id']].update(**book_data_dict)

book_data_dict_list = list(id_to_book_dict.values())

print('====== Result ======')
print(f'book_list = {book_data_dict_list}')
