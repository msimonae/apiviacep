#from requests import HTTPSession

import requests

def main():

    print('#############################')
    print('####### Consulta CEP ########')
    print('#############################')
    print('')

    cep_input = input('Digite um cep com 8 dígitos sem "-" :')

    if len(cep_input)!=8:
        print('Quantidade de dígitos inválida ! Digite 8 digitos do CEP')

    #http = HTTPSession()
    #request = http.request('get', 'https://viacep.com.br/ws/{}/json/'.format(cep_input))

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('==> CEP Encontrado <==')
        print('CEP: {}'.format(address_data['cep']))
        print('Rua: {}'.format(address_data['logradouro']))
        print('Complemento: {}'.format(address_data['complemento']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))
    else:
        print('CEP {} digitado Inválido !'.format(cep_input))

    print('---------------------------------------------------------')
    option = int(input('Deseja realizar uma outra consulta ?\n1. Sim\n2. Sair\n'))        
    if option == 1:
        main()
    else:
        print('Saindo ......')

if __name__ == '__main__':
    main()
