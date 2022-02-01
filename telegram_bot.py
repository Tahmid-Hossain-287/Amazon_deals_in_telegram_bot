from product_link_scrape import launch_deals_page, driver, WebDriverWait, By, EC
import telegram, re
from secrets import token, group_id
from time import sleep

# Note that your bot will not be able to send more than 20 messages per minute to the same group.
bot = telegram.Bot(token=str(token))
updates = bot.get_updates()


def get_product_information():
    try:
        discount_amount = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.CLASS_NAME, 'a-span12.a-color-price.a-size-base')
                        )
                    )
        raw_discount = str(discount_amount.text)
        discount_amount = (re.search('\((.*?)\)', raw_discount)).group(1)
        
        saved_amount_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'a-span12.a-color-price.a-size-base')
            )
        )

        saved_amount = re.search('^(.*?)\€', saved_amount_element.text).group(0)

        original_price_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'a-span12.a-color-secondary.a-size-base')
            )
        )
        
        original_price = re.search('^(.*?)\€', original_price_element.text).group(0)
        

        offer_price_element = WebDriverWait(driver, 5).until(
             EC.presence_of_element_located(
                (By.CLASS_NAME, 'a-price.a-text-price.a-size-medium.apexPriceToPay')
            )
        )

        offer_price = re.search('^(.*?)\€', offer_price_element.text).group(0)

        return discount_amount, original_price, offer_price, saved_amount
        # print(f' Saved money is  {saved_amount}.\n Original price was {original_price}.\n The offer price is {offer_price}.')
        
    except Exception as e:
        print(e)
        pass

def send_telegram_message():
    with open('deals.txt') as file:
        lines = file.readlines()
        for line in lines:
            try:
                driver.get(line)
                sleep(3)
                discount = get_product_information()
                discount_amount = discount[0]
                original_price = discount[1]
                offer_price = discount[2]
                saved_amount = discount[3]
                template = f" 🔥🔥 {discount_amount} OFF 🔥🔥\n 🤑 SUPER SCONTO 🤑\n 💣 Solo {offer_price} ❌Invece di {original_price}\n 💰💲 Risparmiare fino a {saved_amount} 💰💲\n 👉 Apri su Amazon {line}"
                bot.send_message(text= template, chat_id=group_id)
            except Exception as e:
                print(e)
                continue    

            
if __name__ == "__main__":
    launch_deals_page()
    send_telegram_message()

