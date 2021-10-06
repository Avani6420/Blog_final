from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from .models import Blog_post, log
from .form import Blog_form, log_form


def B_post(request):
    return render(request, 'index.html')


def blog(request):
    form = Blog_post.objects.all()
    return render(request, 'blog.html', {'form': form})


def add_blog(request):
    if request.method == 'POST':
        add = Blog_form(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('blog_display')
    else:
        add = Blog_form()
    return render(request, 'add_blog.html', {'add': add})


def blog_display(request):
    return render(request, 'blog.html')


def login(request):
    return render(request, 'login.html')


def edit_blog(request, id):
    form = Blog_post.objets.get(id=id)
    return render(request, 'update_blog.html', {'form': form})


def blogpost(request, id):
    detail = Blog_post.objects.filter(id=id)
    args = {'detail': detail}
    return render(request, 'blog_detail.html', args)


def LikeView(request, pk):
    post = get_object_or_404(Blog_post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blogpost_detail', args=[str(pk)]))


class BlogPostDetailView(DetailView):
    model = Blog_post
    #template_name = 'blog_detail.html'
    # context_object_name = 'object'

    def get_context_data(self, **kwargs):
        #likes = Blog_post.objects.all()
        data = super(BlogPostDetailView, self).get_context_data()

        likes_connected = get_object_or_404(Blog_post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        #total_likes = likes_connected.total_likes()
        data['total_likes'] = likes_connected
        data['likes'] = liked
        return data


def update(request, id):
    data = Blog_post.objects.get(id=id)
    u_form = Blog_form(request.POST, request.FILES, instance=data)
    if u_form.is_valid():
        '''img_path = data.image_document.path
        if os.path.exists(img_path):
            os.remove(img_path)'''
        u_form.save()
        return redirect('/blog')
    else:
        return render(request, 'update_blog.html', {'form': data})


def register(request):
    context = {}
    sub = log_form(request.POST or None)
    if sub.is_valid():
        sub.save()
    context['sub'] = sub
    return render(request, 'reg.html', {'sub': sub})
# Create your views here.













from django.shortcuts import render, redirect
from .models import Article, Tag, Article_Tag


def display_article(request):
    data = Article.objects.all()
    tags = Tag.objects.all()
    context={
        'data' : data,
        'tags' : tags
    }
    return render(request, 'index.html', context)

def add_article(request):
    if request.method == 'POST':
        if request.POST.get('Title') and request.POST.get('txtarea'):
            article_obj = Article()
            article_obj.Title = request.POST.get('Title')
            article_obj.Content = request.POST.get('txtarea')
            article_obj.Image = request.POST.get('Image')
            obj2 = Tag()
            obj2.name = request.POST.get('Tag')
            article_obj.save()
            obj2.save()
            return render(request, 'article.html')
    else:
        return render(request, 'article.html')

def tag_opration(request):
    result= Article_Tag.objects.all()
    if result.request.method == 'POST':
        for ch in result:
            ch.result.tag()


def get_articles(request):
    ...
    ...
    result = []
    articles = Articles.all()
    for article in articles:
        # Get tags of each article one by one
        tags = ArticleTag.find_from_db(article).values("tag__name")

        article_dict = {
            "article": article.name,
            ...
            ...
            "tags": tags
        }
        result.push(article_dict)

    print(result)
    return response(result)


    def create_article(request):
    ...
    ...
    article = article_form.save()

    # Get tag value from the POST data.
    # POST key is the name attribute of the tag element.
    tags_val = request.POST[""]
    tags = [split tags_val by comma]

    for tag_val in tags:
        tag = Tag.find_from_db(tag_val)
        if tag is None:
            # Use create method to insert data
            tag = Tag.create()

        # Use tag and article object to insert relation entry in ArticleTag table.
        ArticleTag.create()


