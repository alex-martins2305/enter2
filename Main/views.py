from django.shortcuts import render, redirect
import xlrd2
from .models import Aposentados
from datetime import date, datetime

def index(request):
    if request.method == 'POST':
        conta=request.POST['conta']
        beneficio=request.POST['beneficio']

        #validation datas
        if conta!="" and beneficio!="":
            messageError="Não informe conta e benefício juntos." 
            return render (request, 'index.html', {'messageError':messageError})
        if conta=="" and beneficio=="":
            messageError="Informe conta ou benefício para pesquisa." 
            return render (request, 'index.html', {'messageError':messageError})
        if len(str(conta))<=2 and len(str(beneficio))<=7:
            messageError="Quantidade de dígitos insuficientes para pesquisa" 
            return render (request, 'index.html', {'messageError':messageError})
        try:
            if conta!="":
                conta1=float(conta)
            if beneficio!="":
                beneficio1=float(beneficio)
        except:
            messageError="informe apenas números para pesquisa" 
            return render (request, 'index.html', {'messageError':messageError})        
 
        if conta!="":
            aposentado=Aposentados.objects.filter(conta__icontains=conta).first()
        if beneficio!="":
            aposentado=Aposentados.objects.filter(beneficio__icontains=beneficio).first()
        if aposentado:
            if int(aposentado.idade.split('.')[0])<=78 and float(aposentado.analfabeto)!=1 and float(aposentado.limite_vigente)==1:
            # quantidade_dias = abs((aposentado.ultimo_atendimento - date.today()).days)
            #a linha abaixo deverá ser ativada quando se quiser filtrar clientes que foram atendidos a mais de 90 dias.
            # if aposentado.idade<=78 and aposentado.alfabetizado==1 and aposentado.limite_vigente==1 and quantidade_dias>=90:   
                message="ENTRAR" 
                aposentado.ultimo_atendimento=date.today()
                aposentado.save()
                return render (request, 'index.html', {'message':message})
            else:
                message1="LIBERAR"
                return render (request, 'index.html', {'message1':message1})
        else:
            messageError="Cliente não encontrado."  
            return render (request, 'index.html', {'messageError':messageError})

    else:
        return render (request, 'index.html')

def load_data(request):
    if request.method == 'POST':
        adress = request.POST.get('adress')
        print(adress)
        if adress!="":
            # try:   
            book = xlrd2.open_workbook(adress)
            sh = book.sheet_by_index(0)
            n_total=0
            n_novos=0
            for rx in range(1, sh.nrows):
                n_total+=1
                mci=sh.cell_value(rowx=rx, colx=0)
                beneficio=sh.cell_value(rowx=rx, colx=1)
                tipo_beneficio=sh.cell_value(rowx=rx, colx=2)
                idade=sh.cell_value(rowx=rx, colx=3)
                analfabeto=sh.cell_value(rowx=rx, colx=4)
                agencia=sh.cell_value(rowx=rx, colx=5)
                conta=sh.cell_value(rowx=rx, colx=6)
                dia_recebimento=sh.cell_value(rowx=rx, colx=7)
                limite_vigente=sh.cell_value(rowx=rx, colx=8)
                precisa_prova_vida=sh.cell_value(rowx=rx, colx=9)

                if Aposentados.objects.filter(mci=sh.cell_value(rowx=rx, colx=0)).exists():
                    print('Registro já existe.')
                    Aposentado=Aposentados.objects.filter(mci=sh.cell_value(rowx=rx, colx=0)).first()

                    Aposentado.beneficio=beneficio
                    Aposentado.tipo_beneficio=tipo_beneficio
                    Aposentado.idade=idade
                    Aposentado.analfabetizado=analfabeto
                    Aposentado.agencia=agencia
                    Aposentado.conta=conta
                    Aposentado.dia_recebimento=dia_recebimento
                    Aposentado.limite_vigente=limite_vigente
                    Aposentado.precisa_prova_vida=precisa_prova_vida
                    Aposentado.save()

                else:
                    Aposentado= Aposentados.objects.create(mci=mci, beneficio=beneficio, tipo_beneficio=tipo_beneficio,idade=idade, analfabeto=analfabeto, agencia=agencia, conta=conta, dia_recebimento=dia_recebimento, limite_vigente=limite_vigente, precisa_prova_vida=precisa_prova_vida)
                    Aposentado.save()
                    n_novos+=1
            print ('INCLUÍDO ', n_novos, ' REGISTROS, EM UM TOTAL DE ', n_total, " REGISTROS.")  
            return redirect ('index')
            # except:
            #     print("Deu erro, parou no except.")
            #     return render (request, 'choose_file.html')
        else:
            return render (request, 'choose_file.html')   
    else:
        return render (request, 'choose_file.html')



# def load_data(request):
#     book = xlrd2.open_workbook("D:/BANCO/inss/relatorio1365.xls")
#     sh = book.sheet_by_index(0)
#     for rx in range(sh.nrows):
#         print(sh.row(rx))
#     return redirect ('index')

def teste(request):
        return render (request, 'teste.html')
