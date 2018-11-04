from django.shortcuts import render, get_object_or_404
from blog.models import Page
from .forms import ContactForm

from .secret import EmailSettings
import smtplib
from email.mime.text import MIMEText
from django.shortcuts import redirect
from django.template.loader import get_template
# Create your views here.

def about(request):
    page = get_object_or_404(Page, slug='sobre')
    return render(request, 'about.html',{'page':page})

def contact(request):
    form_class = ContactForm
    page = get_object_or_404(Page, slug='contato')
    if(request.method=='POST'):
        form = form_class(data=request.POST)
        if form.is_valid():
            frm_nome = request.POST.get('nome', '')
            frm_email = request.POST.get('email', '')
            frm_mensagem = request.POST.get('mensagem', '')
            template = get_template('contato_template.txt')
            context = {
                'nome':frm_nome,
                'email':frm_email,
                'mensagem': frm_mensagem
            }
            conteudo = template.render(context)
            emailInfo = EmailSettings

            message = MIMEText(conteudo)
            message['Subject'] = "[Lucas na Web] Contato"
            message['From'] = emailInfo.DEFAULT_FROM_EMAIL
            message['To'] = emailInfo.DEFAULT_FROM_EMAIL
            server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
            server.login(emailInfo.DEFAULT_FROM_EMAIL, emailInfo.EMAIL_HOST_PASSWORD)
            server.sendmail(emailInfo.DEFAULT_FROM_EMAIL, [emailInfo.DEFAULT_FROM_EMAIL], message.as_string())
            server.quit()

            return redirect('/contato/')
    return render(request, 'contato.html',{'form':form_class, 'page':page})