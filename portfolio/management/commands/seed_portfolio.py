from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.files import File
from pathlib import Path
import shutil
from portfolio.models import Project, Skill, Experience, Adventure, Post

class Command(BaseCommand):
    help='Create starter portfolio content using the included assets.'
    def handle(self,*args,**kwargs):
        Project.objects.all().delete(); Skill.objects.all().delete(); Experience.objects.all().delete(); Adventure.objects.all().delete(); Post.objects.all().delete()
        def attach(obj, field, rel):
            p=settings.BASE_DIR/'static'/rel
            if p.exists():
                with p.open('rb') as f: getattr(obj,field).save(p.name,File(f),save=True)
        p=Project.objects.create(title='MediStreak',short_description='Gamified medical learning platform with interactive case simulations, diagnosis quizzes, progress tracking and community learning.',description='MediStreak is a medical learning platform built to make practice more interactive through cases, quizzes and progress-oriented learning.',stack='Django, Python, JavaScript, HTML, CSS',live_url='https://medistreak-platform.onrender.com/',github_url='https://github.com/Surexx7/medistreak-platform',featured=True,order=1)
        attach(p,'image',Path('images/projects/medistreak.png'))
        Project.objects.create(title='CivicEye',short_description='Mobile-first civic engagement platform for Nepal’s urban municipalities with AI-assisted issue detection and routing.',description='Academic project using React Native, Django REST API and PostgreSQL, with computer vision and NLP components.',stack='React Native, Django REST, PostgreSQL, Machine Learning',featured=True,order=2)
        Project.objects.create(title='Texas College Chatbot',short_description='AI-powered chatbot designed to help students with college-related queries using Python and NLP.',description='Student-assistance chatbot project using Python, machine learning and natural language processing.',stack='Python, NLP, Machine Learning',featured=True,order=3)
        groups={
          'development':['Python','Django','HTML5','CSS3','JavaScript','Bootstrap','PHP','REST APIs'],
          'systems':['Windows Server','Active Directory','Microsoft 365','Intune','Defender','VMware','Hyper-V','Networking'],
          'tools':['GitHub','VS Code','Figma','Canva','Photoshop']}
        codes={'Python':'Py','Django':'dj','HTML5':'5','CSS3':'#','JavaScript':'JS','Bootstrap':'B','PHP':'PHP','REST APIs':'API','Windows Server':'WS','Active Directory':'AD','Microsoft 365':'365','Intune':'IN','Defender':'DF','VMware':'VM','Hyper-V':'HV','Networking':'NET','GitHub':'Git','VS Code':'VS','Figma':'Fg','Canva':'Ca','Photoshop':'Ps'}
        icons={'Python':'fa-brands fa-python','Django':'fa-solid fa-code','HTML5':'fa-brands fa-html5','CSS3':'fa-brands fa-css3-alt','JavaScript':'fa-brands fa-js','Bootstrap':'fa-brands fa-bootstrap','PHP':'fa-brands fa-php','REST APIs':'fa-solid fa-plug','Windows Server':'fa-brands fa-windows','Active Directory':'fa-solid fa-users-gear','Microsoft 365':'fa-brands fa-microsoft','Intune':'fa-solid fa-shield-halved','Defender':'fa-solid fa-shield','VMware':'fa-solid fa-server','Hyper-V':'fa-solid fa-cubes','Networking':'fa-solid fa-network-wired','GitHub':'fa-brands fa-github','VS Code':'fa-solid fa-code','Figma':'fa-brands fa-figma','Canva':'fa-solid fa-palette','Photoshop':'fa-solid fa-image'}
        for cat,names in groups.items():
            for i,n in enumerate(names): Skill.objects.create(name=n,category=cat,short_code=codes[n],icon_class=icons[n],order=i+1)
        exp=[
          ('B.Sc. CSIT','Texas International College','2022 – Present','Computer Science & Information Technology.'),
          ('IT Support Training','TechSkills Institute','Dec 2025 – Present','Windows Server, Active Directory, Microsoft 365, networking and virtualization.'),
          ('IT Support Specialist','Active IT — Australia','Current','Systems and end-user support in a professional environment.'),
          ('Web Development','Personal & Academic Projects','Ongoing','Django, Python and modern web applications.'),
          ('Explorer','Nepal','Always','Trekking, hiking and travel photography.'),]
        for i,(t,o,d,desc) in enumerate(exp): Experience.objects.create(title=t,organization=o,date_label=d,description=desc,current=(i==2),order=i+1)
        advs=[('Langtang Trek','Nepal','images/travel/langtang.jpg'),('Mardi Himal','Nepal','images/travel/mardi.jpg'),('Panch Pokhari','Nepal','images/travel/panch-pokhari.jpg'),('Travel Moments','Keep exploring','images/travel/langtang-trail.jpg')]
        for i,(t,loc,img) in enumerate(advs):
            a=Adventure.objects.create(title=t,location=loc,summary='Mountains, trails and moments from the journey.',story='This is the place for the story behind this adventure. Open Django Admin → Adventures and write a short personal journey: why you went, the trail, memorable moments, challenges and what the trip meant to you.',instagram_url='https://www.instagram.com/suresh_shahi7',order=i+1)
            attach(a,'cover_image',Path(img))
        Post.objects.create(title='My IT Support Learning Journey',category='it-support',excerpt='Notes and lessons from practical IT support training and real-world support work.',body='Use Django Admin to replace this starter article with your training posts, troubleshooting notes, Microsoft 365 tips, Windows Server lessons and other IT support content.',order=1)
        self.stdout.write(self.style.SUCCESS('Portfolio starter content created.'))
