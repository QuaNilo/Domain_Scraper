import whois
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def domain():
    domain = request.args.get('domain')
    domain_extensions = [
        '.com', '.net', '.org', '.name', '.me', '.ae', '.au', '.ru', '.us', '.uk',
        '.fr', '.nl', '.lt', '.fi', '.hr', '.hn', '.hk', '.jp', '.pl', '.br', '.eu',
        '.ee', '.kr', '.pt', '.bg', '.de', '.at', '.ca', '.be', '.рф', '.info', '.su',
        '.si', '.kg', '.io', '.biz', '.mobi', '.ch', '.li', '.id', '.sk', '.se', '.no',
        '.nu', '.is', '.dk', '.it', '.mx', '.ai', '.il', '.in', '.cat', '.ie', '.nz',
        '.space', '.lu', '.cz', '.online', '.cn', '.app', '.money', '.cl', '.ar', '.by',
        '.cr', '.do', '.jobs', '.lat', '.pe', '.ro', '.sa', '.tw', '.tr', '.ve', '.ua',
        '.укр', '.kz', '.ir', '.中国', '.website', '.sg', '.ml', '.ooo', '.group', '.market',
        '.za', '.bw', '.bz', '.city', '.design', '.studio', '.style', '.рус', '.life', '.tn'
    ]

    if not domain:
        return jsonify({'success': False, 'error': {'type': 'NoTLDProvided', 'message': f'Please insert a domain, valid domains : {str(domain_extensions)}'}}), 400

    domain_tld = '.' + domain.split('.')[-1]

    if domain_tld not in domain_extensions:
        return jsonify({'success': False, 'error': {'type': 'InvalidTLD', 'message': f'Please insert a valid domain, valid domains : {str(domain_extensions)}'}}), 400
    try:
        results = whois.whois(str(domain))
        is_available = True if results['domain_name'] == None else False
        response = {'success': True,  'data': {'results': results}, 'is_available': is_available}

        return jsonify(response), 200

    except Exception as e:
        app.logger.error(f'Failed to get info for domain : {str(e)}')
        return jsonify( {'success': False, 'error': {'type': 'genericError', 'message': f'{str(e)}'}}), 500


if __name__ == '__main__':
    app.run(debug=True)
