from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class OrderedModel(models.Model):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Project(OrderedModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    stack = models.CharField(max_length=300, help_text='Comma-separated technologies')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def technologies(self):
        return [x.strip() for x in self.stack.split(',') if x.strip()]

    def get_absolute_url(self):
        return reverse('project_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Skill(OrderedModel):
    DEVELOPMENT = 'development'
    SYSTEMS = 'systems'
    TOOLS = 'tools'
    CATEGORIES = [
        (DEVELOPMENT, 'Development'),
        (SYSTEMS, 'IT & Systems'),
        (TOOLS, 'Tools'),
    ]
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    short_code = models.CharField(max_length=10, blank=True)
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text='Font Awesome class, e.g. fa-brands fa-python',
    )
    featured = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return self.name


class Experience(OrderedModel):
    title = models.CharField(max_length=120)
    organization = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    date_label = models.CharField(max_length=80, blank=True)
    description = models.TextField(blank=True)
    current = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f'{self.title} — {self.organization}'


class Adventure(OrderedModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    location = models.CharField(max_length=120, blank=True)
    summary = models.CharField(max_length=220, blank=True)
    story = models.TextField(blank=True, help_text='Your travel story / journey description.')
    cover_image = models.ImageField(upload_to='adventures/', blank=True, null=True)
    instagram_post_url = models.URLField(
        blank=True,
        help_text='Paste the URL of the specific Instagram travel post/reel to embed on the detail page.',
    )
    instagram_url = models.URLField(blank=True, help_text='Optional profile or fallback Instagram URL.')
    featured = models.BooleanField(default=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('adventure_detail', args=[self.slug])

    def __str__(self):
        return self.title


class AdventurePhoto(OrderedModel):
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='adventures/gallery/')
    caption = models.CharField(max_length=180, blank=True)

    class Meta:
        ordering = ['order', 'id']


class Post(OrderedModel):
    IT = 'it-support'
    DEV = 'development'
    TRAVEL = 'travel'
    CATEGORIES = [(IT, 'IT Support'), (DEV, 'Development'), (TRAVEL, 'Travel')]
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, default=IT)
    excerpt = models.CharField(max_length=240)
    body = models.TextField()
    cover_image = models.ImageField(upload_to='posts/', blank=True, null=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=160, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.created_at:%Y-%m-%d}'
