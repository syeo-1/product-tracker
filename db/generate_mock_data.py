import string, random

def generate_mock_data():
    '''
    function to create some fake data for api to display to see if things work as expected.
    Will only generate one row at a time! This is to imitate what the actual scraping program will do
    '''
    dummy_link = 'https://google.com'

    # random.seed(5)
    
    dummy_dict = dict()
    # random_price = round(random.uniform(0, 100), 2)
    # print(random_price)
    for c in string.ascii_lowercase:
        dummy_dict[c] = {
            'price': round(random.uniform(0, 100), 2),
            'url': dummy_link
        }
    # print(dummy_dict)
    return dummy_dict

if __name__ == '__main__':
    generate_mock_data()