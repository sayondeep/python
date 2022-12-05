import requests
def solve(name,id):
    sum = 0
    cnt = 0
    r = requests.get("https://jsonmock.hackerrank.com/api/medical_records").json()
    total_pages = r['total_pages']
    for i in range(1,total_pages+1):
        r = requests.get("https://jsonmock.hackerrank.com/api/medical_records?page="+str(i)).json()
        data = r['data']
        for j in range(len(data)):
            if data[j]["doctor"]["id"] == id and data[j]["diagnosis"]["name"]==name:
                sum+=data[j]["vitals"]["pulse"]
                cnt+=1

    return int(sum/cnt)
                


print(solve("Pulmonary embolism",2))