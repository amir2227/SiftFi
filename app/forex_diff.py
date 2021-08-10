from app import app
from app.utils import get_database_connection
from flask import jsonify, request
from datetime import date


@app.route("/api/v0/forex_get_all_diff")
def get_all_diff():
    try:
        json_data_ir = {}
        json_data_gdp = {}
        json_data_cot = {}
        json_data_escore = {}
        ir_diff = {}
        gdp_diff = {}
        cot_diff = {}
        escore_diff = {}
        today = date.today()
        db = get_database_connection()
        cur = db.cursor()
        cur.execute(f"SELECT * FROM IR where d_date = '{today.year}'")
        row_headers_ir = [x[0] for x in cur.description]
        rows = cur.fetchall()
        cur.execute(f"SELECT * FROM GDP where d_date = '{today.year}'")

        row_headers_gdp = [x[0] for x in cur.description]
        rows2 = cur.fetchall()
        cur.execute(f"""SELECT * FROM COT where
                    d_date <= '{today}' order by d_date desc limit 1""")
        row_headers_cot = [x[0] for x in cur.description]
        rows3 = cur.fetchall()
        cur.execute(f"""SELECT * FROM E_SCORE where
                    d_date <= '{today}' order by d_date desc limit 1""")
        row_headers_escore = [x[0] for x in cur.description]
        rows4 = cur.fetchall()
        for result in rows:
            json_data_ir = dict(zip(row_headers_ir, result))
        for result2 in rows2:
            json_data_gdp = dict(zip(row_headers_gdp, result2))
        for result3 in rows3:
            json_data_cot = dict(zip(row_headers_cot, result3))
        for result4 in rows4:
            json_data_escore = dict(zip(row_headers_escore, result4))
        
        ir_diff = {"AUD/CAD": json_data_ir['AUD'] - json_data_ir['CAD'],
                    "AUD/CHF": json_data_ir['AUD'] - json_data_ir['CHF'],
                    "AUD/JPY": json_data_ir['AUD'] - json_data_ir['JPY'],
                    "AUD/NZD": json_data_ir['AUD'] - json_data_ir['NZD'],
                    "AUD/USD": json_data_ir['AUD'] - json_data_ir['USD'],
                    "AUD/ZAR": json_data_ir['AUD'] - json_data_ir['ZAR'],
                    "CAD/JPY": json_data_ir['CAD'] - json_data_ir['JPY'],
                    "CAD/ZAR": json_data_ir['CAD'] - json_data_ir['ZAR'],
                    "CHF/JPY": json_data_ir['CHF'] - json_data_ir['JPY'],
                    "EUR/AUD": json_data_ir['EUR'] - json_data_ir['AUD'],
                    "EUR/CAD": json_data_ir['EUR'] - json_data_ir['CAD'],
                    "EUR/CHF": json_data_ir['EUR'] - json_data_ir['CHF'],
                    "EUR/GBP": json_data_ir['EUR'] - json_data_ir['GBP'],
                    "EUR/JPY": json_data_ir['EUR'] - json_data_ir['JPY'],
                    "EUR/NZD": json_data_ir['EUR'] - json_data_ir['NZD'],
                    "EUR/RUB": json_data_ir['EUR'] - json_data_ir['RUB'],
                    "EUR/USD": json_data_ir['EUR'] - json_data_ir['USD'],
                    "EUR/ZAR": json_data_ir['EUR'] - json_data_ir['ZAR'],
                    "GBP/AUD": json_data_ir['GBP'] - json_data_ir['AUD'],
                    "GBP/CAD": json_data_ir['GBP'] - json_data_ir['CAD'],
                    "GBP/CHF": json_data_ir['GBP'] - json_data_ir['CHF'],
                    "GBP/JPY": json_data_ir['GBP'] - json_data_ir['JPY'],
                    "GBP/NZD": json_data_ir['GBP'] - json_data_ir['NZD'],
                    "GBP/USD": json_data_ir['GBP'] - json_data_ir['USD'],
                    "GBP/ZAR": json_data_ir['GBP'] - json_data_ir['ZAR'],
                    "NZD/CAD": json_data_ir['NZD'] - json_data_ir['CAD'],
                    "NZD/CHF": json_data_ir['NZD'] - json_data_ir['CHF'],
                    "NZD/MXN": json_data_ir['NZD'] - json_data_ir['MXN'],
                    "NZD/USD": json_data_ir['NZD'] - json_data_ir['USD'],
                    "USD/CAD": json_data_ir['USD'] - json_data_ir['CAD'],
                    "USD/CHF": json_data_ir['USD'] - json_data_ir['CHF'],
                    "USD/JPY": json_data_ir['USD'] - json_data_ir['JPY'],
                    "USD/MXN": json_data_ir['USD'] - json_data_ir['MXN'],
                    "USD/RUB": json_data_ir['USD'] - json_data_ir['RUB'],
                    "USD/ZAR": json_data_ir['USD'] - json_data_ir['ZAR']}
        
        gdp_diff = {"AUD/CAD": json_data_gdp['AUD'] - json_data_gdp['CAD'],
                    "AUD/CHF": json_data_gdp['AUD'] - json_data_gdp['CHF'],
                    "AUD/JPY": json_data_gdp['AUD'] - json_data_gdp['JPY'],
                    "AUD/NZD": json_data_gdp['AUD'] - json_data_gdp['NZD'],
                    "AUD/USD": json_data_gdp['AUD'] - json_data_gdp['USD'],
                    "AUD/ZAR": json_data_gdp['AUD'] - json_data_gdp['ZAR'],
                    "CAD/JPY": json_data_gdp['CAD'] - json_data_gdp['JPY'],
                    "CAD/ZAR": json_data_gdp['CAD'] - json_data_gdp['ZAR'],
                    "CHF/JPY": json_data_gdp['CHF'] - json_data_gdp['JPY'],
                    "EUR/AUD": json_data_gdp['EUR'] - json_data_gdp['AUD'],
                    "EUR/CAD": json_data_gdp['EUR'] - json_data_gdp['CAD'],
                    "EUR/CHF": json_data_gdp['EUR'] - json_data_gdp['CHF'],
                    "EUR/GBP": json_data_gdp['EUR'] - json_data_gdp['GBP'],
                    "EUR/JPY": json_data_gdp['EUR'] - json_data_gdp['JPY'],
                    "EUR/NZD": json_data_gdp['EUR'] - json_data_gdp['NZD'],
                    "EUR/RUB": json_data_gdp['EUR'] - json_data_gdp['RUB'],
                    "EUR/USD": json_data_gdp['EUR'] - json_data_gdp['USD'],
                    "EUR/ZAR": json_data_gdp['EUR'] - json_data_gdp['ZAR'],
                    "GBP/AUD": json_data_gdp['GBP'] - json_data_gdp['AUD'],
                    "GBP/CAD": json_data_gdp['GBP'] - json_data_gdp['CAD'],
                    "GBP/CHF": json_data_gdp['GBP'] - json_data_gdp['CHF'],
                    "GBP/JPY": json_data_gdp['GBP'] - json_data_gdp['JPY'],
                    "GBP/NZD": json_data_gdp['GBP'] - json_data_gdp['NZD'],
                    "GBP/USD": json_data_gdp['GBP'] - json_data_gdp['USD'],
                    "GBP/ZAR": json_data_gdp['GBP'] - json_data_gdp['ZAR'],
                    "NZD/CAD": json_data_gdp['NZD'] - json_data_gdp['CAD'],
                    "NZD/CHF": json_data_gdp['NZD'] - json_data_gdp['CHF'],
                    "NZD/MXN": json_data_gdp['NZD'] - json_data_gdp['MXN'],
                    "NZD/USD": json_data_gdp['NZD'] - json_data_gdp['USD'],
                    "USD/CAD": json_data_gdp['USD'] - json_data_gdp['CAD'],
                    "USD/CHF": json_data_gdp['USD'] - json_data_gdp['CHF'],
                    "USD/JPY": json_data_gdp['USD'] - json_data_gdp['JPY'],
                    "USD/MXN": json_data_gdp['USD'] - json_data_gdp['MXN'],
                    "USD/RUB": json_data_gdp['USD'] - json_data_gdp['RUB'],
                    "USD/ZAR": json_data_gdp['USD'] - json_data_gdp['ZAR']}

        escore_diff = {"AUD/CAD": json_data_escore['AUD'] - json_data_escore['CAD'],
                    "AUD/CHF": json_data_escore['AUD'] - json_data_escore['CHF'],
                    "AUD/JPY": json_data_escore['AUD'] - json_data_escore['JPY'],
                    "AUD/NZD": json_data_escore['AUD'] - json_data_escore['NZD'],
                    "AUD/USD": json_data_escore['AUD'] - json_data_escore['USD'],
                    "AUD/ZAR": json_data_escore['AUD'] - json_data_escore['ZAR'],
                    "CAD/JPY": json_data_escore['CAD'] - json_data_escore['JPY'],
                    "CAD/ZAR": json_data_escore['CAD'] - json_data_escore['ZAR'],
                    "CHF/JPY": json_data_escore['CHF'] - json_data_escore['JPY'],
                    "EUR/AUD": json_data_escore['EUR'] - json_data_escore['AUD'],
                    "EUR/CAD": json_data_escore['EUR'] - json_data_escore['CAD'],
                    "EUR/CHF": json_data_escore['EUR'] - json_data_escore['CHF'],
                    "EUR/GBP": json_data_escore['EUR'] - json_data_escore['GBP'],
                    "EUR/JPY": json_data_escore['EUR'] - json_data_escore['JPY'],
                    "EUR/NZD": json_data_escore['EUR'] - json_data_escore['NZD'],
                    "EUR/RUB": json_data_escore['EUR'] - json_data_escore['RUB'],
                    "EUR/USD": json_data_escore['EUR'] - json_data_escore['USD'],
                    "EUR/ZAR": json_data_escore['EUR'] - json_data_escore['ZAR'],
                    "GBP/AUD": json_data_escore['GBP'] - json_data_escore['AUD'],
                    "GBP/CAD": json_data_escore['GBP'] - json_data_escore['CAD'],
                    "GBP/CHF": json_data_escore['GBP'] - json_data_escore['CHF'],
                    "GBP/JPY": json_data_escore['GBP'] - json_data_escore['JPY'],
                    "GBP/NZD": json_data_escore['GBP'] - json_data_escore['NZD'],
                    "GBP/USD": json_data_escore['GBP'] - json_data_escore['USD'],
                    "GBP/ZAR": json_data_escore['GBP'] - json_data_escore['ZAR'],
                    "NZD/CAD": json_data_escore['NZD'] - json_data_escore['CAD'],
                    "NZD/CHF": json_data_escore['NZD'] - json_data_escore['CHF'],
                    "NZD/MXN": json_data_escore['NZD'] - json_data_escore['MXN'],
                    "NZD/USD": json_data_escore['NZD'] - json_data_escore['USD'],
                    "USD/CAD": json_data_escore['USD'] - json_data_escore['CAD'],
                    "USD/CHF": json_data_escore['USD'] - json_data_escore['CHF'],
                    "USD/JPY": json_data_escore['USD'] - json_data_escore['JPY'],
                    "USD/MXN": json_data_escore['USD'] - json_data_escore['MXN'],
                    "USD/RUB": json_data_escore['USD'] - json_data_escore['RUB'],
                    "USD/ZAR": json_data_escore['USD'] - json_data_escore['ZAR']}
        
        cot_diff = {"AUD/CAD": json_data_cot['A_AUD'] - json_data_cot['A_CAD'],
                    "AUD/CHF": json_data_cot['A_AUD'] - json_data_cot['A_CHF'],
                    "AUD/JPY": json_data_cot['A_AUD'] - json_data_cot['A_JPY'],
                    "AUD/NZD": json_data_cot['A_AUD'] - json_data_cot['A_NZD'],
                    "AUD/USD": json_data_cot['A_AUD'] - json_data_cot['A_USD'],
                    "AUD/ZAR": json_data_cot['A_AUD'] - json_data_cot['A_ZAR'],
                    "CAD/JPY": json_data_cot['A_CAD'] - json_data_cot['A_JPY'],
                    "CAD/ZAR": json_data_cot['A_CAD'] - json_data_cot['A_ZAR'],
                    "CHF/JPY": json_data_cot['A_CHF'] - json_data_cot['A_JPY'],
                    "EUR/AUD": json_data_cot['A_EUR'] - json_data_cot['A_AUD'],
                    "EUR/CAD": json_data_cot['A_EUR'] - json_data_cot['A_CAD'],
                    "EUR/CHF": json_data_cot['A_EUR'] - json_data_cot['A_CHF'],
                    "EUR/GBP": json_data_cot['A_EUR'] - json_data_cot['A_GBP'],
                    "EUR/JPY": json_data_cot['A_EUR'] - json_data_cot['A_JPY'],
                    "EUR/NZD": json_data_cot['A_EUR'] - json_data_cot['A_NZD'],
                    "EUR/RUB": json_data_cot['A_EUR'] - json_data_cot['A_RUB'],
                    "EUR/USD": json_data_cot['A_EUR'] - json_data_cot['A_USD'],
                    "EUR/ZAR": json_data_cot['A_EUR'] - json_data_cot['A_ZAR'],
                    "GBP/AUD": json_data_cot['A_GBP'] - json_data_cot['A_AUD'],
                    "GBP/CAD": json_data_cot['A_GBP'] - json_data_cot['A_CAD'],
                    "GBP/CHF": json_data_cot['A_GBP'] - json_data_cot['A_CHF'],
                    "GBP/JPY": json_data_cot['A_GBP'] - json_data_cot['A_JPY'],
                    "GBP/NZD": json_data_cot['A_GBP'] - json_data_cot['A_NZD'],
                    "GBP/USD": json_data_cot['A_GBP'] - json_data_cot['A_USD'],
                    "GBP/ZAR": json_data_cot['A_GBP'] - json_data_cot['A_ZAR'],
                    "NZD/CAD": json_data_cot['A_NZD'] - json_data_cot['A_CAD'],
                    "NZD/CHF": json_data_cot['A_NZD'] - json_data_cot['A_CHF'],
                    "NZD/MXN": json_data_cot['A_NZD'] - json_data_cot['A_MXN'],
                    "NZD/USD": json_data_cot['A_NZD'] - json_data_cot['A_USD'],
                    "USD/CAD": json_data_cot['A_USD'] - json_data_cot['A_CAD'],
                    "USD/CHF": json_data_cot['A_USD'] - json_data_cot['A_CHF'],
                    "USD/JPY": json_data_cot['A_USD'] - json_data_cot['A_JPY'],
                    "USD/MXN": json_data_cot['A_USD'] - json_data_cot['A_MXN'],
                    "USD/RUB": json_data_cot['A_USD'] - json_data_cot['A_RUB'],
                    "USD/ZAR": json_data_cot['A_USD'] - json_data_cot['A_ZAR']}
        
        return jsonify({'ir_diff': ir_diff, 'gdp_diff': gdp_diff,
                    'e_score': escore_diff, 'cot': cot_diff}), 200

    except Exception as ex:
        print(ex)
        return jsonify({'error': f'there is some problem in database {ex}'})
    finally:
        cur.close()
        db.close()

@app.route('/api/v0/GDP_DIFF')
def gdp_diff():
    try:
        arg = request.args['field']
        base = arg[:3]
        quote = arg[-3:]
        db = get_database_connection()
        cur = db.cursor()
        cur.execute(f'SELECT d_date,{base},{quote} FROM GDP')
        rows = cur.fetchall()
        json_data = []
        for t_result in rows:
            result = list(t_result)
            for i in range(len(result)):
                if not result[i]:
                    result[i] = 0
            json_data.append({"Base" : result[1], "Quote": result[2], 'Date': result[0], 'Diff': result[1] - result[2]})
        return jsonify(json_data), 200
    except Exception as e:
        print(e)
        return jsonify({'error': f'there is some problem in database {e}'})
    finally:
        cur.close()
        db.close()

@app.route('/api/v0/COT_DIFF')
def cot_diff():
    try:
        arg = request.args['field']
        base = arg[:3]
        quote = arg[-3:]
        db = get_database_connection()
        cur = db.cursor()
        cur.execute(f'SELECT d_date,A_{base},A_{quote} FROM COT')
        rows = cur.fetchall()
        json_data = []
        for t_result in rows:
            result = list(t_result)
            for i in range(len(result)):
                if not result[i]:
                    result[i] = 0
            json_data.append({"Base" : result[1], "Quote": result[2], 'Date': result[0], 'Diff': result[1] - result[2]})
        return jsonify(json_data), 200
    except Exception as e:
        print(e)
        return jsonify({'error': f'there is some problem in database {e}'})
    finally:
        cur.close()
        db.close()

@app.route('/api/v0/E_SCORE_DIFF')
def EScore_diff():
    try:
        arg = request.args['field']
        base = arg[:3]
        quote = arg[-3:]
        db = get_database_connection()
        cur = db.cursor()
        cur.execute(f'SELECT d_date,{base},{quote} FROM E_SCORE')
        rows = cur.fetchall()
        json_data = []
        for t_result in rows:
            result = list(t_result)
            for i in range(len(result)):
                if not result[i]:
                    result[i] = 0
            json_data.append({"Base" : result[1], "Quote": result[2], 'Date': result[0], 'Diff': result[1] - result[2]})
        return jsonify(json_data), 200
    except Exception as e:
        print(e)
        return jsonify({'error': f'there is some problem in database {e}'})
    finally:
        cur.close()
        db.close()


@app.route('/api/v0/IR_DIFF')
def ir_diff():
    try:
        arg = request.args['field']
        base = arg[:3]
        quote = arg[-3:]
        db = get_database_connection()
        cur = db.cursor()
        cur.execute(f'SELECT d_date,{base},{quote} FROM IR')
        rows = cur.fetchall()
        json_data = []
        for t_result in rows:
            result = list(t_result)
            for i in range(len(result)):
                if not result[i]:
                    result[i] = 0
            json_data.append({"Base" : result[1], "Quote": result[2], 'Date': result[0], 'Diff': result[1] - result[2]})
        return jsonify(json_data), 200
    except Exception as e:
        print(e)
        return jsonify({'error': f'there is some problem in database {e}'})
    finally:
        cur.close()
        db.close()
