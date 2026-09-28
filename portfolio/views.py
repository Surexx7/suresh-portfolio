from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Project, Skill, Experience, Adventure, Post, ContactMessage

def _base_context():
    return {'skills':Skill.objects.filter(featured=True),'experiences':Experience.objects.all()}

def home(request):
    if request.method=='POST':
        name=request.POST.get('name','').strip(); email=request.POST.get('email','').strip(); msg=request.POST.get('message','').strip()
        if name and email and msg:
            ContactMessage.objects.create(name=name,email=email,subject=request.POST.get('subject','').strip(),message=msg)
            messages.success(request,'Thanks! Your message has been received.')
        else: messages.error(request,'Please complete your name, email and message.')
        return redirect('home')
    ctx=_base_context(); ctx.update({
      'projects':Project.objects.filter(featured=True,published=True)[:3],
      'adventures':Adventure.objects.filter(featured=True,published=True)[:4],
      'posts':Post.objects.filter(published=True)[:3],
    }); return render(request,'portfolio/home.html',ctx)

def projects(request): return render(request,'portfolio/projects.html',{'projects':Project.objects.filter(published=True)})
def project_detail(request,slug): return render(request,'portfolio/project_detail.html',{'project':get_object_or_404(Project,slug=slug,published=True)})
def adventures(request): return render(request,'portfolio/adventures.html',{'adventures':Adventure.objects.filter(published=True)})
def adventure_detail(request,slug): return render(request,'portfolio/adventure_detail.html',{'adventure':get_object_or_404(Adventure,slug=slug,published=True)})
def posts(request): return render(request,'portfolio/posts.html',{'posts':Post.objects.filter(published=True)})
def post_detail(request,slug): return render(request,'portfolio/post_detail.html',{'post':get_object_or_404(Post,slug=slug,published=True)})
