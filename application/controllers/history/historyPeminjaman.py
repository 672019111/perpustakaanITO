from application import app
from flask import jsonify, request, render_template, url_for, redirect, flash
from application.models.history.historyPeminjamanModals import *
from application.controllers.auth import adminLoginRequired
from application.controllers.webservis import *


@app.route('/historypeminjaman', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def PageHistoryPeminjaman():
    data = getHistoryPenyimpanan()
    print (data)
    return render_template("history/historypeminjaman.html", data= data)
