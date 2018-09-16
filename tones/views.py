from django.shortcuts import render, HttpResponse

# Create your views here
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'tones/index.html')

    def post(self, request):
    	form = HomeForm(request.POST)
    	if form.is_valid():
    		text - form.cleaned_Data['post']

    		args = {'form': form, 'text': text}
    		return render(request, self.template_name, args)