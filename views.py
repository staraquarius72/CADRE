from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import base64


# Create your views here.
def home(request):
    # mydb=mysql.connector.connect(host="localhost",user="root",password="Pathu@2002", database="innovation")
    # mycursor=mydb.cursor()
    # mycursor.execute("select * from innovation")
    # myrecord=mycursor.fetchall()
    # mycursor.reset()
    # if myrecord is not None:
    #     co=myrecord[-1][1]
    #     nox=myrecord[-1][2]
    #     pm=myrecord[-1][3]
    # else :
    #     co="-"
    #     nox="-"
    #     pm="-"

    # time_l,co_l,nox_l,pm_l=[],[],[],[]
    # for i in myrecord:
    #     time_l.append(i[0])
    #     co_l.append(i[1])
    #     nox_l.append(i[2])
    #     pm_l.append(i[3])

    # plt.plot(time_l,co_l)
    # plt.xlabel('Time')
    # plt.ylabel('CO Concentration')

    # buffer1 = io.BytesIO()
    # plt.savefig(buffer1, format='png')
    # plt.close()

    # plt.plot(time_l,nox_l)
    # plt.xlabel('Time')
    # plt.ylabel('NOx Concentration')

    # buffer2 = io.BytesIO()
    # plt.savefig(buffer2, format='png')
    # plt.close()

    # plt.plot(time_l,pm_l)
    # plt.xlabel('Time')
    # plt.ylabel('Particulate Matter Concentration')

    # buffer3 = io.BytesIO()
    # plt.savefig(buffer3, format='png')
    # plt.close()

    # plot_co = base64.b64encode(buffer1.getvalue()).decode('utf-8')
    # plot_nox = base64.b64encode(buffer2.getvalue()).decode('utf-8')
    # plot_pm = base64.b64encode(buffer3.getvalue()).decode('utf-8')

    # context={
    #     "co":co,
    #     "nox":nox,
    #     "pm":pm,
    #     'plot_co': plot_co,
    #     'plot_nox': plot_nox,
    #     'plot_pm': plot_pm,
    # }
    return render(request, "cansatapp/index.html")
