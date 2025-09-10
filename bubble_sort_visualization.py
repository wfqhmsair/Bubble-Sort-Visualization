import time
import os

def clear_console():
    # Clear the console for Windows, Mac, and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def visualize(lst, highlight_indices=None):
    # Print the list, highlighting any indices in highlight_indices
    highlight_indices = highlight_indices or []
    visual = []
    for i, num in enumerate(lst):
        if i in highlight_indices:
            visual.append(f"[{num}]")
        else:
            visual.append(f" {num} ")
    print(' '.join(visual))

def bubble_sort_visualize(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            clear_console()
            print(f"Step: i={i}, j={j}")
            visualize(lst, highlight_indices=[j, j+1])
            time.sleep(0.5)
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                clear_console()
                print(f"Swapping {lst[j+1]} and {lst[j]}")
                visualize(lst, highlight_indices=[j, j+1])
                time.sleep(0.5)

    clear_console()
    print("Sorted list:")
    visualize(lst)

if __name__ == "__main__":
    sample = [5, 1, 4, 2, 8]
    print("Initial list:")
    visualize(sample)
    time.sleep(1)
    bubble_sort_visualize(sample)
