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

        image = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.ID, 'landingImage')
            )
        )

        image_link = image.get_attribute('src')

        return discount_amount, original_price, offer_price, saved_amount, image_link
        
    except Exception as e:
        print(e)
        pass

def send_telegram_message():
    with open('deals.txt') as file:
        lines = file.readlines()
        for line in lines:
            try:
                driver.get(line)
                sleep(3) # Pausing is important so as not to hit the limit of telegram message limit of one message per three second.
                discount = get_product_information()
                discount_amount = discount[0]
                original_price = discount[1]
                offer_price = discount[2]
                saved_amount = discount[3]
                image_link = discount[4]
                long_url = driver.current_url
                template = f" 🔥🔥 {discount_amount} OFF 🔥🔥\n 🤑 SUPER SCONTO 🤑\n 💣 SOLO {offer_price} ❌Invece di {original_price}\n 💰💲 Risparmi {saved_amount} 💰💲\n 👉 Apri su Amazon {line}"
                button_1 = telegram.InlineKeyboardButton(text='📩Invita un amico', url='https://t.me/share/url?url=https://t.me/+DRsQpE_ZD59kODE1')
                button_2 = telegram.InlineKeyboardButton(text="📱Apri nell'app", url=f'{long_url}')
                keyboard_inline = telegram.InlineKeyboardMarkup([[button_1, button_2]])
                bot.send_message(text= f"[\n]({image_link}){template}", parse_mode='markdown', chat_id=group_id, reply_markup=keyboard_inline)
            except Exception as e:
                print(e)
                continue    
    
    with open('deals.txt', 'w'):
        pass # Clears deals.txt after sending all the advertisements.
    driver.quit()
    

if __name__ == "__main__":
    launch_deals_page()
    send_telegram_message()

