http_status = 500

match http_status: # the match statement compares values and several different condition until one of them is met
    case 200 | 201:
        print('Success')
    case 400:
        print('Bad request')
    case 500 | 501:
        print('Server error')
    case _:
        print('Unknown')