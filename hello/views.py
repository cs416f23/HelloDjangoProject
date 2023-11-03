# Import necessary modules
from django.shortcuts import render


# Define the hello function that takes a Django request object,
# and two parameters: name and last_name.
def hello(request, first_name, last_name):

    # Create a context dictionary to pass data to the template.
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'states': ['CT', 'CA', 'MA'],
        'user_type': 'admin'
    }

    # Render the 'hello.html' template with the provided context data,
    # and return the result as an HTTP response.
    return render(request, 'hello.html', context)
