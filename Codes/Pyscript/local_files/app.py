import asyncio
import js
from js import document
from pyodide import create_proxy


def read_complete(event):
    # event is ProgressEvent
    # console.log('read_complete')

    image = document.getElementById("image")
    image.src = event.target.result


async def process_file(x):
    fileList = document.getElementById("myfile").files

    for f in fileList:
        # reader is a pyodide.JsProxy
        reader = js.FileReader.new()

        # Create a Python proxy for the callback function
        onload_event = create_proxy(read_complete)

        reader.onload = onload_event

        reader.readAsDataURL(f)

    return


def setup():
    # Create a Python proxy for the callback function
    file_event = create_proxy(process_file)

    # Set the listener to the callback
    e = document.getElementById("myfile")
    e.addEventListener("change", file_event, False)


setup()
image = document.getElementById("image")
print(image.src)
