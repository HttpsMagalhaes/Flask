import re

class ValidaDados:

    @staticmethod
    def eh_cnpj(cnpj):
        # Remove caracteres não numéricos (pontos, traços, barras)
        cnpj = re.sub(r'[^0-9]', '', cnpj)

        # Verifica se tem 14 dígitos
        if len(cnpj) != 14:
            return False

        # Verifica se todos os dígitos são iguais
        if len(set(cnpj)) == 1:
            return False

        # Cálculo do primeiro dígito verificador
        # Pesos: 5,4,3,2,9,8,7,6,5,4,3,2
        pesos_primeiro = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = 0
        for i in range(12):
            soma += int(cnpj[i]) * pesos_primeiro[i]

        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto

        if digito1 != int(cnpj[12]):
            return False

        # Cálculo do segundo dígito verificador
        # Pesos: 6,5,4,3,2,9,8,7,6,5,4,3,2
        pesos_segundo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = 0
        for i in range(13):
            soma += int(cnpj[i]) * pesos_segundo[i]

        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto

        # Retorna True se o segundo dígito bater, senão False
        return digito2 == int(cnpj[13])