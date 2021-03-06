from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import View

from .forms import PostForm


class PaginatorMixin:
    paginate_by = 5
    initial_page_number = 1

    def get_page(self, request):
        paginator = Paginator(self.model.objects.all(), self.paginate_by)
        total_pages = paginator.num_pages
        try:
            page_number = request.GET.get('page')
            if int(page_number) > total_pages:
                page_number = total_pages
            elif int(page_number) < self.initial_page_number:
                raise
        except:
            page_number = self.initial_page_number
        return paginator.page(page_number)


class GetObjectMixin:

    def get_model_object(self, year, month, slug):
        return (
            get_object_or_404(
                self.model,
                pub_date__year  = year,
                pub_date__month = month,
                slug__iexact    = slug
            )
        )


class ObjectListMixin(PaginatorMixin):

    def get(self, request):
        page = self.get_page(request)
        context = {
            self.context_name: page,
        }
        return render(request, self.template_name, context)


class ObjectDetailMixin(GetObjectMixin):

    def get(self, request, **kwargs):
        context = {
            self.context_name: self.get_model_object(**kwargs)
        }
        return render(request, self.template_name, context)


class CreateObjectMixin:

    def get(self, request):
        context = {
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_object = form.save()
            return redirect(new_object)
        else:
            context = {'form': form}
        return render(request, self.template_name, context)


class UpdateObjectMixin(GetObjectMixin):

    def get(self, request, **kwargs):
        object = self.get_model_object(**kwargs)
        context = {
            'form': self.form_class(instance=object),
            self.context_name: object,
        }

    def post(self, request, **kwargs):
        object = self.get_model_object(**kwargs)
        form = self.form_class(request.POST, instance=object)
        if form.is_valid():
            updated_object = form.save()
            return redirect(updated_object)
        else:
            context = {
                'form': form,
                self.context_name: object,
            }
        return render(request, self.template_name, context)


class DeleteObjectMixin(GetObjectMixin):

    def get(self, request, **kwargs):
        context = {
            self.context_name: self.get_model_object(**kwargs)
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        self.get_model_object(**kwargs).delete()
        return redirect(self.redirect_to)


class YearArchiveIndexView(View):
    model = None
    template_name = ''

    def get_archive_list(self, ordering='ASC'):
        return self.model.objects.dates('pub_date', 'year', ordering)

    def get(self, request):
        context = {
            'archive_index': self.get_archive_list()
        }
        return render(request, self.template_name, context)


class YearArchiveView(View):
    model = None
    template_name = ''

    def get_archive_elements(self, year):
        return self.model.objects.filter(pub_date__year=year)

    def get(self, request, year):
        context = {
            self.context_object_name: self.get_archive_elements(year),
            'year': year,
        }
        return render(request, self.template_name, context)
