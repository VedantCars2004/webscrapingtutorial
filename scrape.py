from bs4 import BeautifulSoup

def find_vehicle_types():
    with open('home.html', "r") as html_file:
        content = html_file.read()
        #print(content)
        soup = BeautifulSoup(content, 'lxml')
        # print(soup.prettify())
        vehicle_type_tags = soup.find_all('h3') 
        # tags = soup.find('p') # to find the first occurence
        for vehicle_type in vehicle_type_tags:
            print(vehicle_type.text)
            # use vehicle_type.text to print out text within h3 tags
        
def button():
    with open('home.html', 'r') as html_file:
        # read in content and initialize soup
        content = html_file.read()
        soup = BeautifulSoup(content, 'lxml')
        # load in car_cards (reads in all div boxes with class card), and iterate thru car div boxes and print them 
        car_cards = soup.find_all('div', class_= 'card')
        for car in car_cards:
            # in a div box, we can extract certain tags from the div boxes, using car.h3 
            # to get the text from the tag, we just have to add a .text
            car_type = car.h3.text
            car_desc = car.find('p').get_text() # the .find() method can be used to find p as well 
            # for buttons, we can use car.a.text but if button is not a and a class btn for example, we can use the 
            # .find() method where we find 'button' type and class whatever the name is
            car_button = car.find('button', class_='btn').get_text()
            print(car_button)


if __name__ == "__main__":
    # find_vehicle_types() # run command to find vehicle types
    button()