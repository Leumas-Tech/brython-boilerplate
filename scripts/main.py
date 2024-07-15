from browser import document, alert

def greet(event):
    alert("Hello from Python!")

document["mybutton"].bind("click", greet)
