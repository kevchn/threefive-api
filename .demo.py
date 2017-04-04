# Example search by location
print("---")
pprint(yelp_api.search_query(term='ice cream', location='frederick, md', sort_by='rating', limit=3))

# Example phone search
print("---")
pprint(yelp_api.phone_search_query(phone='+13193375512'))

# Example transaction query
print("---")
pprint(yelp_api.transaction_search_query(transaction_type='delivery', location='dallas, tx'))

# Example business query
print("---")
pprint(yelp_api.business_query(id='amys-ice-creams-austin-3'))

# Example reviews query
print("---")
pprint(yelp_api.reviews_query(id='amys-ice-creams-austin-3'))

# Example autocomplete query
print("---")
pprint(yelp_api.autocomplete_query(text='Hambur', longitude=-91.5327, latitude=41.6560))