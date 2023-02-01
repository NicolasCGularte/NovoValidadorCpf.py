class ValidadeCpf:
    def __init__(self, cpf):
        self.cpf = cpf

    def cpf_formatado(self):
        cpf = self.cpf
        if len(cpf) == 11:
            cpf = cpf.replace('.', '')
            cpf = cpf.replace('-', '')
            return cpf

    def cpf_valido(self):
        while not self.cpf.isnumeric() or len(self.cpf) != 11:
            self.cpf = input('Digite um CPF válido: ')
        return self.cpf

    def digitos_iguais(self):
        igual = 0
        for i in range(1, 11):
            i += 1
            if self.cpf[i] == self.cpf[i - 1]:
                igual += 1
        return igual

    def digito_verificador1(self):
        valido = 10
        soma1 = 0
        for j in range(0, 9):
            soma1 += int(self.cpf[j]) * valido
            valido -= 1
        resto = soma1 % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto
        return digito1

    def digito_verificador2(self):
        valido = 11
        soma2 = 0
        for k in range(0, 10):
            soma2 += int(self.cpf[k]) * valido
            valido -= 1
        resto = soma2 % 11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto
        return digito2

    def valida_cpf(self):
        cpf = self.cpf_formatado()
        self.cpf_valido()
        if self.digitos_iguais() == 10:
            return False
        else:
            digito1 = self.digito_verificador1()
            digito2 = self.digito_verificador2()
            if int(self.cpf[9]) == digito1 and int(self.cpf[10]) == digito2:
                return True
            else:
                return False






















               

























                



