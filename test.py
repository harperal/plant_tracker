import time


if __name__ == '__main__':

    file = open("run.txt", "w")
    file.write("run\n")
    file.close()

    time.sleep(1)
    with open('fertilizer.txt', 'r') as ffile:
        ftext = ffile.readlines()
    with open('water.txt', 'r') as wfile:
        wtext = wfile.readlines()
    with open('date.txt', 'r') as file3:
        text3 = file3.readline()

    print(f"Today's Date: {text3}")
    print(f"The plants that need watered today:{wtext}")
    print(f"The plants that need fertilized today:{ftext}")





