from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import TabelaPessoa

def index(request):
    return render(request, "home/index.html")

def export_to_excel(request):
    # Query the data from the database
    data = TabelaPessoa.objects.all().values()

    # Convert the data to a DataFrame
    df = pd.DataFrame(list(data))

    # Create an HttpResponse object with the appropriate Excel header
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tabela_pessoa.xlsx"'

    # Use Pandas to write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response
