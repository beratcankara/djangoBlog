import random
from datetime import datetime, timedelta

def generate_random_date(time):
    dates = []
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    # Başlangıç ve bitiş tarihlerini datetime nesnelerine dönüştürme
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    for i in time:
        
    # Başlangıç ve bitiş tarihleri arasında rastgele bir timedelta oluşturma
        random_delta = random.randrange((end_date - start_date).days)    
        # Başlangıç tarihine rastgele timedelta ekleyerek rastgele bir tarih oluşturma
        random_date = start_date + timedelta(days=random_delta)
        dates.append(random_date)
    
    return dates