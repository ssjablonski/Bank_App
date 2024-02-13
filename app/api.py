from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.KontoOsobiste import KontoOsobiste

app = Flask(__name__)


@app.route("/api/accounts", methods=['POST'])
def stworz_konto():
   dane = request.get_json()
   print(f"Request o stworzenie konta z danymi: {dane}")
   if RejestrKont.znajdz_konto(dane["pesel"]) == None:
    konto = KontoOsobiste(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify({"message": "Konto stworzone"}), 201
   else:
       return jsonify({"message": "Istnieje konto z tym peselem"}), 409

@app.route("/api/accounts/count", methods=['GET'])
def ile_kont():
    return jsonify({"count": RejestrKont.ile_kont()}), 200


@app.route("/api/accounts/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    konto = RejestrKont.znajdz_konto(pesel)
    if konto is None:
        return jsonify({"message": "Nie znaleziono konta"}), 404
    else:
        return jsonify({
            "Imię": konto.imie, 
            "Nazwisko": konto.nazwisko,
            "Saldo": konto.saldo,
            "PESEL": konto.pesel,
            "Historia": konto.historia,
            "Zgoda na kredyt": konto.zgoda_na_kredyt
            }), 200
    
@app.route("/api/accounts/update/<pesel>", methods=['PATCH'])
def aktualizuj_konto_z_peselem(pesel):
    dane = request.get_json()
    konto = RejestrKont.znajdz_konto(pesel)
    if konto is None:
        return jsonify({"message": "Nie znaleziono konta"}), 404
    else:
        # tu moze jakos zapisywac do tablicy co sie zmienia i na koniec w komunikacie wysqwietlac co zostalo zmienione??
        if "imie" in dane:
            konto.imie = dane["imie"]
        if "nazwisko" in dane:
            konto.nazwisko = dane["nazwisko"]
        if "pesel" in dane:
            konto.pesel = dane["pesel"]
        if "saldo" in dane:
            konto.saldo = dane["saldo"]
        return jsonify({"message": "Konto zaktualizowane"}), 200

@app.route("/api/accounts/delete/<pesel>", methods=['DELETE'])
def usun_konto_z_peselem(pesel):
    konto = RejestrKont.znajdz_konto(pesel)  
    if konto is None:
        return jsonify({"message": "Nie znaleziono konta"}), 404
    else:
        RejestrKont.usun_konto(pesel)
        return jsonify({"message": "Konto zostało usunięte"}), 200
    
@app.route("/api/accounts/<pesel>/transfer", methods=["POST"])
def wykonaj_przelew(pesel):
    konto = RejestrKont.znajdz_konto(pesel)
    if konto is None:
        return jsonify({"message": "Nie znaleziono konta"}), 404
    else:
        dane = request.get_json()
        if ("amount" and "type") in dane:
            if dane["type"] == "incoming":
                konto.zaksieguj_przelew_przychodzacy(int(dane["amount"]))
                return jsonify({"message": "Przelew wykonany"}), 200
            elif dane["type"] == "outgoing":
                konto.zaksieguj_przelew_wychodzacy(int(dane["amount"]))
                return jsonify({"message": "Przelew wykonany"}), 200        
        return jsonify({"message": "Przelew przyjęto do realizacji"}), 400