from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from .managers import CategoryManager
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Banner(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_('Title')),
        description=models.CharField(max_length=200, verbose_name=_('Description'))
    )
    link = models.CharField(max_length=400, verbose_name=_('Link'))
    image = models.ImageField(upload_to='photos/banners')
    link = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'


class About(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=245, verbose_name=_('Title')),
        short_description=models.CharField(max_length=1300, verbose_name=_('Short Description')),
        description=RichTextField(verbose_name=_('Description')),
    )
    image = models.ImageField(upload_to='photos/home', verbose_name=_('Image'))
    experience = models.CharField(max_length=245, verbose_name=_('Experience'))

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')


class Projects(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_('Title')),
        description=RichTextField(blank=True, verbose_name=_('Description')),
        type=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Type')),

    )
    slug = models.SlugField(max_length=200, blank=True, null=True, unique=True, verbose_name=_('Slug'))
    cover = models.ImageField(blank=True, null=True, upload_to='photos/projects')
    image = models.ImageField(blank=True, null=True, upload_to='photos/projects')
    icon = models.CharField(max_length=200, blank=True, null=True)
    customer = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Сustomer'))
    date = models.DateField(blank=True, null=True, verbose_name=_('Date'))
    projects = models.BooleanField(default=True, blank=True, null=True, verbose_name=_('Projects'))
    know_how = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Know How'))
    completed_job = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Completed Job'))
    new_developments = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('New Developments'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name=_('Order'))

    def get_url(self):
        return reverse('project_detail', args=[self.slug])

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = _('Projects')
        verbose_name_plural = _('Projects')


class News(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_('Title')),
        description=RichTextField(blank=True, verbose_name=_('Description')),

    )
    news = models.BooleanField(default=True, blank=True, null=True, verbose_name=_('News'))
    events = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Events'))

    slug = models.SlugField(max_length=200, blank=True, null=True, unique=True, verbose_name=_('Slug'))
    image = models.ImageField(blank=True, null=True, upload_to='photos/projects')
    date = models.DateField(blank=True, null=True, verbose_name=_('Date'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name=_('Order'))

    def get_url(self):
        return reverse('news_detail', args=[self.slug])

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = _('News')
        verbose_name_plural = _('News')


class SiteSettings(TranslatableModel):
    translations = TranslatedFields(
        text=models.CharField(max_length=200, blank=True, null=True),
    )
    thumbnail = models.ImageField(upload_to='site_settings/thumbnail', blank=True, null=True)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = _('Site settings')
        verbose_name_plural = _('Site settings')


class Tables(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=500, verbose_name=_('Title')),
        file=models.FileField(upload_to='files/tables')
    )
    number = models.CharField(max_length=250, verbose_name=_('Number'))
    date = models.DateField(verbose_name=_('Date'))

    def get_url(self):
        return self.url

    def __str__(self):
        return str(self.title)


class Category(MPTTModel, TranslatableModel):
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children",
                            verbose_name=_('Parent'))

    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name'), null=True, blank=True),
    )
    slug = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Slug'))
    image = models.ImageField(upload_to='images/category', default='category/default.jpg', verbose_name=_('Images'))
    objects = CategoryManager()

    class Meta:
        verbose_name = _('Navbar')
        verbose_name_plural = _('Navbar')

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True) or "-"


class Tender(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=250, verbose_name=_('Title')),
        description=RichTextField(blank=True, verbose_name=_('Description')),
    )
    slug = models.SlugField(max_length=200, blank=True, null=True, unique=True, verbose_name=_('Slug'))
    date = models.DateField(verbose_name=_('Date'))
    until_date = models.DateField(blank=True, null=True, verbose_name=_('Until Date'))
    until_hour = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Until Hour'))
    applications = models.CharField(max_length=240, verbose_name=_('Applications'))
    view_count = models.IntegerField(default=0, null=True, verbose_name=_('View Count'))

    def get_url(self):
        return reverse('tender_detail', args=[self.slug])

    def __str__(self):
        return f"{self.safe_translation_getter('title')}"

    class Meta:
        verbose_name = _('Tender')
        verbose_name_plural = _('Tender')


# class StaticContent(TranslatableModel):
#     """ Static Content MODEL """
#
#     translations = TranslatedFields(
#         title=models.CharField(max_length=255, verbose_name=_('Title')),
#         content=RichTextField(verbose_name=_('Content')),
#     )
#     category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL ,verbose_name=_('Category'))
#     slug = models.CharField(blank=True, null=True, verbose_name=_("Slug"), max_length=500)
#
#     def get_url(self):
#         return reverse('static_page', args=[self.slug])
#
#     def __str__(self):
#         return f"{self.safe_translation_getter('title', '-')}"
#
#     class Meta:
#         verbose_name = _('Static Content')
#         verbose_name_plural = _('Static Content')


class File(models.Model):
    title = models.CharField(max_length=250, verbose_name=_('Title'))
    file = models.FileField(upload_to='pdf/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Pdf File')
        verbose_name_plural = _('Pdf File')


class Membership(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=250, verbose_name=_('Name')),
        position=models.CharField(max_length=400, verbose_name=_('Position')),
        description=RichTextField(verbose_name=_('Description')),
        adress=models.CharField(max_length=300, blank=True, null=True, verbose_name=_('Adress')),

    )
    slug = models.CharField(blank=True, null=True, verbose_name=_("Slug"), max_length=500)
    image = models.ImageField(upload_to='membership/', blank=True, null=True, verbose_name=_('image'))
    number = models.CharField(max_length=300, verbose_name=_('Number'))
    email = models.CharField(max_length=300, verbose_name=_('Email'))

    def get_url(self):
        return reverse('membership_page', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Membership')
        verbose_name_plural = _('Membership')


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name=_('Image'))

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Gallery')


class Video(models.Model):
    link = models.CharField(max_length=250, verbose_name=_('Link'))

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Video')


class StaticContent(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_('Title')),
        content=RichTextField(verbose_name=_('Content')),
    )
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('Category'))
    slug = models.CharField(blank=True, null=True, verbose_name=_("Slug"), max_length=500)

    def __str__(self):
        return f"{self.safe_translation_getter('title')}"

    class Meta:
        verbose_name = "StaticContent"