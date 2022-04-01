from tkinter import *
import pandas as pd
import random
from bs4 import BeautifulSoup
import requests
import itertools
BACKGROUND_COLOR = "#B1DDC6"

# Create a list of indexes to be learned
# with open(file="data/to_learn.txt", mode="w") as file:
#     to_write_in_file = ""
#     for i in range(0,101):
#         to_write_in_file += str(i)+"\n"
#     print(to_write_in_file)
#     file.write(to_write_in_file)

# Reading data
data = pd.read_csv("data/list_of_movies.csv")
# print(data.iloc[100])

# Generate random French words


def random_french():
    ri = random.randint(0, 100)
    return ri, data.iloc[ri]["Movie_name"]


def flip_card(index):
    pass
    # canvas.itemconfig(canvas_image, image=card_back_img)
    # canvas.itemconfig(title, text="Movie_name", fill="white")
    # canvas.itemconfig(word, text=data.iloc[index]["Movie_name"], fill="white")


def right_command():
    # global flip_timer
    # if flip_timer != 0:
    #     window.after_cancel(flip_timer)
    index, french_word = random_french()
    with open(file="data/to_learn.txt", mode="r") as file:
        indexes = file.readlines()
    if index in indexes:
        right_command()
    else:
        canvas.itemconfig(title, text="Movie", fill="black")
        canvas.itemconfig(word, text=french_word, fill="black")
        canvas.itemconfig(canvas_image, image=card_front_img)
        with open(file="data/to_learn.txt", mode="a") as file:
            file.write(str(index))
            file.write("\n")
        # flip_timer = window.after(3000, flip_card, index)

    # window.after_cancel(after_id)


def left_command():
    # global flip_timer
    # if flip_timer != 0:
    #     window.after_cancel(flip_timer)
    canvas.itemconfig(title, text="Movie", fill="black")
    index, french_word = random_french()
    canvas.itemconfig(word, text=french_word, fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    # flip_timer = window.after(3000, flip_card, index)
    # window.after_cancel(after_id)

# Creating the UI

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = 0

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 20, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_command)
right_button.grid(column=1, row=1)

left_image = PhotoImage(file="images/wrong.png")
left_button = Button(image=left_image, highlightthickness=0, command=left_command)
left_button.grid(column=0, row=1)

left_command()

window.mainloop()

#
# response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
# soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())
#<h3 class="jsx-4245974604">99) Groundhog Day</h3>
# print(soup.title.string)

# heading = soup.select_all('h2')
# heading_data = heading.text
# print(heading)

# heading2 = soup.find_all('h1')
# print(heading2)

cl = "jsx-3523802742 listicle-item"

# mt =soup.find_all('div', class_=cl)
# print(mt[1])

# im = [i["alt"] for i in soup.find_all("img")]
# # print(len(im))
# not_a_movie =['Facebook', 'Twitter', 'Pinterest']
# counter = itertools.count(1)
# list_of_movies = [i for i in im if (im.count(i) == 1) & (i not in not_a_movie)]
# # print(im)
# # print(len(im))
# # list_of_movies.to_csv("list_of_movies.csv", index=True)
# list_of_movies = ""
# with open("movies.txt", "r") as f:
#     list_of_movies = f.read().splitlines()
# 
# dict_of_movies = {"Movie_name": list_of_movies}
# df = pd.DataFrame(dict_of_movies)
# df.to_csv("list_of_movies.csv", index=True)
# print(list_of_movies)
# list_of_movies.to_csv("list_of_movies.csv", index=True)

# movie_conntainer_text = [m.text for m in ]

# print(movie_conntainer_text)

# print("List of all the h1, h2, h3 :")
# for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
#     print(heading.name + ' ' + heading.text.strip())

# tags = {tag.name for tag in soup.find_all()}
# class_list = set()
# iterate all tags
# for tag in tags:
#
#     # find all element of tag
#     for i in soup.find_all(tag):
#
#         # if tag has attribute of class
#         if i.has_attr("class"):
#
#             if len(i['class']) != 0:
#                 class_list.add(" ".join(i['class']))

# print(class_list)

# print(soup)
# movies_list = [title.text for title in soup.find_all("h3.jsx-4245974604")]
# print(movies_list)
