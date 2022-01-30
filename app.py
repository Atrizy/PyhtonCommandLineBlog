from unittest import result
import newpost as n

selection = input(f"1: Write a new entry or 2: See all posting: ")


if selection == '1':
    username = input(f"What is your username: ")
    post_content = input(f"Type your blog entry: ")
    n.add_new_post(post_content, username)
    print("Blog posted!")
    exit()