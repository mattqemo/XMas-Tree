# comment from Ben
# adapted from Engineer Man on YouTube

import threading
import random
import os
import time

mutex = threading.Lock()
tree = list(open('tree.txt').read().rstrip())

def colored_dot(color):
    if color == 'red':
        return f'\033[91m●\033[0m'
    if color == 'green':
        return f'\033[92m●\033[0m'
    if color == 'yellow':
        return f'\033[93m●\033[0m'
    if color == 'blue':
        return f'\033[94m●\033[0m'

def lights(color, indexes):
    off = True
    print("hello")
    while True:
        for idx in indexes:
            tree[idx] = colored_dot(color) if off else '●'
        
        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(tree))
        mutex.release()
        
        off = not off
        
        time.sleep(random.uniform(.25, 2))


yellow = []
red = []
green = []
blue = []


for i, color in enumerate(tree):
    if color == 'R':
        red.append(i)
        tree[i] = f'\033[91m●\033[0m'
    if color == 'G':
        green.append(i)
        tree[i] = f'\033[92m●\033[0m'
    if color == 'Y':
        yellow.append(i)
        tree[i] = f'\033[93m●\033[0m'
    if color == 'B':
        blue.append(i)
        tree[i] = f'\033[94m●\033[0m'

#create threads
ty = threading.Thread(target=lights, args=('yellow', yellow))
tr = threading.Thread(target=lights, args=('red', red))
tg = threading.Thread(target=lights, args=('green', green))
tb = threading .Thread(target=lights, args=('blue', blue))

for t in [ty, tr, tg, tb]:
    t.start()
for t in [ty, tr, tg, tb]:
    t.join()
