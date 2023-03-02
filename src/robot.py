from termcolor import colored
from restaurant_csv import RestaurantCsv

class Robot(object):
    def test(self):
        csv = RestaurantCsv()
        csv.get_restaurant_by_rank()

    def greeting(self):
        text = 'こんにちは!私はRobokoです。あなたの名前は何ですか?'
        self.name = self.input_capitalize(text)

    def which_restaurant(self):
        text = '{} さん。どこのレストランが好きですか?'.format(self.name)
        self.restaurant = self.input_capitalize(text)
        
    def save(self):
        csv = RestaurantCsv()
        csv.write(self.restaurant)
        csv.read()
    
    def recommend_restaurant(self, rank = 1):
        if not self.recommend_exists(): return
        
        def get_restaurant():
            csv = RestaurantCsv(rank)
            return csv.get_restaurant_by_rank()
        
        restaurant = get_restaurant()
        
        if restaurant == False: return

        text = ('私のオススメのレストランは、 {}です。\n'
                'このレストランは好きですか? [Yes/No]\n').format(restaurant)
        choice = self.input_yes_no_result(text)
        
        if choice == False:
            next = rank + 1
            self.recommend_restaurant(next)
    
    def recommend_exists(self):
        csv = RestaurantCsv()
        return csv.exists()
    
    def get_top_ranked_restaurant(self):
        csv = RestaurantCsv()
        return csv.get_top_ranked()
    
    def last_bow(self):
        text = ('{} さんありがとうございました。\n'
                '良い一日を!さようなら。\n').format(self.name)
        print(self.text_decorator(text))
    
    def text_decorator(self, text):
        def green_text(text, color='green'):
            return colored(text, color)
        
        def line_decoration():
            text = '=' * 80
            return green_text(text)
        
        return line_decoration() + '\n' + green_text(text) + '\n' + line_decoration() + '\n'
    
    def input_yes_no_result(self, text):
        choice = input(self.text_decorator(text)).lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            self.input_yes_no_result(text)
    
    def input_capitalize(self, text):
        titled = input(self.text_decorator(text)).title()
        return titled