from django.shortcuts import render
from django.views import View
# Create your views here.




class index (View):
    def get(self,request):
        all_grp = [
        "Artificial Intelligence",
        "Data Science",
        "Machine Learning",
        "Computer Vision",
        "Natural Language Processing",
        "Robotics",
        "Computer Graphics",
        "Database Systems",
        "Cybersecurity",
        "Software Engineering",
        "Web Development",
        "Mobile App Development",
        "Cloud Computing",
        "Distributed Systems",
        "Operating Systems",
        "Computer Networks",
        "Algorithms",
        "Data Structures",
        "Computer Architecture",
        "Human-Computer Interaction"
        ]

        contex = {
            'groups': all_grp
        }
        return render(request ,'index.html', context=contex)
