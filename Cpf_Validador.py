class ValidarCPF:
    def __init__(self, cpf):

        """
            Este é o construtor que recebe o número do CPF como argumento.
        """

        self.cpf = cpf

    def cpf_formatado(self):

        """
            Este método formata o número do CPF removendo quaisquer pontos ou hífens.
        """


        self.cpf = self.cpf.replace('.', '')
        self.cpf = self.cpf.replace('-', '')
        return self.cpf
    
    def cpf_valido(self):


        """
           Este método verifica se o número do CPF é válido verificando se é numérico e se possui
           11 dígitos. Se não for válido, ele solicita que o usuário insira um número de CPF válido.
        """

        while not self.cpf.isnumeric() or len(self.cpf) != 11:
            self.cpf = (input('Erro! DIGITE UM NÚMERO VÁLIDO: '))
        return self.cpf
    
    def digitos_iguais(self):


        """
             Este método verifica se todos os dígitos do número do CPF são iguais, o que tornaria o número inválido.
        """


        igual = 0
        for i in range(11):
            igual += int(self.cpf[i])
        if int(self.cpf[0]) * 11 == igual:    
            print('CPF INVÁLIDO. TODOS DIGITOS SÃO IGUAIS!')    
            return False
        return True
    
    def digitov1(self, VerificaDigitos):    
           
        """
             Este método calcula o segundo dígito verificador do número do CPF.
        """
       
        Validacao1 = 10
        Somadig1 = 0
        for Digito1 in VerificaDigitos:
            resultado = int(Digito1) * Validacao1
            Validacao1 -= 1
            Somadig1 += resultado
        resto = Somadig1 % 11
        if resto < 2:
            dv1 = 0
        else:
            dv1 = 11 - resto
        return dv1
    
    def verifica_digito2(self, cpfdig10):

        """
             Este método calcula o segundo dígito verificador do número do CPF.
        """             

        Validacao2 = 11
        Somadig2 = 0
        for Digito2 in cpfdig10:
            resultado = int(Digito2) * Validacao2
            Validacao2 -= 1
            Somadig2 += resultado
        resto_2 = Somadig2 % 11
        if resto_2 < 2:
            dv2 = 0
        else:
            dv2 = 11 - resto_2
        return dv2
    
    def valida_cpf(self):


        """
             Este é o método principal que chama os outros métodos e realiza
             o processo de validação. Imprime "CPF VÁLIDO" se o número do CPF
             for válido e "CPF INVÁLIDO" caso contrário.
        """

        self.cpf = self.cpf_formatado()
        self.cpf = self.cpf_valido()
        if not self.digitos_iguais():
            return

        VerificaDigitos = self.cpf[:9]

        dv1 = self.digitov1(VerificaDigitos)

        cpfdig10 = VerificaDigitos + str(dv1)        

        dv2 = self.verifica_digito2(cpfdig10)

        cpf_valido = str(self.cpf[:9]) + str(dv1) + str(dv2)

        if cpf_valido == self.cpf:
            print(' CPF VÁLIDO .')
        else:
            print(' CPF INVÁLIDO .')

    def salva_resultados(self):

        """
            A função "salva_resultados" recebe um objeto self como entrada e executa as seguintes ações:
            chama o método "valida_cpf" no objeto self e armazena o resultado na variável "resultado".
            Se a variável "resultado" for true (ou seja, avaliada como True), a função anexa o atributo 
            "cpf" do objeto self a um arquivo chamado "resultados.txt".
            Se a variável "resultado" for falsa (ou seja, avaliada como False), 
            a função anexa a representação de string da variável "resultado" a um arquivo chamado "erros.log".

        """

        resultado = self.valida_cpf()
        if resultado:
            with open('resultados.txt', 'a') as arquivo:
                arquivo.write(self.cpf + '\n')
        else:
            with open( 'erros.log', 'a') as arquivo: 
                arquivo.write(str(resultado) + '\n')        


cpf = ValidarCPF("81597037087")
result = cpf.valida_cpf()
print(result) 
