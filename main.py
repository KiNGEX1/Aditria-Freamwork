import os
import time
from tqdm import tqdm
from colorama import init, Fore, Style

# Initialize colorama
init()

def starting_animation():
    stages = [
        "Loading.",
        "Loading..",
        "Loading...",
        "Starting the framework.",
        "Starting the framework..",
        "Starting the framework...",
    ]

    # Color settings
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

    for i in range(2):  # Loop through twice
        for color, stage in zip(colors, stages):
            print(f"{color}{stage}{Style.RESET_ALL}")
            time.sleep(0.5)
            print("\033[F" + " " * len(stage) + "\033[F")  # Clear the line

    # Final stage with progress bar
    print(Fore.GREEN + "Initialization Complete:" + Style.RESET_ALL)
    for _ in tqdm(range(100), desc=Fore.GREEN + "Progress" + Style.RESET_ALL, ncols=75, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.02)

def print_banner():
    banner = """
\033[1;30m
  ___        _ _ _        _
 / _ \\     | (_) |      (_)
/ /_\\ \\ __| |_| |_ _ __ _  __ 
|  _  |/ _` | | __| '__| |/ _` |
| | | | (_| | | |_| |  | | (_| |
\_| |_/\__,_|_|\__|_|  |_|\__,_| Framework
\033[0m
"""
    print(banner)

def disclaimer_and_agreement():
    print_banner()
    
    # Check if user has previously agreed
    if os.path.exists("user_agreed.txt"):
        with open("user_agreed.txt", "r") as f:
            agreed = f.read().strip()
            if agreed.lower() == "yes":
                starting_animation()
                os.system("python YWRpdHJpYS1mcmVhbXdvcms=")
                return
    
    # If user has not previously agreed or file doesn't exist, prompt for agreement
    print("Disclaimer: This tool is provided for educational purposes only.")
    print("The author is not responsible for any damage caused by the use of this tool.")
    print()
    agreement = input("Do you agree? (Yes/No): ").strip().lower()
    
    if agreement == "yes":
        # Write agreement to file for future sessions
        with open("user_agreed.txt", "w") as f:
            f.write("Yes")
        starting_animation()
        os.system("python YWRpdHJpYS1mcmVhbXdvcms=")
    else:
        os.system("exit")

if __name__ == "__main__":
    os.system('clear')
    disclaimer_and_agreement()