# if ... elif ... else
amount_hansueli = 1000

def compare_amount(amount):
    if amount < amount_hansueli:
        print("Du bisch ja no ermer als de Hansueli")
    elif amount == amount_hansueli:
        print("Du bisch gliich arm wie de Hansueli")
    else:
        print("Du bisch richer als de Hansueli")

# switch case
compare_amount(10000000)

def switch_color(color):
    match color:
        case 'red':
            return "wrong color"
        case 'blue':
            return "wrong color"
        case 'green':
            return "wrong color"
        case 'magenta':
            return "right color"