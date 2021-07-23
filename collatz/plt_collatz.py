import matplotlib.pyplot as plt
import numpy as np

def collatz(x):
    step = 0
    while True:
        if x == 1 :return step
        step += 1
        
        if (x % 2): x = (x*3)+1
        else: x /= 2

def map_collatz(X):
    return  np.array(list(map(collatz, X)))

def main():
    try:
        fig, ax = plt.subplots(1, 1)
        x = np.arange(1, 50, 1)
        y = map_collatz(x)
        
        lines, = ax.plot(x, y)
        
        while True:
            x += 1
            y = map_collatz(x)
            
            lines.set_data(x, y)
            ax.set_xlim((x.min(), x.max()))
            ax.set_ylim((0, y.max()+10))
            plt.pause(.01)
            
    except Exception as e:
        print(e)
    finally:
        print("Terminated.")
        

if __name__ == "__main__":
    main()
