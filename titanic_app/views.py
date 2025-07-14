from django.shortcuts import render
import pandas as pd
import os

def index(request):
  csv_path = os.path.join('titanic_app', 'static', 'titanic_cleaned.csv')
  
  df = pd.read_csv(csv_path)
  df_html = df.head(15).to_html(classes='table table-dark table-striped', index=False)
  
  context = {
      'data_table': df_html,
      'images': [
        'imgs/plot1.png', 'imgs/plot2.png', 'imgs/plot3.png',
        'imgs/plot4.png', 'imgs/plot5.png', 'imgs/plot6.png',
        'imgs/plot7.png', 'imgs/plot8.png', 'imgs/plot9.png',
      ]
    }
  return render(request, 'index.html', context)

# Create your views here.
