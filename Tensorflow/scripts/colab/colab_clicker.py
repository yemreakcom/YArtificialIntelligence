from time import sleep, time

from pynput import keyboard, mouse

mController = mouse.Controller()
kController = keyboard.Controller()


LEFT = (409, 407)
RIGHT = (1587, 407)

# 409,575
# 1587 487


def scroll_page(position):
    mController.position = position
    mController.click(mouse.Button.left, 1)
    kController.press(keyboard.Key.down)
    sleep(0.2)
    kController.release(keyboard.Key.down)


def scroll_loop(delay: float, debug=False):
    if debug:
        count = 0
        now = time()
        print("---------------------------------------------------")

    while True:
        sleep(10)
        remaining_time = delay - int(time() - now)

        if debug:
            print(f"Yenilenme Sayısı: {count}")
            print(f"Yeni tıklamaya kalan saniye saniye: {remaining_time}")
            print("---------------------------------------------------")

        if remaining_time == 0:
            scroll_page(LEFT)
            scroll_page(RIGHT)
            count += 1 if debug else None


scroll_loop(500, debug=True)
