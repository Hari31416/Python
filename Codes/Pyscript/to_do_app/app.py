from pyodide import create_proxy


add_item_text = document.querySelector("#new-item")
add_btn = document.querySelector("#new-item-btn")
the_list = document.querySelector(".list-group")


def check(event):
    console.log(the_list)
    for child in the_list.children:
        if child.children[0].checked:
            child.classList.add("crossed")
        else:
            child.classList.remove("crossed")


for child in the_list.children:
    child.children[0].addEventListener("click", create_proxy(check))


def add_item(event):
    if add_item_text.value:
        # Create the list item
        item = document.createElement("li")
        item.classList.add("list-group-item")
        item.innerText = add_item_text.value
        # Create the checkbox
        checkbox = document.createElement("input")
        checkbox.setAttribute("type", "checkbox")
        checkbox.classList.add("checkbox")
        item.prepend(checkbox)
        the_list.appendChild(item)


add_btn.addEventListener("click", create_proxy(add_item))
