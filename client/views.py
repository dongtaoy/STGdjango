from django.shortcuts import render

# Create your views here.


def clientList(request):
    clients = [
        {
            "name": "George Cai",
            "DoB": "1993-11-05",
            "status": "Ongoing",
            "nationality": "China",
            "consultant": "Tim Wang",
            "clientManager": "Cecilia Han",
            # "stageLink": "http://www.baidu.com",
            "stage": "Stage 1",
            "visa": 163,
            "institution": "University of Melbourne",
            "courseStart": "2014-05-11",
            "courseEnd": "2014-08-01",
            "detailsLink": "http://www.google.com",
        }
    ]
    # return render(request, "client/stagePage.html", {"clients": clients})
    return render(request, "client/client.list.html", {"clients": clients})


def clienDetails(request):
    clients = [
        {
            "name": "George Cai",
            "DoB": "1993-11-05",
            "status": "Ongoing",
            "nationality": "China",
            "consultant": "Tim Wang",
            "clientManager": "Cecilia Han",
            # "stageLink": "http://www.baidu.com",
            "stage": "Stage 1",
            "visa": 163,
            "institution": "University of Melbourne",
            "courseStart": "2014-05-11",
            "courseEnd": "2014-08-01",
            "detailsLink": "http://www.google.com",
        }
    ]
    return render(request, "client/client.info.html", {"clients": clients})