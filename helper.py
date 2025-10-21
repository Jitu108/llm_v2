from IPython.display import display, Markdown, update_display

def iterate_and_print_list(list):
    for index, item in enumerate(list):
        #display(Markdown(f"**Item {index + 1}:** {item}"))
        print(item)