from django.http import HttpResponse

def home_page(request):
    # Log a message indicating that the project or app has been loaded.
    print("Project/App is loaded.")

    # Return an HTTP response
    return HttpResponse("Setup is working fine.")