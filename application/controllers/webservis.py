from application import app
from flask import jsonify, request, flash, redirect, url_for
from application.models.master.bukuModels import *
from application.models.master.penerbitModels import *
from application.models.master.penulisModels import *
from application.models.master.kategoriModels import *
from application.models.master.anggotaPerpustakaanModels import *
from application.controllers.auth import adminLoginRequired


@app.route('/mastersBuku', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def mastersBuku():
    data = {
        "penerbit": getAllpenerbit(),
        "pengarang": getAllpenulis(),
        "kategori": getAllKategori()
    }
    return jsonify(data)


@app.route('/judulBuku/<int:id>', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def judulBukubyid(id):
    data = getJudulBuku(id)
    if request.method == 'POST':

        print("masuk disini")

        idjudlbuku = request.form['input_update_idjudulbuku']
        nama = request.form['input_update_judul_buku']
        idpenerbit = request.form['select_update_penerbit']
        idpengarang = request.form['select_update_pengarang']
        idkategori = request.form['select_update_kategori']
        tahunterbit = request.form['update_tahunterbit']
        respon = updateJudulBuku(
            idjudlbuku, idpenerbit, idpengarang, idkategori, nama, tahunterbit)
        print("respon", respon)
        if respon['status'] == 'T':
            flash('buku ' + nama + ' berhasil diupdate ', 'success')
            print("masuk disini")
        else:
            flash('buku ' + nama +
                  ' Gagal ditambah, silakan hubungi bagian IT [001] ', 'danger')
        return redirect(url_for('PageJudulBuku'))
    return jsonify(data)


@app.route('/judulBuku', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def judulBuku():
    id = request.args.get("id")
    if request.method == 'GET':
        if id:
            data = getJudulBuku(id)
        else:
            data = getAllJudulBuku()
        return jsonify(data)
    if request.method == 'POST':
        nama = request.form['judul_buku']
        idpenerbit = request.form['select_penerbit']
        idpengarang = request.form['select_pengarang']
        idkategori = request.form['select_kategori']
        tahunterbit = request.form['tahunterbit']
        respon = insertJudulBuku(idpenerbit, idpengarang,
                                 idkategori, nama, tahunterbit)
        if respon['status'] == 'T':
            flash('buku ' + nama + ' berhasil ditambah ', 'success')
        else:
            flash('buku ' + nama +
                  ' Gagal ditambah, silakan hubungi bagian IT [001] ', 'danger')
        return redirect(url_for('PageJudulBuku'))
    return jsonify(data)


@app.route('/buku', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def buku():
    id = request.args.get("id")
    data = {}
    if request.method == 'GET':
        data = getBuku(id) if id else getAllBuku()
    elif request.method == 'POST':
        return "under maintenance"
    return jsonify(data)


@app.route('/TempbukuPinjam', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def TempbukuPinjam():
    id = request.args.get("id")
    data = getBuku(id)
    print("data", data, data['result'][0]['status'] != 'tersedia')
    if data['result'][0]['status'] != 'tersedia':
        return ({'status': 'X'})
    else :
        return jsonify(data)


@app.route('/AnggotaPerpustakaan', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def anggotaPerpustakaan():
    id = request.args.get("id")
    if request.method == 'GET':
        if id:
            data = getAnggotaPerpustakaan(id)
        else:
            data = getAnggotaPerpustakaans()
        return jsonify(data)
    if request.method == 'POST':
        return "under maitenance"
    return jsonify(data)
