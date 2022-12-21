from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# posts = [
#     {
#         'author': 'Paul Rukwaro',
#         'title': 'Machine Learning',
#         'content': 'Here is paul post regarding ChatGTP',
#         'date_posted': 'August 13th 2022'
#     },
#     {
#         'author': 'Judy wa Georgia',
#         'title': 'Microbiology applications',
#         'content': 'Here is judy post regarding Microbiology',
#         'date_posted': 'July 17th 2022'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog_app/home.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'blog_app/home.html' # <app> / <nodel>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog_app/user_posts.html' # <app> / <nodel>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDetailView(DetailView):
    model = Post
    

def downloads(request):
    return HttpResponse('<h1>Paul Downloads home</h1>')

# def about(request):
#     return HttpResponse('<h1>Paul about page</h1>')


def about(request):
    return render(request, 'blog_app/about.html')

def mybio(request):
    return render(request, 'blog_app/mybio.html')

def mytest(request):
    return render(request, 'blog_app/portfolio.html')