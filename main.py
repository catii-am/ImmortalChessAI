import asyncio
import time
import chess
import chess.engine
import pgnToFen
import SearchPos
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Selenium():
    def __init__(self, mnemonic) -> None:
        self.mnemonicc = mnemonic
        pass

    def start_driver(self):
        # time.sleep(random.randint(1,10))
        options = uc.ChromeOptions()

        options.add_argument('--no-first-run')
        options.add_argument('--no-service-autorun')
        options.add_argument('--password-store=basic')
        options.add_argument('--load-extension=C:\\Users\\admin\\PycharmProjects\\Immortal AI\\utils\\MM')

        driver = uc.Chrome(
            options=options
        )
        self.driver = driver
        return

    def take_element(self, path, timeout=20, delay=0):
        element = ""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            time.sleep(delay)
            self.driver.find_element(By.XPATH, path).click()
        except Exception as e:
            print(f"No element after {timeout} seconds of waiting!!!\n{path}")
            return None

    def send_text(self, path, text, timeout=20, delay=0):
        element = ""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            time.sleep(delay)
            self.driver.find_element(By.XPATH, path).send_keys(text)

        except Exception as e:
            print(f"No input after {timeout} seconds of waiting!!!\n{path}")
            return None
        if element is not None:
            time.sleep(delay)
            return element
        else:
            print(f"NO SUCH ELEMENT!\n Path: {path}")
        self.driver.execute_script("""document.body.style.backgroundColor = 'green'""")
        input()

    def open_site(self, url):
        self.driver.get(url)

    def lastWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def refresh(self):
        self.driver.refresh()

class Metamask(Selenium):
    def __init__(self, mnemonic, driver) -> None:
        self.mnemonic = mnemonic
        self.driver = driver
        pass

    def install_MM(self):
        while True:
            if len(self.driver.window_handles) > 1:
                time.sleep(1)
                self.lastWindow()
                self.driver.close()
                self.lastWindow()
                print('MM установлен')
                break
            else:
                time.sleep(1)

    def create_wallet(self, mnemonic):
        while True:
            try:
                time.sleep(1)
                self.driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
                break
            except Exception as e:
                self.refresh()

        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]')
        self.send_text('//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input', mnemonic)
        self.send_text('//*[@id="password"]', '12345678')
        self.send_text('//*[@id="confirm-password"]', '12345678')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/form/button')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/button')
        print('Кошелек импортирован')

class Immortall(Selenium):
    def __init__(self, driver) -> None:
        self.driver = driver
        pass

    def login_to_site(self):
        self.open_site('https://immortal.game/login')
        time.sleep(3)
        self.take_element('/html/body/div[2]/div/div/div[2]/div[1]/div/button')
        while True:
            if len(self.driver.window_handles) > 1:
                self.lastWindow()
                self.take_element('//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]')
                self.take_element('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')
                time.sleep(3)
                self.lastWindow()
                self.take_element('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]')
                try:
                    time.sleep(3)
                    self.lastWindow()
                    self.take_element('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]')
                except:
                    pass
                time.sleep(1)
                self.lastWindow()
                print('Успешно авторизовались')
                break
            else:
                time.sleep(1)

    def start_game(self):
        self.open_site('https://immortal.game/play')
        input('Настройте игру и нажмите Enter...')

    def make_move(self):
        pass

async def main() -> None:
    mnemonic = 'fragile mad plate garment aunt reject fat dragon rely cheap island warm'
    pgnConverter = pgnToFen.PgnToFen()
    player = None
    start_fen = ''
    searchPos = SearchPos.SearchPos()

    print('Запуск нейросети...')
    transport, engine = await chess.engine.popen_uci(
        r"C:\Users\admin\Desktop\nibbler-2.3.6-windows\chess engine\lc0.exe")
    time.sleep(10)
    print('Нейросеть запущена\nЗапуск браузера...')

    driver = ''
    driver_session = Selenium(mnemonic)
    driver = driver_session.start_driver()
    metamask = Metamask(mnemonic, driver)
    immortall = Immortall(driver)
    print('Браузер запущен')

    metamask.install_MM()
    metamask.create_wallet()

    immortall.login_to_site()

    while True:
        immortall.start_game()
        player = input('w or b? ')
        if player == 'w':
            if fen is not None:
                board = chess.Board(fen)
            else:
                board = chess.Board(start_fen)
            info = await engine.analyse(board, chess.engine.Limit(depth=1))
            move = info["pv"]
            move_ = str(move).split("'")[1]
            x1 = searchPos.GetX1(move_)
            y1 = searchPos.GetY1(move_)
            x2 = searchPos.GetX2(move_)
            y2 = searchPos.GetY2(move_)

            # if len(list(move_)) > 4:
            #     x3 = searchPos.GetX3(move_)
            #     y3 = searchPos.GetY3(move_)
            time.sleep(0.5)
            move_ = input('Твой ход: ')

            while True:
                board = chess.Board(start_fen)
                info = await engine.analyse(board, chess.engine.Limit(depth=1))

                print(info)
                move = info["pv"]
                move_ = str(move).split("'")[1]
                x1 = SearchPos.SearchPos.GetX1(move_)
                print(f'ход на {move_}')
                pgnConverter.move(move_)
                print('ход сделан')

                time.sleep(0.5)

                move_ = input('Твой ход: ')
                if move_ != 'gg':
                    pgnConverter.move(move_)
                    fen_ = str(pgnConverter.getFullFen())
                    print(f'полный fen: {fen_}')
                    fen = f"{fen_.split(' ')[0]} {fen_.split(' ')[1]}"
                    print(f'разделеный fen: {fen}')
                else:
                    print('Победа!')
                    break

    await engine.quit()

if __name__ == '__main__':
    asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
    asyncio.run(main())